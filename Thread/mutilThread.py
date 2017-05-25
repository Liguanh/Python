#coding:utf-8

'thread testing '

import time, threading

#新循环的线程执行

def Loop( ):
    print( 'thread %s is running '% threading.current_thread().name )
    n = 0

    while n < 5:
        n  = n +1
        print( 'thread %s >>> %s '%( threading.current_thread().name, n ) )

        time.sleep( 1 )
    print( 'thread %s ended:'% threading.current_thread().name )

print( 'thread %s is running' % threading.current_thread().name )

t = threading.Thread( target = Loop, name =' LoopThread' )

t.start()
t.join()

print( 'threading %s ended:' % threading.current_thread().name )
