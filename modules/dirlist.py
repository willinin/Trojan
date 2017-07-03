import os

def run(**args):

	print "[*] In dirlister module. "
	cdir=os.getcwd()
	files = os.listdir(".")
    for i in range(len(files)):
		files[i]=cdir+files[i]
	return str(files)
