import tarfile
with tarfile.open('test.tar') as t:
	for member_info in t.getmembers():
		print(member_info.name)


#归档文件，添加文件
with tarfile.open('test1.tar', 'w') as out:
	out.add("k8s")
	
#读取gzip压缩的文件
with open('test1.tar', mode='r:gz') as out:

#创建一个用bzip2的压缩文件包
with open('test1.tar.bz2', mode='w:bz2') as out:


#实例 备份指定文件到压缩包中
#!/usr/bin/python
#-*- coding:UTF-8 -*-
import os
import fnmatch
import tarfile
import datetime



def find_specific_files(root, patterns=['*'], exclude_dirs=[]):
	pass
def main():
	#选择需要打包的文件类型
	patterns= ['*.jpg']
	now=datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
	filename = "all_images_{0}.tar.gz".format(now)
	with tarfile.open(filename, 'w:gz') as f:
		for item in find_specific_files(".", patterns):
			f.add(item)
			
if __name__ == '__main__':
	main()