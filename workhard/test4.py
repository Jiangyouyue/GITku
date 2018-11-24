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
        self.setCentralWidget(self.layoutt())
        self.defaultnum=[1,1,1,1]
        #self.setCentralWidget(self.textEdit)
        self.statusBar()
        self.setFocus()

        ope = QtGui.QAction(QtGui.QIcon('open.png'), u'打开', self)
        #ope.setShortcut('Ctrl+O')
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


    def layoutt(self):
        self.lit1=QtGui.QPushButton(u'分析',self)
        self.lit2=QtGui.QPushButton(u'放大',self)
        self.lit3=QtGui.QPushButton(u'缩小',self)
        self.lit4=QtGui.QPushButton(u'缩放适合大小',self)
        self.lit5=QtGui.QPushButton(u'退出',self)
        self.litmap=QtGui.QLabel(self)
        self.litmap.setPixmap(QtGui.QPixmap("hello8.png"))
        self.litche1=QtGui.QPushButton(u'覆盖情况',self)
        self.litche2=QtGui.QPushButton(u'下行最大速率',self)

        self.lit1.clicked.connect(self.onClick1)     
        #接口button.clicked.connect(self.onClicked)
        self.lit2.clicked.connect(self.onClick2) 
        self.lit3.clicked.connect(self.onClick3) 
        self.lit4.clicked.connect(self.onClick4) 
        self.lit5.clicked.connect(self.onClick5) 
        self.litche1.clicked.connect(self.onClickche1)
        self.litche2.clicked.connect(self.onClickche2)   

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch()
        vbox.addWidget(self.litche1)
        vbox.addWidget(self.litche2)
        vbox.addWidget(self.lit1)
        vbox.addWidget(self.lit2)
        vbox.addWidget(self.lit3)
        vbox.addWidget(self.lit4)
        vbox.addWidget(self.lit5)

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.litmap)
        hbox.addLayout(vbox)
        main_frame=QtGui.QWidget()
        #加载布局
        main_frame.setLayout(hbox)
        return main_frame


    def onClick1(self,evt):
        quit()
    def onClick2(self,evt):
        quit()
    def onClick3(self,evt):
        quit()
    def onClick4(self,evt):
        quit()
    def onClick5(self,evt):
        quit()
    def onClickche1(self,evt):
        quit()  
    def onClickche2(self,evt):
        quit()


    def showDialog(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file', './')
        file = open(filename)
        self.data = file.read()
        self.textEdit.setText(self.data)

    def showDialog2(self):
        dialog=QtGui.QDialog()         #创建QDialog对象
        btn=QtGui.QPushButton('save',dialog)      #创建按钮到新创建的dialog对象中
        btn.move(150,220)              #移动按钮，设置dialog的标题
        dialog.connect(btn, QtCore.SIGNAL('clicked()'), self.addnum)
        b=[u'热噪声:',u'带宽:',u'频率:',u'RSRP门限:']
        d=['dBm/Hz','Hz','MHz','dBm']
        for i in range(4):
            b1=QtGui.QLabel(dialog)
            b1.setText(b[i])
            b1.setGeometry(50,50+i*40,60,30)            
            d1=QtGui.QLabel(dialog)
            d1.setText(d[i])
            d1.setGeometry(210,50+i*40,60,30)
        self.c1= QtGui.QLineEdit(dialog)
        self.c1.setGeometry(110,50+0*40,80,25)
        self.c2= QtGui.QLineEdit(dialog)
        self.c2.setGeometry(110,50+1*40,80,25)
        self.c3= QtGui.QLineEdit(dialog)
        self.c3.setGeometry(110,50+2*40,80,25)
        self.c4= QtGui.QLineEdit(dialog)
        self.c4.setGeometry(110,50+3*40,80,25)
        dialog.setWindowTitle(u"配置")
        dialog.exec_()

    def addnum(self):
        num1=self.c1.text()
        num2=self.c2.text()
        num3=self.c3.text()
        num4=self.c4.text()
        self.defaultnum[0]=int(num1)
        self.defaultnum[1]=int(num2)
        self.defaultnum[2]=int(num3)
        self.defaultnum[3]=int(num4)
        #print self.defaultnum,num1



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