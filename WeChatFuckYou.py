#!/usr/bin/python

import zipfile
def extractFile(file,password):
	try:
		file.extractall(pwd=password.encode("ascii"))
		print("发现密码",password)
		return password
	except:
		return
def main():
	file=zipfile.ZipFile("1.zip") #文件名字
	f=open("data.txt") #密码字典
	for line in f.readlines():
		password=line.strip("\n")
		result=extractFile(file,password)
		if result==None:
			continue
		else:
			f.close()
			return
if __name__=="__main__":
	main()