# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\Darren\Python\SR830ResistanceMeasure\MainWindow.ui'
#
# Created: Fri Jan 30 14:03:40 2015
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(565, 512)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gResistance = PlotWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.gResistance.sizePolicy().hasHeightForWidth())
        self.gResistance.setSizePolicy(sizePolicy)
        self.gResistance.setObjectName(_fromUtf8("gResistance"))
        self.verticalLayout.addWidget(self.gResistance)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.tGateStart = QFNumberEdit(self.centralwidget)
        self.tGateStart.setObjectName(_fromUtf8("tGateStart"))
        self.horizontalLayout.addWidget(self.tGateStart)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.tGateStep = QFNumberEdit(self.centralwidget)
        self.tGateStep.setObjectName(_fromUtf8("tGateStep"))
        self.horizontalLayout.addWidget(self.tGateStep)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.tGateEnd = QFNumberEdit(self.centralwidget)
        self.tGateEnd.setObjectName(_fromUtf8("tGateEnd"))
        self.horizontalLayout.addWidget(self.tGateEnd)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.tMeasureEvery = QINumberEdit(self.centralwidget)
        self.tMeasureEvery.setObjectName(_fromUtf8("tMeasureEvery"))
        self.horizontalLayout_3.addWidget(self.tMeasureEvery)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.bStartScan = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bStartScan.sizePolicy().hasHeightForWidth())
        self.bStartScan.setSizePolicy(sizePolicy)
        self.bStartScan.setObjectName(_fromUtf8("bStartScan"))
        self.gridLayout.addWidget(self.bStartScan, 0, 0, 1, 1)
        self.bAbortScan = QtGui.QPushButton(self.centralwidget)
        self.bAbortScan.setObjectName(_fromUtf8("bAbortScan"))
        self.gridLayout.addWidget(self.bAbortScan, 1, 0, 1, 1)
        self.bResetData = QtGui.QPushButton(self.centralwidget)
        self.bResetData.setObjectName(_fromUtf8("bResetData"))
        self.gridLayout.addWidget(self.bResetData, 0, 1, 1, 1)
        self.bSaveData = QtGui.QPushButton(self.centralwidget)
        self.bSaveData.setObjectName(_fromUtf8("bSaveData"))
        self.gridLayout.addWidget(self.bSaveData, 1, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 565, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.mFileSettings = QtGui.QAction(MainWindow)
        self.mFileSettings.setObjectName(_fromUtf8("mFileSettings"))
        self.mFileExit = QtGui.QAction(MainWindow)
        self.mFileExit.setObjectName(_fromUtf8("mFileExit"))
        self.menuFile.addAction(self.mFileSettings)
        self.menuFile.addAction(self.mFileExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SR830 Measurement", None))
        self.label.setText(_translate("MainWindow", "Gate Start (V)", None))
        self.tGateStart.setText(_translate("MainWindow", "0", None))
        self.label_2.setText(_translate("MainWindow", "Gate Step (V)", None))
        self.tGateStep.setText(_translate("MainWindow", ".1", None))
        self.label_3.setText(_translate("MainWindow", "Gate End (V)", None))
        self.tGateEnd.setText(_translate("MainWindow", "10", None))
        self.label_4.setText(_translate("MainWindow", "Measure Every", None))
        self.tMeasureEvery.setText(_translate("MainWindow", "1", None))
        self.bStartScan.setText(_translate("MainWindow", "Start", None))
        self.bAbortScan.setText(_translate("MainWindow", "Abort", None))
        self.bResetData.setText(_translate("MainWindow", "Reset Data", None))
        self.bSaveData.setText(_translate("MainWindow", "Save Data", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.mFileSettings.setText(_translate("MainWindow", "Settings...", None))
        self.mFileExit.setText(_translate("MainWindow", "Exit", None))

from customQt import QINumberEdit, QFNumberEdit
from pyqtgraph import PlotWidget
