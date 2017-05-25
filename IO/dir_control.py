#coding:utf-8

__author__ = 'linguanghui'

import os
import shutil

print( os.name )
print( '###########################')
print( os.uname() )
print( '###########################')
print( os.environ )
print( os.environ.get('USER') )
print( os.environ.get('USER1', 'lgh189491' ) )

print( '###########################')

print( os.path.abspath( '.' ) )

print( '###########################')

#os.path.join( './', 'test' )

#os.mkdir( './test' )

print( '###########################')

print( os.path.split( './test.txt' ) )
print( os.path.splitext( './test.txt' ) )

print( '###########################')

#shutil.copyfile( 'test1.txt', 'test2.txt' )

list = [ x for x in os.listdir( '.' ) if os.path.isdir( x ) ]

print( list )

filelist =  [ x for x in os.listdir( '.' ) if os.path.isfile( x ) and os.path.splitext( x )[1] =='.py' ]

print( filelist )
