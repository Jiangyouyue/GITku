#!python2
#coding=utf-8

import random
import cairo
import math
import copy


squa=[
[1,1,1,1,1,9],
[1,1,1,1,1,9],
[1,1,1,1,1,9],
[1,1,1,1,1,9],
[9,9,9,9,9,9]
]
plate=[]
xypos=[
[0,0],[0,1],[0,2],[0,3],[0,4],
[1,0],[1,1],[1,2],[1,3],[1,4],
[2,0],[2,1],[2,2],[2,3],[2,4],
[3,0],[3,1],[3,2],[3,3],[3,4]
]
times=0

def check(xpos,ypos,x,y,L):
    emp=1
    for i in range(x):
        if emp==0:
            break
        for j in range(y):
            if L[i+xpos][j+ypos]==1 :
                pass
            else :
                emp=0
                break
    return emp
class ACLA(object):
    def __init__(self):
        self.len=2
        self.wid=2
        self.num=2
class BCLA(object):
    def __init__(self):
        self.len=1
        self.wid=2
        self.num=3
class CCLA(object):
    def __init__(self):
        self.len=2
        self.wid=1
        self.num=4
class DCLA(object):
    def __init__(self):
        self.len=1
        self.wid=1
        self.num=5
'''empty=check(0,0,5,4,squa)
print "empty=",empty'''
def change(xpos,ypos,squa,cla):
    empty=check(xpos,ypos,cla.wid,cla.len,squa)
    if empty==1:
        for i in  range(cla.len):
            for j in range(cla.wid):
                squa[i+xpos][j+ypos]= cla.num
        return 1
    else :
        return 0
asqu=ACLA()
bsqu=BCLA()
csqu=CCLA()
dsqu=DCLA()
def run(plate,squa,asqu,bsqu,csqu,dsqu):
    for xpos,ypos in xypos:
        rep=change(xpos,ypos,squa,asqu)
        if rep==1:
            for i in range(4):
                for xpos,ypos in xypos:
                    rep=change(xpos,ypos,squa,bsqu)
                    if rep==1:
                        for xpos,ypos in xypos:
                            rep=change(xpos,ypos,squa,csqu)
                            if rep==1:
                                for j in range(4):
                                    for xpos,ypos in xypos:
                                        rep=change(xpos,ypos,squa,dsqu)
                                        if rep==1:
                                            global squa1
                                            squa1=squa
                                            notclu=1                                           
                                            for allplate in plate:
                                                if allplate==squa1:
                                                    notclu=0
                                                    break
                                            if notclu==1:
                                                plate.append(squa1)
                                                global times
                                                times+=1 
                                                squa=[
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
run(plate,squa,asqu,bsqu,csqu,dsqu)             
for i,value in enumerate(plate) : 
    print(i,value) 
a="可能的分配方式数量为："
print (a.decode("utf-8").encode("gbk")),times



