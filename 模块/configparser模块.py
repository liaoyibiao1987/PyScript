#读取配置方法
#-read(filename) 直接读取ini文件内容
#-sections() 得到所有的section，并以列表的形式返回
#-options(section) 得到该section的所有option
#-items(section) 得到该section的所有键值对
#-get(section,option) 得到section中option的值，返回为string类型
#-getint(section,option) 得到section中option的值，返回为int类型
#写入配置方法
#-add_section(section) 添加一个新的section
#-set( section, option, value) 对section中的option进行设置

import configparser
#生成config对象
config = configparser.ConfigParser()
#用config对象读取配置文件
config.read('test_con')
#以列表形式返回所有的section
sections = config.sections()
print('sections',sections)
#得到指定section的所有option
options = config.options("liuyao")
print('options',options)
#得到指定section的所有键值对
kvs = config.items("liuyao")
print('kvs',kvs)
#指定section，option读取值
str_val = config.get("liuyao", "card")
int_val = config.getint("liuyao", "limit")
print('liuyao 的 card',str_val)
print('liuyao 的 limit',int_val)
#修改写入配置文件
#更新指定section，option的值
config.set("mayun", "limit", "32764889")
int_val = config.getint("mayun", "limit")
print('mayun 的 limit',int_val)
#写入指定section增加新option和值
config.set("liuyao", "age", "99999")
int_val = config.getint("liuyao", "age")
print('liuyao 的 age',int_val)
#增加新的section
if config.get('duobian',"age") == "" :
    config.add_section('duobian')
    config.set('duobian', 'age', '41555')
#写回配置文件
config.write(open("test_con",'w'))