#coding:utf-8
#匿名函数lambda
L = map(lambda x: pow(x,2),[1,3,5,7,9])
print(L)

L1 = reduce(lambda x,y: x*y,[1,3,5])
print L1

f = lambda x: pow(x,3)
print f(5)

def fn(x):
    return lambda : x*x

fa = fn(5)
print fa()

print fa.__name__

