#! /usr/bin python
##############################################
##	      	    SWAG		    ##
##	      Brought to you by  	    ##
##		Hunter Gregal		    ##
##############################################



import time
import os

os.system('clear')

s = open('s.txt')
i=0
while (i<=11):
	print(s.readline())
	time.sleep(0.05)
	i=i+1
s.close()


w = open('w.txt')
i=0
while (i<=11):
        print(w.readline())
        time.sleep(0.05)
        i=i+1
w.close()	


a = open('a.txt')
i=0
while (i<=11):
        print(a.readline())
        time.sleep(0.05)
        i=i+1
a.close()


g = open('g.txt')
i=0
while (i<=11):
        print(g.readline())
        time.sleep(0.05)
        i=i+1
g.close()

##Clear##
os.system('clear')

i=0
while (i<=2):
	swagblock = open('swagblock.txt')
	print(swagblock.read())
	time.sleep(0.5)
	os.system('clear')
	time.sleep(0.5)
	swagblock.close()
	i=i+1
##clear##
os.system('clear')

swag3D = open('swag3D.txt')
print(swag3D.read())
swag3D.close()
