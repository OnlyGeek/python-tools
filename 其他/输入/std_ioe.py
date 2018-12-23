import sys


#打印标准流中的文件
#python std_ioe.py < /etc/passwd
for line in sys.stdin:
	print(line, end="")