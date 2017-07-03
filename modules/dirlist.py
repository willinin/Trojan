import os

def run(**args):
	print "[*] In dirlister module. "
	cdir=os.getcwd()
	#os.chdir("D:\\")
	files = os.listdir(".")
	for i in range(0,len(files)):
		files[i]=cdir+files[i]
	return str(files)
