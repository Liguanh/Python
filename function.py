#coding:utf-8
import math
print '--------函数的的使用------------'

#sum求1到N的平方的和
L = []
n=0
while n < 100:
    n = n + 1
    L.append(n**2)
print sum(L)

L = []
n = 1
while n <= 100:
    L.append(n**2)
    n = n + 1
print sum(L)

#自定义函数

def square_of_sum(L):
    List = []
    for name in L:
        List.append(name**2)
    return sum(List)

print square_of_sum([1,5,7,8,9,10])

#一元二次方程的函数

def quadratic_equation(a,b,c):

    t = b**2 - 4*a*c
    if t < 0:
        return
    else:
        x1 = (-b + math.sqrt(t))/(2*a)
        x2 = (-b - math.sqrt(t))/(2*a)

    return x1,x2

print quadratic_equation(1,-6,5)


#汉诺塔的移动

def hnt_move(n,a,b,c):

    if n ==1:
        print(a+'-->'+c)
    else:
        hnt_move(n-1,a,c,b)
        print(a+'-->'+c)
        hnt_move(n-1,b,a,c)

hnt_move(4,'A','B','C')


#接收可变参数的函数求平均值

def average(*args):

    if args:
        return sum(args)*1.0/len(args)
    else:
        return 0.0

print average()
print average(1,2,3)
print average(1,3,5,7,9)
