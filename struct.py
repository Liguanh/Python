#coding:utf-8

#list结构
print '/*---------------list结构------------------*/'
L =['guanghui','chunjie','jiangxue'];
print L
print L[0]
L.insert(1,'linxue')
print L
L.pop(2)
print L

print '\n/*------------tuple结构--------------------*/'


t = ('a','b','c','d')

print t

t=(1,)
print t

t = ('a','b',['x','y'])

L=t()
