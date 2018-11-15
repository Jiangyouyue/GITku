
'''print "为什么："
print "1"

a="中文"
print(a.decode("utf-8").encode("gbk"))'''
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
def change(xpos,ypos,squa,cla):
    empty=check(xpos,ypos,cla.len,cla.wid,squa)
    if empty==1:
        for i in  range(cla.len):
            for j in range(cla.wid):
                squa[i+xpos][j+ypos]= cla.num
        return 1
    else :
        return 0


asqu=ACLA()                                  #生成4个对象
bsqu=BCLA()
csqu=CCLA()
dsqu=DCLA()

#主要运行函数，多个for循环对矩阵历遍，
def run(plate,squa,asqu,bsqu,csqu,dsqu):
    for xpos,ypos in xypos:
        rep=change(xpos,ypos,squa,asqu)
        if rep==1:
            rep=0
            bsq=0
            for xpos,ypos in xypos:
                rep=change(xpos,ypos,squa,bsqu)
                if bsq==4:
                    break
                if rep==1:
                    bsq+=1
            if rep==1:
                for xpos,ypos in xypos:
                    rep=change(xpos,ypos,squa,csqu)
                    if rep==1:
                        rep=0
                        dsq=0
                        for xpos,ypos in xypos:
                            rep=change(xpos,ypos,squa,dsqu)
                            if dsq==4:
                                break
                            if rep==1:
                                dsq+=1
                                return
                        if rep==1:
                            global squa1
                            squa1=squa
                            notclu=1                  #notclu表示新生成矩阵是否不存在，默认为1                               
                            for allplate in plate:
                                if allplate==squa1:
                                    notclu=0
                                    break
                            if notclu==1:             
                                plate.append(squa1)    #将新矩阵添加到plate里
                                global times
                                times+=1 
                                squa=[                 #重新初始化squa 
                                [1,1,1,1,1,9],
                                [1,1,1,1,1,9],
                                [1,1,1,1,1,9],
                                [1,1,1,1,1,9],
                                [9,9,9,9,9,9]
                                ]
                            else :
                                squa=[
                                [1,1,1,1,1,9],
                                [1,1,1,1,1,9],
                                [1,1,1,1,1,9],
                                [1,1,1,1,1,9],
                                [9,9,9,9,9,9]
                                ] 
run(plate,squa,asqu,bsqu,csqu,dsqu)            #运行主函数   
for value1 in plate :              #输出plate
    for j,value2 in enumerate(value1) :
        print (j,value2) 
    print ''
times=times*24*24
a="可能的分配方式数量为："
print (a.decode("utf-8").encode("gbk")),times   #输出数量times