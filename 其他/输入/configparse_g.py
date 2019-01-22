from configparser import ConfigParser



#解析cnf文件
cf = configparser.ConfigParser(allow_no_value=True)
cf.read('my.cnf')

#查看区域和选项
cf.options('section') #返回列表
cf.get("section", 'opt')

#设置选项的值
cf.set("section", 'opt', "value")
cf["section"][opt] = "value" #一样的作用

#写入配置文件
with open("test.txt", "wt") as f:
    cf.write(f)
