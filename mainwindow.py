# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Jul  4 08:22:18 2013
#      by: PyQt4 UI code generator 4.10
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
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 150, 361, 16))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_Import = QtGui.QMenu(self.menu_File)
        self.menu_Import.setObjectName(_fromUtf8("menu_Import"))
        self.menu_Edit = QtGui.QMenu(self.menubar)
        self.menu_Edit.setObjectName(_fromUtf8("menu_Edit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_Open = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.action_Open.setFont(font)
        self.action_Open.setObjectName(_fromUtf8("action_Open"))
        self.action_Close = QtGui.QAction(MainWindow)
        self.action_Close.setObjectName(_fromUtf8("action_Close"))
        self.action_File = QtGui.QAction(MainWindow)
        self.action_File.setObjectName(_fromUtf8("action_File"))
        self.action_Object = QtGui.QAction(MainWindow)
        self.action_Object.setObjectName(_fromUtf8("action_Object"))
        self.action_Cut = QtGui.QAction(MainWindow)
        self.action_Cut.setObjectName(_fromUtf8("action_Cut"))
        self.action_Paste = QtGui.QAction(MainWindow)
        self.action_Paste.setObjectName(_fromUtf8("action_Paste"))
        self.action_Clear = QtGui.QAction(MainWindow)
        self.action_Clear.setObjectName(_fromUtf8("action_Clear"))
        self.menu_Import.addAction(self.action_File)
        self.menu_Import.addAction(self.action_Object)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Close)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.menu_Import.menuAction())
        self.menu_Edit.addAction(self.action_Cut)
        self.menu_Edit.addAction(self.action_Paste)
        self.menu_Edit.addAction(self.action_Clear)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_Close, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QObject.connect(self.action_Clear, QtCore.SIGNAL(_fromUtf8("activated()")), self.label.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "TextLabel", None))
        self.menu_File.setTitle(_translate("MainWindow", "&File", None))
        self.menu_Import.setTitle(_translate("MainWindow", "&Import", None))
        self.menu_Edit.setTitle(_translate("MainWindow", "&Edit", None))
        self.action_Open.setText(_translate("MainWindow", "&Open", None))
        self.action_Close.setText(_translate("MainWindow", "&Close", None))
        self.action_Close.setShortcut(_translate("MainWindow", "Ctrl+X", None))
        self.action_File.setText(_translate("MainWindow", "&File", None))
        self.action_Object.setText(_translate("MainWindow", "&Object", None))
        self.action_Cut.setText(_translate("MainWindow", "&Cut", None))
        self.action_Paste.setText(_translate("MainWindow", "&Paste", None))
        self.action_Clear.setText(_translate("MainWindow", "&Clear", None))
        self.action_Clear.setToolTip(_translate("MainWindow", "Clear label", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

