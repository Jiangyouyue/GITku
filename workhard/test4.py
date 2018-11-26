#!python2
#coding=utf-8

import math
import os
import sys
import cairo
from PyQt4 import QtGui,QtCore

####新定义的可触发鼠标动作的Label
class BtnLabel(QtGui.QLabel):  
    sig=QtCore.pyqtSignal()
    sig1=QtCore.pyqtSignal()
    def __init__(self,parent=None):  
        super(BtnLabel,self).__init__(parent)  
        self.if_mouse_press = 0
        self.setMouseTracking(True)
        self.xpos=0
        self.ypos=0
        self.xposmove=0
        self.yposmove=0
        self.staxpos=0
        self.stoxpos=0
        self.staypos=0
        self.stoypos=0
        self.xpossig=0
        self.ypossig=0
    def mouseMoveEvent(self,e):
        self.if_mouse_press = 1 
        if self.if_mouse_press:
            self.xpos=e.globalPos().x()-300
            self.ypos=e.globalPos().y()-324
            self.sig1.emit()
            #print 'move'
        print 2
        print ('mouse move:(%d,%d)\n'%(e.globalPos().x(),e.globalPos().y()))
    def mousePressEvent(self,e):  
        self.if_mouse_press = 1  
        self.staxpos=e.globalPos().x()-300
        self.staypos=e.globalPos().y()-300
        self.xpos=e.globalPos().x()-300
        self.ypos=e.globalPos().y()-324
        #self.sig1.emit()
        #self.xposmove=self.staxpos-self.stoxpos
        #self.yposmove=self.staypos-self.stoypos
        #self.sig.emit()
        print 1
        print ('mouse move:(%d,%d)\n'%(e.globalPos().x(),e.globalPos().y()))
        
    def mouseReleaseEvent(self,e): 
        self.if_mouse_press = 0
        self.stoxpos=e.globalPos().x()-300
        self.stoypos=e.globalPos().y()-300
        self.xposmove=self.stoxpos-self.staxpos
        self.yposmove=self.stoypos-self.staypos
        self.xpossig+=self.xposmove
        self.ypossig+=self.yposmove
        self.sig.emit()
        print 3,self.xpossig,self.ypossig,self.xposmove
        print ('mouse move:(%d,%d)\n'%(e.globalPos().x(),e.globalPos().y()))

