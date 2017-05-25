#coding:utf-8

'a test portery Model programme'

__author__ = 'linguanghui'

import types

#property  作为python内置的一种装饰器，负责把一个方法作为属性来调用的

class Students( object ):

    @property
    def score( self ):
        return self._score

    @score.setter
    def score( self, value ):
        if not isinstance( value, int ):
            raise ValueError( 'score must be a interger' )

        if value <0 or value >100:
            raise ValueError( 'score must be in 0~100' )

        self._score = value

    @property
    def avage_age( self ):
        return self._score / 2



s = Students()

s.score = 60

print s.score



#添加一个Screen对像加一个width和height属性，以及只读属性resolution

class Screen( object ):

    @property
    def width( self ):
        return self._width

    @width.setter
    def width( self, value ):
        self._width = value

    @property
    def height( self ):
        return self._height

    @height.setter
    def height( self, value ):
        self._height = value

    @property
    def resolution( self ):
        return self._height*self._width

screen = Screen( )

screen.width = 100
screen.height = 100

print( '高：%s, 宽: %s, 面积: %s'%( screen.height, screen.width, screen.resolution ) )

