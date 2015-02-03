# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 10:28:08 2015

@author: dvalovcin
"""

import numpy as np
from PyQt4 import QtCore, QtGui
from Instruments import Keithley2400Instr, SR830Instr
from settings_ui import Ui_Dialog
from MainWindow_ui import Ui_MainWindow
import re
import threading
import time
import copy
import pyqtgraph as pg
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')
try:
    import visa
except:
    print 'Error. VISA library not installed' 

class WorkTh(QtCore.QThread):
    def __init__(self, target = None, args = None, parent = None):
        super(WorkTh, self).__init__(parent)
        self.target = target
        self.args = args
    def run(self):
        self.target(self.args)
    def start(self):
        self.target(self.args)

class Win(QtGui.QMainWindow):
    keith = None
    SR830 = None
    resSig = QtCore.pyqtSignal(object)
    phaSig = QtCore.pyqtSignal(object)
    statusSig = QtCore.pyqtSignal(object)
    def __init__(self):
        super(Win,self).__init__()
        #Alll of the settings
        self.settings = dict()
        self.settings['saveLoc'] = ''
        self.settings['resSaveName'] = ''
        self.settings['phaSaveName'] = ''
        self.settings['saveComments'] = ''
        self.settings['kGPIB'] = 'Fake'
        self.settings['sGPIB'] = 'Fake'
        self.settings['measurePhase'] = False
        self.settings['measureReverse'] = False
        self.settings['stepSleep'] = 0.2
        self.settings['kCompliance'] = 1e-3
        self.settings['seriesResistance'] = 1e6
        self.settings['GPIBChoices'] = []
        
        self.openKeith()
        self.openSR830()
        self.initUI()
        
        self.startV = self.parseInp(self.ui.tGateStart.text())
        self.stepV = self.parseInp(self.ui.tGateStep.text())
        self.endV = self.parseInp(self.ui.tGateEnd.text())
        self.measureEvery = int(self.parseInp(self.ui.tMeasureEvery.text()))
        
        self.statusSig.connect(self.updateStatusBar)
        self.resSig.connect(self.updateResistance)
        self.phaSig.connect(self.updatePhase)
        
        self.resistances = np.empty((0,2))
        self.phases = np.empty((0,2))
        self.voltage = 0
        self.runFlag = False
        self.show()
        
    def initUI(self):
        #Import ui file from designer
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
        #initialize plot
        self.rGraph = self.ui.gResistance.plot(pen='k')
#        self.ui.gResistance.setBackground('w')
#        self.ui.gResistance.setForegroundBrush(pg.mkBrush('k'))
#        self.ui.gResistance.setBackgroundBrush(pg.mkBrush('k'))
        self.p1 = self.ui.gResistance.plotItem
        self.p1.setLabel('top',text='Resistance')
        self.p1.setLabel('left',text='Resistance',units='O')
        self.p1.setLabel('bottom',text='voltage', units='V')
        
        #http://bazaar.launchpad.net/~luke-campagnola/pyqtgraph/inp/view/head:/examples/MultiplePlotAxes.py
        #Need to do all this nonsense to make it plot on two different axes. 
        #Also note the self.updatePhase plot which shows how to update the data.         
        self.p2 = pg.ViewBox()
        self.p1.showAxis('right')
        self.p1.scene().addItem(self.p2)
        self.p1.getAxis('right').linkToView(self.p2)
        self.p2.setXLink(self.p1)
        self.p1.getAxis('right').setLabel('Phase', units='deg', color='#ff0000')
        self.pGraph = pg.PlotCurveItem(pen='r')
        self.p2.addItem(self.pGraph)
        
        #need to set it up so that when the window (and thus main plotItem) is
        #resized, it informs the ViewBox for the second plot that it must update itself.
        self.p1.vb.sigResized.connect(lambda: self.p2.setGeometry(self.p1.vb.sceneBoundingRect()))
        
        
        #Connect all the things
        self.ui.bStartScan.clicked.connect(self.startScan)
        self.ui.bAbortScan.clicked.connect(self.abortScan)
        self.ui.bAbortScan.setEnabled(False)
        self.ui.bSaveData.clicked.connect(self.saveData)
        self.ui.bResetData.clicked.connect(self.resetData)
        
        self.ui.mFileExit.triggered.connect(self.closeEvent)
        self.ui.mFileSettings.triggered.connect(self.launchSettings)
        
        self.ui.tGateStart.textAccepted.connect(self.acceptTextChanges)
        self.ui.tGateStep.textAccepted.connect(self.acceptTextChanges)
        self.ui.tGateEnd.textAccepted.connect(self.acceptTextChanges)
        self.ui.tMeasureEvery.textAccepted.connect(self.acceptTextChanges)
        
    def acceptTextChanges(self, value):
        if type(value) is bool:
            self.statusSig.emit('Invalid Value')
        
    def closeEvent(self, event):
        self.abortScan()
        self.keith.close()
        self.SR830.close()
        self.close()
        
    def launchSettings(self):
        try:
            res = list(visa.ResourceManager().list_resources())
            res = [i.encode('ascii') for i in res]
        except:
            self.statusSig.emit(['Error loading GPIB list', 5000])
            res = ['a', 'b','c']
        res.append('Fake')
        self.settings['GPIBChoices'] = res
        
        #need to pass a copy of the settings. Otherwise it passes the reference,
        #thus changing the values and we're unable to see whether things have changed.
        newSettings, ok = SettingsDialog.getSettings(self, copy.copy(self.settings))
        if not ok:
            print 'canceled'
            return
        
        #Need to check to see if the GPIB values changed so we can update them.
        #The opening procedure opens a fake isntrument if things go wrong, which 
        #means we can't assign the settings dict after calling openKeith() as that would
        #potentially overwrite if we needed to open a fake instr.
        #
        #We get the old values before updating the settings. Th
        
        oldkGPIB = self.settings['kGPIB']
        oldsGPIB = self.settings['sGPIB']

        self.settings = newSettings
        print oldkGPIB, newSettings['kGPIB']
        if not oldkGPIB == newSettings['kGPIB']:
            self.keith.close()
            self.settings['kGPIB'] = newSettings['kGPIB']
            self.openKeith()
        print oldsGPIB, newSettings['sGPIB']
        if not oldsGPIB == newSettings['sGPIB']:
            self.SR830.close()
            self.settings['sGPIB'] = newSettings['sGPIB']
            self.openSR830()
            
                
        
        
        
    def openKeith(self):
        try:
            self.keith = Keithley2400Instr(self.settings['kGPIB'], compliance=self.settings['kCompliance'])
            print 'Keithley opened'
        except:
            print 'Error opening Keithley. Adding Fake'
            self.settings['kGPIB'] = 'Fake'
            self.keith = Keithley2400Instr(self.settings['kGPIB'], compliance=self.settings['kCompliance'])
            
    
    def openSR830(self):
        try:
            self.SR830 = SR830Instr(self.settings['sGPIB'])
            print 'SR830 opened'
        except:
            print 'Error opening SR830. Adding Fake'
            self.settings['sGPIB'] = 'Fake'
            self.SR830 = SR830Instr(self.settings['sGPIB'])
            
    def parseInp(self, inp):
        ret = None
        #see if we can just turn it into a number and leave if we can
        try:
            ret = float(inp)
            return ret
        except:
            pass
        #tests to see whether digit is whole number or decimal, and if it has 
        #some modifier at the end
        toMatch = re.compile('-?(\d+\.?\d*|\d*\.\d+)(m|u|n|M|k)?\Z')
        if re.match(toMatch, inp):
            convDict = {'m': 1e-3, 'u':1e-6, 'n':1e-9, 'M':1e6, 'k':1e3}
            try:
                ret = (float(inp[:-1]) * #convert first part to number
                   convDict[[b for b in convDict.keys() if b in inp][0]]) #and multiply by the exponential
                return ret
            except:
                print 'uh oh'
        else:
            raise TypeError('Error with input', str(inp))
        
    def startScan(self):
        #test inputs
        try:
            self.startV = self.parseInp(self.ui.tGateStart.text())
            self.ui.tGateStart.setText(str(self.startV))
            self.stepV = self.parseInp(self.ui.tGateStep.text())
            self.ui.tGateStep.setText(str(self.stepV))
            self.endV = self.parseInp(self.ui.tGateEnd.text())
            self.ui.tGateEnd.setText(str(self.endV))
            m = self.parseInp(self.ui.tMeasureEvery.text())
            self.measureEvery = int(m)
        except Exception as e:
            self.ui.statusbar.showMessage('Error converting input: {}'.format(e[1]), 3000)
            return
        if (self.endV-self.startV) * self.stepV < 0:
            self.ui.statusbar.showMessage('Incorrect step size', 3000)
            return
        #disable all the buttons and inputs so they don't get changed and confuse the user
        self.ui.bStartScan.setEnabled(False)
        self.ui.bAbortScan.setEnabled(True)
        self.ui.tGateStart.setEnabled(False)
        self.ui.tGateStep.setEnabled(False)
        self.ui.tGateEnd.setEnabled(False)
        self.ui.tMeasureEvery.setEnabled(False)
        self.ui.mFileSettings.setEnabled(False)
        
        #Start the thread to take the data
        self.runFlag = True
        self.scanningThread = threading.Thread(target = self.runScan, args = (self.startV, self.stepV, self.endV))
        self.scanningThread.start()
#        self.scanningThread = QtCore.QThread(target=self.runScan, args = (start, step, end))
#        self.scanningThread.finished.connect(self.enableStart)
#        self.scanningThread.start()
#        self.scanningThread = WorkTh(target=self.runScan, args = (start, step, end), parent = self)
#        self.scanningThread.finished.connect(self.enableStart)
#        self.scanningThread.run()
        
    def enableStart(self):
        self.ui.bStartScan.setEnabled(True)
        self.statusSig.emit('Scan Finished')
        self.abortScan()
    
    def abortScan(self):
        #Re-enable all of the buttons/inputs
        self.ui.bAbortScan.setEnabled(False)
        self.ui.tGateStart.setEnabled(True)
        self.ui.tGateStep.setEnabled(True)
        self.ui.tGateEnd.setEnabled(True)
        self.ui.tMeasureEvery.setEnabled(True)
        self.ui.mFileSettings.setEnabled(True)
        if self.runFlag:
            self.runFlag = False
            self.statusSig.emit('Aborting...')
            
            
    def runScan(self, *args):
        print 'run', args
        start = args[0]
        step = args[1]
        end = args[2]
        voltageRange = np.arange(start, end, step)
        voltageRange = np.append(voltageRange, end)
        
        self.keith.turnOn()
        print 'turned on'
        
        self.referenceVoltage = self.SR830.getRefVolt()
        self.appliedCurrent = self.referenceVoltage/self.settings['seriesResistance']
        
        if not start == 0:
            print 'not equal'
            startStep = step
            if start*step<0:
                startStep = -step
            for voltage in np.arange(0, start, startStep):
                if not self.runFlag:
                    break
                self.doRamp(voltage)
        else:
            print 'equal'
            
        measureCount = self.measureEvery
        
        for voltage in voltageRange:
            #Make sure the main thread didn't abort the run
            if not self.runFlag:
                break
            measureCount = measureCount - 1
            if measureCount == 0 or voltage==voltageRange[0]:
                measureCount = self.measureEvery
                if not self.doMeasurementPoint(voltage):
                    print 'Error: Time out?'
                    continue
            else:
                self.doRamp(voltage)
                    
        if self.settings['measureReverse']:
            for voltage in voltageRange[::-1]:
                #Make sure the main thread didn't abort the run
                if not self.runFlag:
                    break
                measureCount = measureCount - 1
                if measureCount == 0 or voltage==voltageRange[0]:
                    measureCount = self.measureEvery
                    if not self.doMeasurementPoint(voltage):
                        print 'Error: Time out?'
                        continue
                else:
                    self.doRamp(voltage)
        
        for voltage in np.arange(self.voltage, 0, -abs(step)*np.sign(self.voltage)):
            self.doRamp(voltage)
            
        self.keith.setVoltage(0)
        self.keith.turnOff()        
        self.ui.bStartScan.setEnabled(True)
        self.statusSig.emit('Scan Finished')
        self.abortScan()
        
    def doRamp(self, voltage):
        self.voltage = voltage
        self.keith.setVoltage(voltage)
        time.sleep(self.settings['stepSleep'])
        self.statusSig.emit('Ramping. Voltage: '+str(voltage))
        
    def doMeasurementPoint(self, voltage, reverse = False):
        self.voltage = voltage
        self.statusSig.emit('Measuring. Voltage: '+str(voltage))
        self.keith.setVoltage(voltage)
        ret = False
        time.sleep(.1) #Sleep incase there's a lag between updating the scope
        if self.settings['measurePhase']:
            #returns the magnitude of the measured voltage and the phase
            val = self.SR830.getMultiple('r', 't')
            if not val:
                return ret
            ret = True
            r = val[0]
            t = val[1]
            res = r/self.appliedCurrent
            self.resSig.emit([[voltage, res]])
            self.phaSig.emit([[voltage, t]])
        else:
            r = self.SR830.getChannel('r')
            if not r:
                return ret
            ret = True
            res = r/self.appliedCurrent
            self.resSig.emit([[voltage, res]])
        return ret
        
        
        
    def saveData(self):
        fname = str(QtGui.QFileDialog.getSaveFileName(self, "Resistance Save File...",directory=self.settings['saveLoc']))
        if not fname=='':
                directory = fname[:-fname[::-1].find('/')]
                self.settings['saveLoc'] = directory
                np.savetxt(fname, self.resistances, header = self.genSaveHeader() + '\nGate (V), Resistance (Ohms)')
        if self.settings['measurePhase']:
            fname = str(QtGui.QFileDialog.getSaveFileName(self, "Phase Save File...",directory=self.settings['saveLoc']))
            if not fname=='':
                    directory = fname[:-fname[::-1].find('/')]
                    self.settings['saveLoc'] = directory
                    np.savetxt(fname, self.phases, header = self.genSaveHeader() + '\nGate (V), Phase (deg)')
    
    def genSaveHeader(self):
        st = 'Time between steps(s): '+ str(self.settings['stepSleep'])
        st += '\nStep size(V): ' + str(self.stepV)
        st += '\nMeasured every: '+ str(self.measureEvery)
        st += '\nCompliance(A): ' + str(self.settings['kCompliance'])
        st += '\nSeries Resistor(Ohms): ' + str(self.settings['seriesResistance'])
        st += self.settings['saveComments']
        return st
            
    
    def resetData(self):
        self.resistances = np.empty((0,2))
        self.rGraph.setData([],[])
        self.phases = np.empty((0,2))
        self.pGraph.setData([],[])
        
    def updateStatusBar(self, args):
        '''function to update the status bar. Connects to a signal so it
           can be used from different threads. Pass a string to emit a message for
           3 seconds. Else pass a list, the first element the message and the second
           a ms value for the timeout'''
        if type(args) is str:
            self.ui.statusbar.showMessage(args, 3000)
        else:
            self.ui.statusbar.showMessage(args[0], args[1])
            
    def updateResistance(self, data):
        self.resistances = np.append(self.resistances, data, axis=0)
        self.rGraph.setData(self.resistances)
    
    def updatePhase(self, data):
        self.phases = np.append(self.phases, data, axis=0)
        self.pGraph.setData(self.phases[:,0], self.phases[:,1])
        self.p2.setGeometry(self.p1.vb.sceneBoundingRect())
    
class SettingsDialog(QtGui.QDialog):
    def __init__(self, parent = None, settings=None):
        super(SettingsDialog, self).__init__(parent)
        self.initUI(settings)
        
    def initUI(self, settings):
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.tSleepTime.setText(str(settings['stepSleep']))
        self.ui.cKeithGPIB.insertItems(0, settings['GPIBChoices'])
        self.ui.cKeithGPIB.setCurrentIndex(
                    settings['GPIBChoices'].index(settings['kGPIB'])
                                            )
        self.ui.tCompliance.setText(str(settings['kCompliance']))
        self.ui.chMeasurePhase.setChecked(settings['measurePhase'])
        self.ui.cSRGPIB.insertItems(0, settings['GPIBChoices'])
        self.ui.cSRGPIB.setCurrentIndex(
                    settings['GPIBChoices'].index(settings['sGPIB'])
                                            )
        self.ui.chMeasureReverse.setChecked(settings['measureReverse'])
        self.ui.tSeriesResistance.setText(str(settings['seriesResistance']))
        self.ui.tSaveComments.setText(settings['saveComments'])
        
    @staticmethod
    def getSettings(parent = None, settings = None):
        dialog = SettingsDialog(parent, settings)
        result = dialog.exec_()
        settings['stepSleep'] = float(dialog.ui.tSleepTime.text())
        settings['kGPIB'] = str(dialog.ui.cKeithGPIB.currentText())
        settings['kCompliance'] = float(dialog.ui.tCompliance.text())
        settings['measurePhase'] = dialog.ui.chMeasurePhase.isChecked()
        settings['sGPIB'] = str(dialog.ui.cSRGPIB.currentText())
        settings['measureReverse'] = dialog.ui.chMeasureReverse.isChecked()
        settings['seriesResistance'] = float(dialog.ui.tSeriesResistance.text())
        settings['saveComments'] = dialog.ui.tSaveComments.toPlainText()
        return (settings, result==QtGui.QDialog.Accepted)
        































def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    ex = Win()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()









