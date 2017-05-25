#coding:utf-8

' a testing for my class define by myself'

__author__ = 'linguanghui'

import types
# 定制类的学习
class Animale ( object ):

    def __init__( self , type ):

        self.type = type

    def __str__( self ):
        return 'Animale object (type is %s):'%(self.type)
    __repr__  = __str__

    def __getattr__( self, attr ):
        if attr == 'color':
            return  'white'
        raise AttributeError( 'Animale Object has no attribution %s'%attr)

a = Animale( 'dog' )
print( a )
print( a.color )

class Fib( object ):
    def __init__( self ):
        self.a, self.b = 0, 1

    def __iter__( self ):
        return self

    def __next__( self ):
        self.a, self.b = self.b, self.a + self.b

        if self.a > 100000:
            raise StopIteration()
        return self.a


for n in Fib():
    print( n )

class Fib_Slice( object ):
    def __getitem__( self, n ):
        a, b = 1, 1
        if isinstance( n , int ): # n是整数
            for x in range( n ):
                a, b = b, a + b

            return a

        if isinstance( n, slice ): #是切片
            start = n.start
            stop  = n.stop
            step  = n.step
            if start is None:
                start = 0;
            if step is None:
                step = None

            L = []
            for x in range( stop ):
                if x >= start:
                    L.append( a )
                a, b = b, a+b

            if step != None :
                L = L[::step]
            return L

f = Fib_Slice()
print( "###############" )
print( f[2:5] )

print( f[2:10:2] )


