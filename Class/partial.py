#coding:utf-8
import functools

#转换二进制
int2 = functools.partial(int,base =2)
print  int2('100000')

max2 = functools.partial(max,10)
print max2(5,7,9)
print max2(11,15,16)
