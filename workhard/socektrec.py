#!python2
#coding=utf-8


import socket

HOST = '10.18.142.42'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('hello,server')
data = s.recv(1024)
s.close()
print 'Received', data

