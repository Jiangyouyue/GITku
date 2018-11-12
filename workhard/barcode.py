#!python2
#coding=utf-8

import random
import cairo
dict_lcode = {
 0: "0001101",
 1: "0011001",
 2: "0010011",
 3: "0111101",
 4: "0100011",
 5: "0110001",
 6: "0101111",
 7: "0111011",
 8: "0110111",
 9: "0001011"
}
dict_rcode = {
 0: "1110010",
 1: "1100110",
 2: "1101100",
 3: "1000010",
 4: "1011100",
 5: "1001110",
 6: "1010000",
 7: "1000100",
 8: "1001000",
 9: "1110100"
}
WIDTH, HEIGHT = 600, 300
Width_per_code = 10
Height_per_code = 200

def Numcre():             #获得随机生成的N位数字
    num=[]
    lnum=[]
    rnum=[]
    for i in range(12):
        num.append(random.randint(0,9))
    check1 = 3 * sum(num[1::2]) + sum(num[::2])
    check2 = 10 - check1 % 10
    if check2 == 10:
        check2 = 0
    num.append(check2)
    for i in range(1,7):
        lnum.append(num[i])
    for i in range(7,13):
        rnum.append(num[i])
    return lnum,rnum
def Lcodecre(num):             #左边数字转义函数
    code=''
    for i in range(len(num)):
        code+=dict_lcode[num[i]]
    return code
def Rcodecre(num):              #右边数字转义函数
    code=''
    for i in range(len(num)):
        code+=dict_rcode[num[i]]
    return code   
class Drawcode(object):     #画图父类
    def __init__(self,width,height):
        self.width=width
        self.height=height
    
    def draw(self):
        lnum,rnum=Numcre()
        lcode=Lcodecre(lnum)
        rcode=Rcodecre(rnum)
        code=lcode+rcode
        surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, self.width, self.height)
        ctx = cairo.Context (surface)
        ctx.translate(50,50)
        ctx.set_source_rgb(0, 0, 0)
        for i,c in enumerate(code):
            xpos = Width_per_code *i
            if c=='1' :
                ctx.rectangle(xpos,0,Width_per_code,Height_per_code)
                ctx.fill()
        surface.write_to_png("%s.png" %code)

test=Drawcode(600,300)
test.draw()





    