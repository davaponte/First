#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello.ui'
#
# Created: Mon Jul  8 08:03:21 2013
#      by: PyQt4 UI code generator 4.10
#
# Usar
#   pyside-uic -x hello.ui -o hello.py
# en lugar de
#   pyuic4 -x hello.py -o hello.py
# para que se use PySide

Ok, esto es una modificación!


import hello
import sys
#from PyQt4 import QtCore, QtGui
from PySide import QtCore, QtGui

class MyForm(QtGui.QDialog, hello.Ui_Form):
    def __init__(self, parent = None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
#        self.setStyle(QtGui.QStyleFactory.create("Motif"))
#        self.setPalette(QtGui.QApplication.style().standardPalette())

    def backtraceCall(self):
        QtGui.QMessageBox.information(self, 'INFO', 'Doing something...\nInside the instanced class!')

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    #app.setStyle(QtGui.QStyleFactory.create('Motif'))
    #app.setStyle(QtGui.QStyleFactory.create('Windows'))
    #app.setStyle(QtGui.QStyleFactory.create('CDE'))
    #app.setStyle(QtGui.QStyleFactory.create('Plastique'))
    #app.setStyle(QtGui.QStyleFactory.create('GTK+'))     ###DEFAULT
    #app.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
    #app.setPalette(QtGui.QApplication.style().standardPalette())

    form  = MyForm()
    form.show()
    #app.exec_()
    sys.exit(app.exec_())


