#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_

import types
from types import MethodType

'a test Class Model'
__author__='linguanghui'

class Dog( object ):

    def __init__( self, heavy, color ):
        self.heavy  = heavy
        self.color  = color

    def run( self ):
        print( 'The Dog color %s is running '%( self.color ))

dog  = Dog( 20, 'white' )
dog.run()

def eat( self ):
    print( 'the dog is %s Kg, it is eat more also'%( self.heavy ))

#给实例绑定外部函数
dog.eat = MethodType( eat, dog )
dog.eat()
#给类绑定外部函数
Dog.eat = eat
dog1 = Dog( 10, 'black' )

dog1.eat()

#__slots__变量用来限制实例的属性 ,只对当前的类其作用，对子类是不起作用的

class Car( object ):

    __slots__ = ( 'cost', 'power','name' )

    def __init__( self, cost, power, name ):
        self.cost   = cost
        self.power  = power
        self.name   = name

    def introduce_car( self ):
        print( 'the car is %s, power %s, Cost %s ten thousands $'%( self.name, self.power, self.cost ))

car = Car( '13.5', '1.6', 'All new Ford' )

car.introduce_car( )

class SmallCar( Car ):

    def colors( self, color ):

        print( 'the car is %s'%( color ) )

smallCar = SmallCar( '13.5', '1.6', 'All new Ford' )

smallCar.colors('white' )
