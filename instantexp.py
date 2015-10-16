#-*- coding : utf-8 -*-
# 
# usage : run the expression which is in the clipboard and put result to clipboard
# 
# @author : becxer87
# @email : becxer87@gmail.com
#

from Tkinter import Tk
import sys
import os
import math
import random

#get encoding
enc = sys.getdefaultencoding()
print "default encoding : " + str(enc)

#get clipboard
root = Tk()
root.withdraw()
src = root.clipboard_get()
print str(type(src)) + " :",
print src

#ini file read
fname = "instantcode.ini"
try:
	ini_f = open(fname,"r")
except IOError as e:
	ini_f = open(fname,"w")
	ini_f.write("python")
	ini_f.close()
	ini_f = open(fname,"r")

lang = ini_f.read().strip()
ini_f.close()
interpreted = 'Error'
if lang == 'python':
	interpreted = eval(src)

print "result : " + str(interpreted)
root.clipboard_clear()
root.clipboard_append(interpreted)
root.destroy()
