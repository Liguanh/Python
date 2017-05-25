#coding:utf-8


print '--------dict数据类型-----------'

dict ={
        'Adam':95,
        'Lisa':80,
        'Bart':70
   }
print 'Adam:',dict.get('Adam')
print 'Lisa:',dict.get('Lisa')
print 'Paul:',dict.get('Paul')

for (key,val) in dict.items():

    print("%s:%s"%(key,val))


#dict的几个特点：1、查找速度快，无论多少元素查找元素速度都是一样的
#  2、存储的key-value是没有顺序的  3、key元素必须是不可变的

print '-------set-------------------------'

s = set(['A','B','C','C'])
print s
print len(s)

#set的特点  1、不存储value值，存储的值是不变的、存储的元素是没有顺序的

months = set(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul','Aug','Sep','Oct','Nov','Dec'])

x1 = 'Feb'
x2 = 'Sun'

if x1 in months:
    print 'x1:ok'
else:
    print 'x1:error'

if x2 in months:
    print 'x2:ok'
else:u
    print 'x2:error'



