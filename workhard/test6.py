#!python2
#coding=utf-8
from PIL import  Image


fname='sys1.png'
n=8
# 1 打开文件, 返回一个文件对象;
im = Image.open(fname)

# 2. 获取已有图片的尺寸;
width, height = im.size

#3. 缩放图片50%
im.thumbnail((width/n, height/n))

# 4.把缩放的图片保存;
im.save('sys4.png', 'png')

