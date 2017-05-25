#coding:utf-8

'test dubug coding'

__author__='linguanghui'

import logging
import pdb
logging.basicConfig( level=logging.INFO )

def foo ( n ):

    n = int( n )

    logging.info( 'n = %s ' % n )
    return 10 / n

def main( ):
    foo( '0' )

main()

s = '0'

n = int( s )

print( 10 / n )
