#encoding=utf-8
import os
import sys

def run(**args):
	print "[*] In file_return module. "
	files = os.listdir(".")
	for i in range(0,len(files)):
		if files[i] not in sys.argv[0]:
            del files[i]
    print str(files)
	return str(files)

print sys.argv[0]
run()
