import configparser



#解析cnf文件
cf = configparser.ConfigParser(allow_no_value=True)
cf.read('my.cnf')