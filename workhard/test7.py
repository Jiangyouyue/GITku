#!python2
#coding=utf-8

import os
import sys
import cairo
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class WindowDemo(QWidget):  
    def __init__(self,parent=None):
        super(WindowDemo,self).__init__(parent)
        self.b1 = QLabel(self)
        self.b2 = QLabel(self)
        self.b2.setPixmap(QPixmap("hello8.png"))
        self.b2.setGeometry(0,50,400,400)

        self.btn = QPushButton('Press me')
        self.btn.setGeometry(250,450,100,50)
        self.setWindowTitle("Inside PyQt ex3")
        self.b2.linkHovered.connect(self.tips)
    def tips(self):
        print 1

if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    win = WindowDemo()  
    win.show()  
    sys.exit(app.exec_())


    #!python2
#coding=utf-8
from PIL import  Image


fname='sys1.png'
lis=[[2,2],[3,4],[4,8]]
for i,n in lis:
    im = Image.open(fname)
    width, height = im.size
    im.thumbnail((width/n, height/n))
    im.save('sys%d.png'%i, 'png')