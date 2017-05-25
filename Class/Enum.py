#coding:utf-8

'test enum'

__author__ = 'linguanghui'

from enum import Enum,unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print( name,'=>',member,',',member.value)

@unique
class Weekday( Enum ):
    Sun = 0
    Mon = 1
    Tue = 2
    Wen = 3
    Thu = 4
    Fri = 5
    Sta = 6


for name, member in Weekday.__members__.items():
    print( name,'=>',member.value )


class Hello( object ):

    def hello( self , name ):
        print( 'my name is %s '%name )

h = Hello()
h.hello( 'linguangui' )
print( type(Hello) )

print( type(h) )
