import os


text=[]
with open('forread.py', 'r') as f:
    for i in range(5):
        text.append(f.readline())
        jon=''.join(text)
    print jon