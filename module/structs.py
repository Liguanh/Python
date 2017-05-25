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

L=t[2]

L[0]='M'
L[1]='N'

print t

print '------------可变得python------------------------\n'

t = ('a','b',['a','b'])
l=t[2]
s=(l[0],l[1])
t=('a','b',s)
print t

print '-----------if else --------------------------\n'

score = 75
if score >= 90:
    print 'percent'
elif score >= 80:
    print 'good'
elif score >=70:
    print 'fine'
else:
    print 'faild'

print '---------foreach循环-----------------------------\n'

L=[75,92,59,68]

sum = 0.0

for name in L:
    sum = sum + name

print sum/4

print '---------------while循环--------------------------\n'

#循环100以内奇数的和

sum = 0
n=1

while(n<=100):
    sum =sum + n
    n +=2

print sum

print '-----while break-----------------------\n'

n=0
sum = 0
x=1
while True:
    if n>20:
        break
    sum=sum + x
    x=x*2
    n=n+1
print sum

print '---------while continue------------'

sum = 0
n = 0

while True:
    n = n + 1
    if n>100:
        break
    if n % 2 ==0:
        continue
    sum = sum + n
print sum

print '----------for 多重循环-------------------'

x = ['A','B','C']
y = ['1','2','3']

for m in x:
    for n in y:
      print m+n

#找出来所有十位数比个位数大的两位数
for a in ['1','2','3','4','5','6','7','8','9']:
        for b in ['1','2','3','4','5','6','7','8','9']:
            if a>=b:
                continue
            print a+b


