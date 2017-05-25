#coding:utf-8

'pickle study'

__author__='linguanghui'

import os
import pickle

d = dict( name = 'Bob', age = 20, score = 88 )

print( pickle.dumps( d ) )

f = open( './dump.txt', 'wb')

pickle.dump( d, f )

f.close()

fr = open( './dump.txt', 'rb' )

dr = pickle.load( fr )

f.close()

print( dr )

os.remove( './dump.txt' );
