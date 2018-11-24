#!python2
#coding=utf-8

import os
import sys
from PyQt4 import QtGui,QtCore

class OpenFile(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('basesys')
        self.textEdit = QtGui.QTextEdit()
        self.painter=QtGui.QPainter()
        self.setCentralWidget(self.painter)
        self.statusBar()
        self.setFocus()
        
        exit = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        exit.setShortcut('Ctrl+O')
        exit.setStatusTip('Open new File')
        self.connect(exit, QtCore.SIGNAL('triggered()'), self.paintEvent)
        
        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        file.addAction(exit)
        
    def showDialog(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file', './')
        file = open(filename)
        data = file.read()
        self.textEdit.setText(data)

    def paintEvent(self,event):
        self.painter.begin(self)
        #自定义绘制方法
        self.drawText(event,painter)
        self.painter.end()

    def drawText(self,event,qp):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file', './')
        file = open(filename)
        data = file.read()
        #设置画笔的颜色
        qp.setPen(QColor(168,34,3))
        #设置字体
        qp.setFont(QFont('SimSun',20))
        #绘制文字
        qp.drawText(event.rect(),Qt.AlignCenter,self.text)
        
app = QtGui.QApplication(sys.argv)
of = OpenFile()
of.show()
sys.exit(app.exec_())
