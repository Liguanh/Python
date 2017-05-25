#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_

import types

'a test Class Model'
__author__='linguanghui'

print __doc__

class Students(object):
    name = 'bob'
    def __init__(self, name, age):
        self.name = name
        self.age  = age
        self.__score = 100
    def tests(self):
        return ('My name is %s,I\'m %s years old!'%(self.name,self.age))

    #获取分数
    def get_score(self):
        return self.__score
    def set_score(self, score):
        if 0<= score <= 100:
            self.__score = score
        else:
            return 'bad Score set !'


    def get_grade(self):
        if self.age >= 90:
            return 'very old'
        elif self.age >= 60:
            return 'old'
        else:
            return 'young'

def fn():
    return 'i love you'

Bart = Students('林光辉', 25)
Bart.score = 80
print Bart._Students__score

Bart.set_score(120)

print Bart.get_score()

#判断数据类型
print isinstance( Bart, Students )
print( type( Bart ) )
print type( abs )

print hasattr( Bart, 'name' )

print hasattr( Bart, 'hobbies');

setattr( Bart, 'hobbies', 'coding' )

print hasattr( Bart, 'hobbies' )

print getattr( Bart, 'hobbaies', 404 )

print type( fn ) == types.FunctionType

print type( abs ) == types.BuiltinFunctionType

print dir( abs)

print .name
