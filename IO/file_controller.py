#coding:utf-8

'testing file-do'

__author__ = 'linguanghui'

from io import StringIO

with open( 'test.txt', 'w' ) as fw:
    fw.write('hello python !')

with open( './test.txt', 'r' ) as f:
    for list in f.readlines():
        print( list.strip() )

f = StringIO()

f.write('hello')
f.write(' ')
f.write('world!')

print( f.getvalue() )

f1 = StringIO( 'Hello!\nHi!\nYeah!')

s = f1.readline()
for str in s:
    print( str.strip() )
