import getpass



#安全方式获得密码
user = getpass.getuser()
passwd = getpass.getpass('your password: ')
print(user, passwd)