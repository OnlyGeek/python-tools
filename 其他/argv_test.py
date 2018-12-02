import sys
import os



#打印出参数---列表
#print(sys.argv)
#例子从命令行获取参数，验证文件是否可以打开
#python argv_test.py test.txt
def main():
	sys.argv.append("")
	filename = sys.argv[1]
	if not os.path.isfile(filename):
		raise SystemExit(filename + ' does not exists')
	elif not os.access(filename, os.R_OK):
		raise SystemExit(filename + ' is not accessible')
	else:
		print(filename + ' is accessible')
		
if __name__ == '__main__':
	main()