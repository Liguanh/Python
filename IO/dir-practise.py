#coding:utf-8

import os

def list_dir( ):
    currentDir = [ x for x in os.listdir( './' ) ]

    dirStr = ''

    if currentDir:
        for name in currentDir:
            dirStr += name+'\n'

    return dirStr;

print( list_dir() )

print( '###########################')


