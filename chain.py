#coding:utf-8

'设置链接的信息'

__author__ = 'linguanghui'

class Chain( object ):

    def __init__( self , path = '' ):

        self._path = path

    def __getattr__( self, path ):

        return Chain( '%s/%s' %( self._path, path ) )

    def __str__( self ):
        return self._path

    __repr__ = __str__

c = Chain( 'http://api.server' )
print( c.user.friends)

class Book( object ):

    def __init__( self, name ):

        self._name = name

    def __call__( self ):

        print( 'My name is %s.'% self._name )

B = Book( 'March' )

B()
print( callable( B ) )
