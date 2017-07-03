#encoding=utf-8
import os
import sys

def run(**args):
	print "[*] In file_return module. "
	files = os.listdir(".")
	for i in range(0,len(files)):
		if files[i] not in sys.argv[0]:
			if os.path.isdir(files[i])==False:
				fp=open(files[i],'rb+')
				ans=fp.read()
				fp.close()
	return str(ans)
