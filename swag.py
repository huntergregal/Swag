#! /usr/bin python
##############################################
##	      	    SWAG		    ##
##	      Brought to you by  	    ##
##		Hunter Gregal		    ##
##############################################


import argparse
import time
import os

#################Define Functions##########################
def s():
	i=int(0)
	s=[" .----------------.","| .--------------. |","| |    _______   | |","| |   /  ___  |  | |",
		"| |  |  (__ \_|  | |","| |   '.___`-.   | |","| |  |`\____) |  | |",
		"| |  |_______.'  | |","| |              | |","| '--------------' |"," '----------------'"]
	while (i<=10):
		print(s[i])
		time.sleep(0.05)
		i=i+1
def w():
	i=int(0)
	w=["         .----------------.","        | .--------------. |","        | | _____  _____ | |","        | ||_   _||_   _|| |",
	"        | |  | | /\ | |  | |","        | |  | |/  \| |  | |","        | |  |   /\   |  | |","        | |  |__/  \__|  | |",
	"        | |              | |","        | '--------------' |","         '----------------'"]
        while (i<=10):
                print(w[i])
                time.sleep(0.05)
                i=i+1
def a():
	i=int(0)
	a=["                 .----------------.","                | .--------------. |","                | |      __      | |","                | |     /  \     | |",
	"                | |    / /\ \    | |","                | |   / ____ \   | |","                | | _/ /    \ \_ | |","                | ||____|  |____|| |",
	"                | |              | |","                | '--------------' |","                 '----------------'"]
        while (i<=10):
                print(a[i])
                time.sleep(0.05)
                i=i+1
def g():
	i=int(0)
	g=["                         .----------------.","                        | .--------------. |","                        | |    ______    | |",
	"                        | |  .' ___  |   | |","                        | | / .'   \_|   | |","                        | | | |    ____  | |",
	"                        | | \ `.___]  _| | |","                        | |  `._____.'   | |","                        | |              | |",
	"                        | '--------------' |","                         '----------------'",]
        while (i<=10):
                print(g[i])
                time.sleep(0.05)
                i=i+1
def swagB():
	swagBlocks="""
	.----------------.  .----------------.  .----------------.  .----------------. 
	| .--------------. || .--------------. || .--------------. || .--------------. |
	| |    _______   | || | _____  _____ | || |      __      | || |    ______    | |
	| |   /  ___  |  | || ||_   _||_   _|| || |     /  \     | || |  .' ___  |   | |
	| |  |  (__ \_|  | || |  | | /\ | |  | || |    / /\ \    | || | / .'   \_|   | |
	| |   '.___`-.   | || |  | |/  \| |  | || |   / ____ \   | || | | |    ____  | |
	| |  |`\____) |  | || |  |   /\   |  | || | _/ /    \ \_ | || | \ `.___]  _| | |
	| |  |_______.'  | || |  |__/  \__|  | || ||____|  |____|| || |  `._____.'   | |
	| |              | || |              | || |              | || |              | |
	| '--------------' || '--------------' || '--------------' || '--------------' |
	 '----------------'  '----------------'  '----------------'  '----------------' """
	i=int(0)
	while (i<=2):
		os.system('clear')
		print(swagBlocks)
		time.sleep(0.5)
		os.system('clear')
		time.sleep(0.5)
		i=i+1
def swag3D():
	swag3D=r"""
	          _____                    _____                    _____                    _____
	         /\    \                  /\    \                  /\    \                  /\    \
	        /::\    \                /::\____\                /::\    \                /::\    \
	       /::::\    \              /:::/    /               /::::\    \              /::::\    \
	      /::::::\    \            /:::/   _/___            /::::::\    \            /::::::\    \
	     /:::/\:::\    \          /:::/   /\    \          /:::/\:::\    \          /:::/\:::\    \
	    /:::/__\:::\    \        /:::/   /::\____\        /:::/__\:::\    \        /:::/  \:::\    \
	    \:::\   \:::\    \      /:::/   /:::/    /       /::::\   \:::\    \      /:::/    \:::\    \
	  ___\:::\   \:::\    \    /:::/   /:::/   _/___    /::::::\   \:::\    \    /:::/    / \:::\    \
	 /\   \:::\   \:::\    \  /:::/___/:::/   /\    \  /:::/\:::\   \:::\    \  /:::/    /   \:::\ ___\
	/::\   \:::\   \:::\____\|:::|   /:::/   /::\____\/:::/  \:::\   \:::\____\/:::/____/  ___\:::|    |
	\:::\   \:::\   \::/    /|:::|__/:::/   /:::/    /\::/    \:::\  /:::/    /\:::\    \ /\  /:::|____|
	 \:::\   \:::\   \/____/  \:::\/:::/   /:::/    /  \/____/ \:::\/:::/    /  \:::\    /::\ \::/    /
	  \:::\   \:::\    \       \::::::/   /:::/    /            \::::::/    /    \:::\   \:::\ \/____/
	   \:::\   \:::\____\       \::::/___/:::/    /              \::::/    /      \:::\   \:::\____\
	    \:::\  /:::/    /        \:::\__/:::/    /               /:::/    /        \:::\  /:::/    /
	     \:::\/:::/    /          \::::::::/    /               /:::/    /          \:::\/:::/    /
	      \::::::/    /            \::::::/    /               /:::/    /            \::::::/    /
	       \::::/    /              \::::/    /               /:::/    /              \::::/    /
	        \::/    /                \::/____/                \::/    /                \::/____/
	         \/____/                  ~~                       \/____/"""
	print(swag3D)

###########Arguemnts##############
parser=argparse.ArgumentParser(description='Initiates Swag (Use with Screen or Tmux to always be swagged out)')
parser.add_argument('-s', '--scroll', help='(Optional) An endless scroll of swag.',action='store_true', required=False)
parser.add_argument('-b', '--blink', help='(Optional) Ever blinking swag on your screen.',action='store_true', required=False)
parser.add_argument('-d', '--dimensional', help='(Optional) A 3D swag banner to accompany your work.',action='store_true', required=False)
parser.add_argument('-l', '--loop', help='(Optional) A continuous loop of all the swag',action='store_true', required=False)
args = parser.parse_args()
########Script Start#########i
if (args.scroll):
	os.system('clear')
	while (args.scroll):
		s()
		w()
		a()
		g()
if (args.blink):
	while (args.blink):
		swagB()
if (args.dimensional):
	os.system('clear')
	swag3D()
	time.sleep(999999)
if (args.loop):
	while (args.loop):
		os.system('clear')
		s()
		w()
		a()
		g()
		swagB()
		swag3D()
	
else:
	os.system('clear')
	s()
	w()
	a()
	g()
	swagB()
	swag3D()


##########################################
