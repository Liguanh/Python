#coding:utf8

print '--------------list追加元素-------------------'
#list 追加元素
L = ['Adam', 'Lisa', 'Bart','Pual']
L.append('Paul')
print L


print '---------------从list中删除元素－－-----------'
#从list删除元素

L = ['Adam', 'Lisa', 'Bart','Pual']
L.pop(2)
L.pop(2)
print L


print '---------------list元素替换-------------------'

#list替换
L = ['Adam', 'Lisa', 'Bart','Pual']
L[0] = 'Pual'
L[3] = 'Adam'

print L


print '----------------tuple有序列表------------------'

#tuple 是另一种有序的列表，中文翻译为“ 元组 ”。tuple 和 list 非常类似，但是，tuple一旦创建完毕，就不能修改了。

t = ('Adam', 'Lisa', 'Bart')

print t[0]



print '-----------------if else 条件语句------------------'

#python if else 条件语句
score=75
if score>=90:
    print 'prefect'
elif score>=80:
    print 'good'
elif score>=60:
    print 'nice'
else:
    print 'No,you must harry up!'


print '-----------------python for 循环----------------'

#pyhton for循环

L=[10,20,30,40,50]
len = len(L)
sum = 0.0
for val in L:
    sum = sum + val
print sum/len



print '---------------------python while循环---------------------------'

#pyhton while 循环

sum = 0

n = 1;
while n<=100:
    sum = sum + n
    n += 2
print sum



print '---------------------python break 退出循环----------------------'

sum = 0
num = 1
n   = 1

while True:
    if n > 20:
        break
    sum += num
    num *= 2
    n   += 1
print sum


print '---------------------'

print '-------------------python continue ----------------------'

sum =0
x=0
while True:
    x=x+1
    if x>100:
        break
    if x%2 == 0:
        continue
    sum = sum + x
print sum