####主要类窗口，QMainWindow类型
class Mainsys(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 550, 380)
        self.setWindowTitle('basesys')
        #self.textEdit = QtGui.QTextEdit()
        #self.setMouseTracking(True)
        self.syspic=['sys1.png','sys2.png','sys3.png','sys4.png']
        self.picnum=0
        self.defaultnum=[1,1,1,1]
        self.data1=[]
        self.xpos=0
        self.ypos=0
        self.picw=6000
        self.pich=3500
        self.tips=''
        #self.setCentralWidget(self.textEdit)
        self.statusBar()
        self.setFocus()
        self.setCentralWidget(self.layoutt())
        self.mainconnect()

        #菜单栏
        ope = QtGui.QAction(QtGui.QIcon('open.png'), u'打开', self)
        #ope.setShortcut('Ctrl+O')
        #ope.setStatusTip('Open new File')
        self.connect(ope, QtCore.SIGNAL('triggered()'), self.showDialog)

        clos=QtGui.QAction(QtGui.QIcon("ico.png"), u'关闭', self)
        self.connect(clos, QtCore.SIGNAL('triggered()'), self.close)

        sett=QtGui.QAction(QtGui.QIcon("ico.png"), u'配置', self)
        self.connect(sett, QtCore.SIGNAL('triggered()'), self.showDialog2)

        hel=QtGui.QAction(QtGui.QIcon("ico.png"), u'作者', self)
        self.connect(hel, QtCore.SIGNAL('triggered()'), self.showDialog3)
        #菜单
        menubar = self.menuBar()
        file = menubar.addMenu('&file')
        file.addAction(ope)
        file.addAction(clos)

        setting = menubar.addMenu('&setting')
        setting.addAction(sett)

        helpp =menubar.addMenu('&help')
        helpp.addAction(hel)

        #状态栏
        self.label_1=QtGui.QLabel(self)
        self.statuss=self.statusBar()
        self.statuss.addWidget(self.label_1)

    #所有部件的定义与布局
    def layoutt(self):
        self.mian_frame=QtGui.QWidget()
        self.litmap=BtnLabel(self.mian_frame) 
        self.lit1=QtGui.QPushButton(u'分析',self)
        self.lit2=QtGui.QPushButton(u'放大',self)
        self.lit3=QtGui.QPushButton(u'缩小',self)
        self.lit4=QtGui.QPushButton(u'缩放适合大小',self)
        self.lit5=QtGui.QPushButton(u'退出',self)
        ####400*300的显示框
        self.litpic=QtGui.QLabel(self.mian_frame)
        self.litpic.setPixmap(QtGui.QPixmap("blank1.png"))
        self.litpic.setGeometry(0,0,1000,20)
        self.litpic1=QtGui.QLabel(self.mian_frame)
        self.litpic1.setPixmap(QtGui.QPixmap("blank2.png"))
        self.litpic1.setGeometry(0,20,20,680)
        self.litpic2=QtGui.QLabel(self.mian_frame)
        self.litpic2.setPixmap(QtGui.QPixmap("blank3.png"))
        self.litpic2.setGeometry(20,320,980,380)
        self.litpic3=QtGui.QLabel(self.mian_frame)
        self.litpic3.setPixmap(QtGui.QPixmap("blank4.png"))
        self.litpic3.setGeometry(420,20,580,300)

        self.litche1=QtGui.QPushButton(u'覆盖情况',self)
        self.litche2=QtGui.QPushButton(u'下行最大速率',self)

        

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
        #hbox.addWidget(self.litmap)
        hbox.addLayout(vbox)
        
        #加载布局
        self.mian_frame.setLayout(hbox)
        return self.mian_frame
    #所有连接关系
    def mainconnect(self):
        self.lit1.clicked.connect(self.onClick1)     
        #接口button.clicked.connect(self.onClicked)
        self.lit2.clicked.connect(self.onClick2) 
        self.lit3.clicked.connect(self.onClick3) 
        self.lit4.clicked.connect(self.onClick4) 
        self.lit5.clicked.connect(self.onClick5) 
        self.litche1.clicked.connect(self.onClickche1)
        self.litche2.clicked.connect(self.onClickche2)
        

    ####所有响应函数
    def onClick1(self,evt):
        quit()
    #缩小按键响应
    def onClick3(self,evt):         #缩小
        if self.picnum<3 :
            self.picnum+=1
            self.picw=self.picw/2
            self.pich=self.pich/2
            self.litmap.setPixmap(QtGui.QPixmap(self.syspic[self.picnum]))
            print self.litmap.xpossig
            self.litmap.setGeometry(self.litmap.xpossig/2+110,self.litmap.ypossig/2+95,self.picw,self.pich)
            self.litmap.xposmove=0
            self.litmap.yposmove=0
            self.litmap.staxpos=0
            self.litmap.stoxpos=0
            self.litmap.staypos=0
            self.litmap.stoypos=0
            self.litmap.xpossig=self.litmap.xpossig/2+110
            self.litmap.ypossig=self.litmap.ypossig/2+95
        else : 
            print u'已达最小'
    #放大按键响应
    def onClick2(self,evt):         #放大
        if self.picnum >0 :
            self.picnum-=1
            self.picw=self.picw*2
            self.pich=self.pich*2
            self.litmap.setPixmap(QtGui.QPixmap(self.syspic[self.picnum]))
            self.litmap.setGeometry(self.litmap.xpossig*2-220,self.litmap.ypossig*2-190,self.picw,self.pich)
            self.litmap.xposmove=0
            self.litmap.yposmove=0
            self.litmap.staxpos=0
            self.litmap.stoxpos=0
            self.litmap.staypos=0
            self.litmap.stoypos=0
            self.litmap.xpossig=self.litmap.xpossig*2-220
            self.litmap.ypossig=self.litmap.ypossig*2-190
        else : 
            print u'已达最大'
    #
    def onClick4(self,evt):
        quit()
    def onClick5(self,evt):
        quit()
    def onClickche1(self,evt):
        quit()  
    def onClickche2(self,evt):
        quit()
    #地图拖动响应函数
    def onClickmap(self):
        self.litmap.setGeometry(self.litmap.xpossig,self.litmap.ypossig,self.picw,self.pich)
    #状态显示函数
    def Tips(self):   
        #self.tips='555'
        #return self.tips
        self.tips=u'横坐标为:%d,纵坐标为:%d,RSRP:%d,SINR:%d' \
        %(self.litmap.xpos-self.litmap.xpossig+440500,\
        self.litmap.ypos-self.litmap.ypossig+4427000,\
        0,0)
        self.label_1.setText(self.tips)
       

    ####菜单响应函数
    #打开文件并画图
    def showDialog(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file', './')
        '''file = open(filename)
        self.data = file.read()
        self.textEdit.setText(self.data)'''
        WIDTH=6000                #6000*3500
        HEIGHT=3500
        surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
        ctx = cairo.Context (surface)      
        ctx.set_source_rgb(0, 0, 0)     #RGB
        ctx.set_line_width(1); 
        
    #打开文件
        with open(filename) as f:
            data=[]
            #data1=[]
            #x=[]
            #y=[]
            for i in range(1627):          #1627
                s1=(f.readline())
                s1 = s1.rstrip('\n')
                data.append(s1.split('\t'))
                num=int(data[i][2])
                x=[]
                y=[]
                for j in range(num):
                    s2=(f.readline())
                    s2=s2.rstrip('\n')
                    d=s2.split('\t')
                    x.append(int((float(d[0])-440500)))
                    y.append(int((float(d[1])-4427000)))
                ctx.set_source_rgb(0, 0, 0)
                ctx.set_line_width(1)
                ctx.move_to(x[0],y[0])
                for k in range(num-1):
                    ctx.line_to(x[k+1],y[k+1])
                ctx.stroke() 
                print i 
            for i1 in range(25):          #1627
                ss=(f.readline())
                ss1=(f.readline())
                ss1 = ss1.rstrip('\n')
                ss1 = ss1.split('\t')
                x1=int((float(ss1[0])-440500))
                y1=int((float(ss1[1])-4427000))
                self.data1.append(ss1[2])
                ctx.set_source_rgb(1, 0, 0)
                ctx.set_line_width(4)
                ctx.arc(x1,y1,50,0,2*math.pi)
                ctx.stroke() 
            print i1,self.data1
            ctx.set_source_rgb(0, 0, 0)  
            ctx.rectangle(0,0,WIDTH,HEIGHT)
            ctx.stroke()
            surface.write_to_png (self.syspic[0])       
        self.litmap.setPixmap(QtGui.QPixmap(self.syspic[0]))
        self.litmap.setGeometry(0,0,self.picw,self.pich)
        self.litmap.sig.connect(self.onClickmap)
        self.litmap.sig1.connect(self.Tips)
    
    #配置对话框
    def showDialog2(self):
        dialog=QtGui.QDialog()         #创建QDialog对象
        btn=QtGui.QPushButton('save',dialog)      #创建按钮到新创建的dialog对象中
        btn.move(150,220)              #设置按钮位置
        dialog.connect(btn, QtCore.SIGNAL('clicked()'), self.addnum) #保存输入数据
        #创建4个输入框
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
        #取名
        dialog.setWindowTitle(u"配置")
        dialog.exec_()
    
    #获得配置参数
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


    #帮助对话框
    def showDialog3(self):
        dialog=QtGui.QDialog()
        a=QtGui.QLabel(dialog)
        a.setText(u'制作人：温翔楠   41524422')
        a.setGeometry(100,100,200,50)
        dialog.setWindowTitle(u"帮助")
        dialog.exec_()


        
app = QtGui.QApplication(sys.argv)
of = Mainsys()
of.show()
sys.exit(app.exec_())