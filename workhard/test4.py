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

        clos=QtGui.QAction(QtGui.QIcon("ico.png"), u'关闭', self)
        self.connect(clos, QtCore.SIGNAL('triggered()'), self.close)

        sett=QtGui.QAction(QtGui.QIcon("ico.png"), u'配置', self)
        self.connect(sett, QtCore.SIGNAL('triggered()'), self.showDialog2)

        hel=QtGui.QAction(QtGui.QIcon("ico.png"), u'作者', self)
        self.connect(hel, QtCore.SIGNAL('triggered()'), self.showDialog3)

        menubar = self.menuBar()
        file = menubar.addMenu('&file')
        file.addAction(ope)
        file.addAction(clos)

        setting = menubar.addMenu('&setting')
        setting.addAction(sett)

        helpp =menubar.addMenu('&help')
        helpp.addAction(hel)



        self.lit1=QtGui.QPushButton(u'分析',self)
        #self.lit1.setGeometry(300,50,50,30)
        self.lit1.clicked.connect(self.onClick1)
        self.lit2=QtGui.QPushButton(u'放大',self)
        self.lit3=QtGui.QPushButton(u'缩小',self)
        self.lit4=QtGui.QPushButton(u'缩放适合大小',self)
        self.lit5=QtGui.QPushButton(u'退出',self)
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch()
        vbox.addWidget(self.lit2)
        vbox.addWidget(self.lit3)
        vbox.addWidget(self.lit4)
        vbox.addWidget(self.lit5)

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch()
        hbox.addLayout(vbox)
        

        
    def onClick1(self,evt):
        quit()

    def showDialog(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file', './')
        file = open(filename)
        data = file.read()
        self.textEdit.setText(data)

    def showDialog2(self):
        dialog=QtGui.QDialog()         #创建QDialog对象
        btn=QtGui.QPushButton('ok',dialog)      #创建按钮到新创建的dialog对象中
        btn.move(150,220)              #移动按钮，设置dialog的标题
        dialog.connect(btn, QtCore.SIGNAL('clicked()'), dialog.close)
        b=[u'热噪声:',u'带宽:',u'频率:',u'RSRP门限:']
        d=['dBm/Hz','Hz','MHz','dBm']
        for i in range(4):
            b1=QtGui.QLabel(dialog)
            b1.setText(b[i])
            b1.setGeometry(50,50+i*40,60,30)            
            d1=QtGui.QLabel(dialog)
            d1.setText(d[i])
            d1.setGeometry(210,50+i*40,60,30)
            c1= QtGui.QLineEdit(dialog)
            c1.setGeometry(110,50+i*40,80,25)
        dialog.setWindowTitle(u"配置")
        dialog.exec_()

    def showDialog3(self):
        dialog=QtGui.QDialog()
        a=QtGui.QLabel(dialog)
        a.setText(u'制作人：温翔楠   41524422')
        a.setGeometry(100,100,200,50)
        dialog.setWindowTitle(u"帮助")
        dialog.exec_()


        
app = QtGui.QApplication(sys.argv)
of = OpenFile()
of.show()
sys.exit(app.exec_())