#-*- coding : utf-8 -*-
# 
# usage : run the code which is in the clipboard and put result to clipboard
# 
# @author : becxer87
# @email : becxer87@gmail.com
#
from Tkinter import Tk
import sys
import os
import subprocess
import codecs

#get encoding
reload(sys)
sys.setdefaultencoding('utf-8')
enc = sys.getdefaultencoding()
print "default encoding : " + str(enc)

#get clipboard & parse encode
root = Tk()
root.withdraw()
src = root.clipboard_get()
if type(src).__name__ != 'unicode':
        src = src.decode(enc)
print "______________________________________________"
print src
print "______________________________________________"

#run command in shell
def run_cmd(bashCmd):
	print "run command : " + str(bashCmd)
	process = subprocess.Popen(bashCmd, shell=True 
				,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	res = ''
	while True:
		output = process.stdout.readline()
		if output == '' and process.poll() is not None:
			break
		if output:
			res += output
		rc = process.poll()
	output, error = process.communicate()
        res += error
	return res

#ini file read
ini_fname = "instantcode.ini"
try:
	ini_f = open(ini_fname,"r")
except IOError as e:
	ini_f = open(ini_fname,"w")
	ini_f.write("python")
	ini_f.close()
	ini_f = open(ini_fname,"r")
lang = ini_f.read().strip()
ini_f.close()

#write source to tmp file & interpret source file
essential_pylib = u'''
#-*- coding=utf-8 -*-
import sys
import os
import math
import random
'''
src_fname = "instantcode.src"
interpreted = 'Error'
if lang == 'python':
        src_f = codecs.open(src_fname,"w","utf-8")
        src_f.write(essential_pylib)
        src_f.write(src)
        src_f.close()
        interpreted = run_cmd('python ' + src_fname).decode(enc)
elif lang == 'win-cpp' or lang == 'win-c' :
	win_fname = src_fname + '.'+lang.split('-')[1]
	src_f = codecs.open(win_fname,'w','utf-8')
	src_f.write(src)
	src_f.close()
	print run_cmd('vcvars32 & cl ' + win_fname)
	interpreted = run_cmd(src_fname+'.exe').decode(enc)
	
#put result to clipboard
print "______________________________________________"
print interpreted
root.clipboard_clear()
root.clipboard_append(interpreted)
root.destroy()
