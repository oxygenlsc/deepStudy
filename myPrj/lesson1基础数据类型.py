# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:54:48 2021

@author: oxygen
"""
'''
# 程序的格式架构
# python语言采用严格的缩进来表明程序的格式框架
# 缩进指每一行代码开始前的空白区域，用来表示代码之间的包含和层次关系。
# 1个缩进（tab）= 4个空格（Space）
# 这个是唯一的方法
# spyder的ctrl加e是注释
'''
flag = False
name = 'lsc'
if name == 'python':
    flag = True
    print('hello')
    
else:
    print(name)
    
'''
标识符命名
Python语言允许采用大写字母,小写字母,数字下划线和汉字等字符命名但是
汉字不要用,就和js命名差不多

True False 大写开头布尔值 None
'''

#内置函数type
#
type(1)#int
type(False)#bool
type(None)#None是一个特殊的常量和False不同 不0 不是空字符串  NoneType是他的类型

'''
#内置函数help help可以查询细节
# 内置函数 pow(2,10)  代表2的10次方
#内置函数id()可以查询每一个对象的内存地址,即身份
内置函数hex()转16进制
oct()八进制
bin()二进制
'''

'''
数据的基本类型
数字 布尔  NoneType  组合数据类型
                        |
                  序列  集合   字典
                    |
           字符串  元组  列表
'''

'''
数字类型
1 整数类型  就是整数每一个具体的取值范围
2 浮点数类型 就是带小数点的呗
3 复数类型 4+3j  j是-1开庚号
'''
'''
python 中 除法/是会有整数和小数的  //是取整 %取余 **次方  abs()绝对值
round(x,保留多少位)四舍五入
max(x1,x2)取最大值
min(x1,x2)最小值
'''

'''
3种类型的转换

int(4.5)直接去掉小数部分
int('15',16)转成16进制
float(4) = 4.0 增加小数
complex(3) = (3+0j)
'''

'''
'abc' = ['a','b','c']
'''

'''
赋值语句可以多个给

a,b,c = 1,2,3
'''





