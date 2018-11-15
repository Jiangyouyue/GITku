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
squacopp=[
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
def change(xpos,ypos,squa,cla):
    empty=check(xpos,ypos,cla.len,cla.wid,squa)
    if empty==1:
        for i in  range(cla.len):
            for j in range(cla.wid):
                squa[i+xpos][j+ypos]= cla.num
        return 1
    else :
        return 0
def cover(squa,plate,xypos):
    h=1
    for i in plate:
        if h==0 :
            break
        for j,m in xypos:
            if i[j][m]==squa[j][m]:
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


containall=[dsqu,dsqu,dsqu,dsqu,csqu,bsqu,bsqu,bsqu,bsqu,asqu]
allname=[squacopp,squacopp,squacopp,squacopp,squacopp,squacopp,squacopp,squacopp,squacopp,squacopp,squacopp]
def cycle(i,plate,squa,containall,allname):
    i-=1
    if i<1:
        for xpos,ypos in xypos:
            rep=change(xpos,ypos,squa,containall[i])
            if rep==1:
                allname[i]=copy.deepcopy(squa)
                notclu=1                 #notclu表示新生成矩阵是否不存在，默认为1                            
                if notclu==1:             
                    plate.append(allname[i])    #将新矩阵添加到plate里
                    global times
                    times+=1 
                    print times
                    squa=copy.deepcopy(allname[i+1])
                else :
                    squa=copy.deepcopy(allname[i+1])
                  
    else:
        for xpos,ypos in xypos:
            coppy(allname[i+1],squa) 
            rep=change(xpos,ypos,squa,containall[i])
            #plate.append(squa5)
            if rep==1:
                #global allname[i]
                allname[i]=copy.deepcopy(squa)        
                cycle(i,plate,squa,containall,allname)
            else :
                squa=copy.deepcopy(allname[i+1])
    return times
times=cycle(10,plate,squa,containall,allname)
a="可能的分配方式数量为："
print (a.decode("utf-8").encode("gbk")),times   #输出数量times