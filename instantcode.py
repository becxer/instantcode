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
import time
import threading

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
eslib = { \
'python' : u'''
#-*- coding=utf-8 -*-
import sys
import os
import math
import random
''',\
'node' : u'''
var fs = require('fs')
''',\
'ruby' : u'''
'''\
}

src_fname = "instantcode.src"
interpreted = 'Error'
if lang in eslib.keys():
	src_f = codecs.open(src_fname,"w", "utf-8")
	src_f.write(eslib[lang])
	src_f.write(src)
	src_f.close()
	interpreted = run_cmd(lang + ' ' + src_fname).decode(enc)
elif lang == 'win-cpp' or lang == 'win-c' :
	win_fname = src_fname + '.'+lang.split('-')[1]
	src_f = codecs.open(win_fname,'w','utf-8')
	src_f.write(src)
	src_f.close()
	print run_cmd('vcvars32 & cl ' + win_fname)
	interpreted = run_cmd(src_fname+'.exe').decode(enc)
elif lang == 'c' or lang == 'cpp':
	compiler = {'c' : 'gcc' , 'cpp' : 'g++'}
	gcc_fname = src_fname + '.'+lang
	src_f = codecs.open(gcc_fname,'w','utf-8')
	src_f.write(src)
	src_f.close()
	print run_cmd(compiler[lang]+' -o instance.src.o ' + gcc_fname)
	interpreted = run_cmd('./instance.src.o').decode(enc)
	
#put result to clipboard
print "______________________________________________"
print interpreted
root.clipboard_clear()
root.clipboard_append(interpreted)

#to escape Tkinter's mainloop
def exit_after(sec):
	for i in xrange(0,sec):
		print "exit() after " + str(sec - i) + " sec"
		time.sleep(1)
	os._exit(5)

# MAC OS has to be wait until clipboard is used (I don't know why..)
from sys import platform as _platform
if _platform == "darwin":
# MAC OS X
	root.update()
	th = threading.Thread(target=exit_after,args=(5,))
	th.start()
	root.mainloop()
root.destroy()	

