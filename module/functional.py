#coding:utf-8
import math
import time
import functools

#python把函数作为参数
def sqrt(a):
    return pow(a, 0.5)

def add(x, y, f):
    return f(x) + f(y)

print add(25,9, sqrt)

#python中的map函数 接受一个函数和一个list 通过函数作用在list的每个元素上，得到一个新的list返回

def format_name(l):
    return l[0].upper()+l[1:].lower()
print map(format_name, ['adam', 'LISA', 'barT'])

#python中的高阶函数reduce,对list的每个元素反复调用传入的函数

def prod(x,y):
    return x*y

print reduce(prod,[1,3,5,7]);

#filter函数
def is_sqr(x):
    return pow(x,0.5)%1 == 0;
print filter(is_sqr, range(1, 101))

#sorted函数排序

def reversed_cmp(x,y):
    if x > y:
        return -1;
    if x < y:
        return 1;
    return 0;

print sorted([36,22,1,14,78],reversed_cmp)

#python中返回函数  匿名函数lambda   lambda 参数: 函数内容 返回函数可以把一些计算延迟

def calc_prod(lst):
    def lazy_reduce():
        return reduce((lambda x,y:x*y), lst)
    return lazy_reduce

f = calc_prod([1,2,3,4])
print f();

#pthon 中的闭包 呢层函数引用外层函数的变量，然后返回内层函数的情况

def count():
    fs = []
    for i in range(1,4):
        def prod(n = i):
            return pow(n,2)
        fs.append(prod)

    return fs
f1,f2,f3 = count()
print  f1(),f2(),f3()

#python 中的匿名函数

print filter(lambda s: s and len(s.strip())>0, ['test', None, '', 'str','End']);


