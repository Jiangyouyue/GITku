#!python2
#coding=utf-8
import os
import sys

'''
text=[]
with open('forread.py', 'r') as f1,open('forwrite.py', 'w') as f2:
    for i in range(10):
        text.append(f1.readline())
        jon=''.join(text)
    print jon
    f2.write(jon)
'''
data=[]
startfile='menuexm'
startpath=os.path.join(os.getcwd(), startfile)
filelist1=os.listdir(startpath)
os.chdir(startpath)
for i in filelist1:
    with open(i, 'r') as f1:
        data.append(f1.read())

os.chdir(os.path.dirname(os.getcwd()))
endfile='firstfile'
endpath=os.path.join(os.getcwd(), endfile)
filelist2=os.listdir(endpath)
os.chdir(endpath)
#os.mkdir(endpath)
for i,value in enumerate(filelist2):
    with open(value, 'w') as f2:
        f2.write(data[i])
'''
for i in filelist:
    f=open(i,'a')
    f.close()
'''

#startpath=os.path.join(os.getcwd(), crefile)
#os.mkdir(startpath)
n='134'
z=int(n.zfill(5))
le=len("file")
print n,z,le,7
#os. chdir("路径")
