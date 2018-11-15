#!python2
#coding=utf-8

import random
import cairo
import math
import copy

#初始化矩阵squa
squa=[
[1,1,1,1,1,9],
[1,1,1,1,1,9],
[1,1,1,1,1,9],
[1,1,1,1,1,9],
[9,9,9,9,9,9]
]
plateshow=[]
plate=[]                                #plate用于储存生成图
xypos=[                                 #坐标序号
[0,0],[0,1],[0,2],[0,3],[0,4],
[1,0],[1,1],[1,2],[1,3],[1,4],
[2,0],[2,1],[2,2],[2,3],[2,4],
[3,0],[3,1],[3,2],[3,3],[3,4]
]
times=0                                 #生成图数量参数


#检查在矩阵L（xpos，ypos，x，y）范围内是否为空
def check(xpos,ypos,x,y,L):             
    emp=1
    for i in range(x):
        if emp==0:
            break
        for j in range(y):
            if L[i+xpos][j+ypos]==1  :
                pass
            else :
                emp=0
                break
    return emp                          #emp取值为0（被占用）或1（空）
##定义4种类
class ACLA(object): 
    def __init__(self):
        self.len=2
        self.wid=2
        self.num=2
class BCLA(object):
    def __init__(self):
        self.len=2
        self.wid=1
        self.num=3
class CCLA(object):
    def __init__(self):
        self.len=1
        self.wid=2
        self.num=4
class DCLA(object):
    def __init__(self):
        self.len=1
        self.wid=1
        self.num=5

#对矩阵squa内容进行替换
def change(xpos,ypos,squa,cla,xypos):
    empty=check(xpos,ypos,cla.len,cla.wid,squa)
    if empty==1:
        for i in  range(cla.len):
            for j in range(cla.wid):
                squa[i+xpos][j+ypos]= cla.num
                if [i+xpos,j+ypos] in xypos:
                    xypos.remove([i+xpos,j+ypos])
        return 1
    else :
        return 0
def cover(squa,plate):
    h=1
    for i in plate:
        if i==squa:
            h=0
            break
    return   h
def copyy(squacopy,squa):
    for i in  range(4):
        for j in range(5):
            squacopy[i][j]= squa[i][j]
    

asqu=ACLA()                                  #生成4个对象
bsqu=BCLA()
csqu=CCLA()
dsqu=DCLA()

#主要运行函数，多个for循环对矩阵历遍，
def run(plate,squa,asqu,bsqu,csqu,dsqu,xypos):
    for xpos,ypos in xypos:
        squa=[
        [1,1,1,1,1,9],
        [1,1,1,1,1,9],
        [1,1,1,1,1,9],
        [1,1,1,1,1,9],
        [9,9,9,9,9,9]
        ]
        xypos11=copy.deepcopy(xypos)
        rep=change(xpos,ypos,squa,asqu,xypos11)
        #plate.append(squa5)
        if rep==1:
            global squa10
            squa10=copy.deepcopy(squa)
            xypos10=copy.deepcopy(xypos11)
            for xpos10,ypos10 in xypos11:
                copyy(squa,squa10)
                rep=change(xpos10,ypos10,squa,bsqu,xypos10)
                if rep==1:
                    global squa9
                    squa9=copy.deepcopy(squa)
                    xypos9=copy.deepcopy(xypos10)
                    for xpos9,ypos9 in xypos10:
                        copyy(squa,squa9)
                        rep=change(xpos9,ypos9,squa,bsqu,xypos9)
                        if rep==1:
                            global squa8
                            squa8=copy.deepcopy(squa)
                            xypos8=copy.deepcopy(xypos9)
                            for xpos8,ypos8 in xypos9:
                                copyy(squa,squa8)
                                rep=change(xpos8,ypos8,squa,bsqu,xypos8)
                                if rep==1:
                                    global squa7
                                    squa7=copy.deepcopy(squa)
                                    xypos7=copy.deepcopy(xypos8)
                                    for xpos7,ypos7 in xypos8:
                                        copyy(squa,squa7)
                                        rep=change(xpos7,ypos7,squa,bsqu,xypos7)
                                        if rep==1:
                                            global squa6
                                            squa6=copy.deepcopy(squa)
                                            xypos6=copy.deepcopy(xypos7)
                                            for xpos6,ypos6 in xypos7:
                                                copyy(squa,squa6)
                                                rep=change(xpos6,ypos6,squa,csqu,xypos6)
                                                if rep==1:
                                                    global squa5
                                                    squa5=copy.deepcopy(squa)
                                                    xypos5=copy.deepcopy(xypos6)
                                                    for xpos5,ypos5 in xypos6:
                                                        copyy(squa,squa5)
                                                        rep=change(xpos5,ypos5,squa,dsqu,xypos5)
                                                        if rep==1:
                                                            global squa4
                                                            squa4=copy.deepcopy(squa)
                                                            xypos4=copy.deepcopy(xypos5)
                                                            for xpos4,ypos4 in xypos5:
                                                                copyy(squa,squa4)
                                                                rep=change(xpos4,ypos4,squa,dsqu,xypos4)
                                                                if rep==1:
                                                                    global squa3
                                                                    squa3=copy.deepcopy(squa)
                                                                    xypos3=copy.deepcopy(xypos4)
                                                                    for xpos3,ypos3 in xypos4:
                                                                        copyy(squa,squa3)
                                                                        rep=change(xpos3,ypos3,squa,dsqu,xypos3)
                                                                        if rep==1:
                                                                            global squa2
                                                                            squa2=copy.deepcopy(squa)
                                                                            xypos2=copy.deepcopy(xypos3)
                                                                            for xpos2,ypos2 in xypos3:
                                                                                copyy(squa,squa2)
                                                                                rep=change(xpos2,ypos2,squa,dsqu,xypos2)
                                                                                if rep==1:
                                                                                    global squa1
                                                                                    squa1=copy.deepcopy(squa)
                                                                                    xypos=copy.deepcopy(xypos)
                                                                                    notclu=cover(squa1,plate)                 #notclu表示新生成矩阵是否不存在，默认为1                            
                                                                                    if notclu==1:             
                                                                                        plate.append(squa1)    #将新矩阵添加到plate
                                                                                        global times
                                                                                        times+=1 
                                                                                        print times
                                                                                        copyy(squa,squa2)
                                                                                else :
                                                                                    squa=copy.deepcopy(squa2)                                                                           
                                            
                                                                        else :
                                                                            squa=copy.deepcopy(squa3)
                                                                            
                                                                else :
                                                                    squa=copy.deepcopy(squa4)
                                                                  
                                                        else :
                                                            squa=copy.deepcopy(squa5)
                                                         
                                                else :
                                                    squa=copy.deepcopy(squa6)
                                                  
                                        else :
                                            squa=copy.deepcopy(squa7)
                                            
                                else :
                                    squa=copy.deepcopy(squa8)

                        else :
                            squa=copy.deepcopy(squa9)
                else :
                    squa=copy.deepcopy(squa10)
        else :
            squa=[
            [1,1,1,1,1,9],
            [1,1,1,1,1,9],
            [1,1,1,1,1,9],
            [1,1,1,1,1,9],
            [9,9,9,9,9,9]
            ]
run(plate,squa,asqu,bsqu,csqu,dsqu,xypos)            #运行主函数   
for value1 in plate :              #输出plate
    for j,value2 in enumerate(value1) :
        print (j,value2) 
    print ''
times=times*24*24
a="可能的分配方式数量为："
print (a.decode("utf-8").encode("gbk")),times   #输出数量times



