#!python2
#coding=utf-8

import os
import sys
import cairo
from PyQt4 import QtGui,QtCore

class OpenFile(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('basesys')
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        self.setFocus()
        
        ope = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        ope.setShortcut('Ctrl+O')
        ope.setStatusTip('Open new File')
        self.connect(ope, QtCore.SIGNAL('triggered()'), self.showDialog)
        clos=QtGui.QAction(QtGui.QIcon("ico.png"), u"关闭", self)
        self.connect(clos, QtCore.SIGNAL('triggered()'), self.close)

        menubar = self.menuBar()
        file = menubar.addMenu('&file')
        file.addAction(ope)
        file.addAction(clos)
        setting = menubar.addMenu('&setting')
        setting.addAction(clos)

    def showDialog(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file', './')
        file = open(filename)
        data = file.read()
        self.textEdit.setText(data)
        
app = QtGui.QApplication(sys.argv)
of = OpenFile()
of.show()
sys.exit(app.exec_())