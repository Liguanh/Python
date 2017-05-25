#coding:utf-8
import time
import functools

#python的装饰器 简化代码，避免重复的调用
def new_fn(f):
    def fn(x):
        print 'call'+ f.__name__+'()'
        return f(x)
    return fn;
# @new_fn 相当图f1=new_fn(f1)
@new_fn
def f1(x):
    return x*2;
print f1(5);

#python中编写无参数的decorator  *args **kw 可以用任意参数
print '#####decorator'
def log(func):
    def wapper(*args,**kw):
        t = time.ctime()
        print('call function %s() in %s' % (func.__name__,t))
        return func(*args,**kw)
    return wapper
@log
def plus(x, y):
    print x+y
print plus(10,5)

print plus.__name__

#python 中编写有参数的装饰器
print '''###############################'''
def performance(unit):
    def performance_decorater(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            print('call %s() in %s'%(f.__name__, unit))
            return f(*args, **kw)
        return wrapper
    return performance_decorater

@performance('ms')
def puls(x,y):
    return x+y
print puls(10,5)
print plus.__name__



##experice  test
print('####################练习题####################')
def logs(func):
    def wrapper(*args, **kw):
        print('begin call %s()'%(func.__name__))
        result = func(*args, **kw)
        print('end call %s()'%(func.__name__))
        return result
    return wrapper

def logs1(text):
    def decorator(func):
        @functools.wraps(func):
            def wrapper(*args, **kw):
                print('%s begin call%s()'%(text,func.__name__))
                result = func(*args,**kw)
                print('%s begin call%s()'%(text,func.__name__))
                return result
            return wrapper
        if isinstance(text,str):
            return decorator
        else:
            note = text
            text =''
            return decorator(note)

@logs1
def test(x, y):
    return x*y

print test(5,6)


