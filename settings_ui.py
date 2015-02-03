# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\Darren\Python\SR830ResistanceMeasure\settings.ui'
#
# Created: Fri Jan 30 14:20:35 2015
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(357, 473)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.tSleepTime = QFNumberEdit(Dialog)
        self.tSleepTime.setObjectName(_fromUtf8("tSleepTime"))
        self.horizontalLayout.addWidget(self.tSleepTime)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.cKeithGPIB = QtGui.QComboBox(Dialog)
        self.cKeithGPIB.setObjectName(_fromUtf8("cKeithGPIB"))
        self.horizontalLayout_3.addWidget(self.cKeithGPIB)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_5.addWidget(self.label_6)
        self.tCompliance = QFNumberEdit(Dialog)
        self.tCompliance.setObjectName(_fromUtf8("tCompliance"))
        self.horizontalLayout_5.addWidget(self.tCompliance)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_6.addWidget(self.label_7)
        self.chMeasureReverse = QtGui.QCheckBox(Dialog)
        self.chMeasureReverse.setText(_fromUtf8(""))
        self.chMeasureReverse.setObjectName(_fromUtf8("chMeasureReverse"))
        self.horizontalLayout_6.addWidget(self.chMeasureReverse)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        self.cSRGPIB = QtGui.QComboBox(Dialog)
        self.cSRGPIB.setObjectName(_fromUtf8("cSRGPIB"))
        self.horizontalLayout_4.addWidget(self.cSRGPIB)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.chMeasurePhase = QtGui.QCheckBox(Dialog)
        self.chMeasurePhase.setText(_fromUtf8(""))
        self.chMeasurePhase.setObjectName(_fromUtf8("chMeasurePhase"))
        self.horizontalLayout_2.addWidget(self.chMeasurePhase)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_2.addWidget(self.label_8)
        self.tSeriesResistance = QFNumberEdit(Dialog)
        self.tSeriesResistance.setObjectName(_fromUtf8("tSeriesResistance"))
        self.horizontalLayout_2.addWidget(self.tSeriesResistance)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.tSaveComments = QtGui.QTextEdit(Dialog)
        self.tSaveComments.setObjectName(_fromUtf8("tSaveComments"))
        self.verticalLayout.addWidget(self.tSaveComments)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Settings", None))
        self.label.setText(_translate("Dialog", "Gate Step Sleep (s)", None))
        self.label_4.setText(_translate("Dialog", "Keithley GPIB:", None))
        self.label_6.setText(_translate("Dialog", "Keithley Compliance (A)", None))
        self.label_7.setText(_translate("Dialog", "Measure Reverse", None))
        self.label_5.setText(_translate("Dialog", "SR830 GPIB:", None))
        self.label_3.setText(_translate("Dialog", "Measure Phase", None))
        self.label_8.setText(_translate("Dialog", "Series Resistance (Ohms)", None))
        self.tSeriesResistance.setText(_translate("Dialog", "1e6", None))
        self.label_2.setText(_translate("Dialog", "Save Comments", None))
        self.tSaveComments.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))

from customQt import QFNumberEdit
