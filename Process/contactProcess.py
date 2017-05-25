#coding:utf-8

'contact process'

from multiprocessing import Process, Queue

import os, time, random

#写进程方法
def write( q ):
    print( 'Processs %s to write .....' % os.getpid() )

    for value in [ 'A', 'B', 'C' ]:
        print( 'process %s to queue...'% value )
        q.put( value )
        time.sleep( random.random() )

#读进程方法
def read( q ):
    print( 'Process %s to read .....' % os.getpid() )

    while True:
        value  = q.get( True )
        print ( 'get %s from queue ....' % value )

if __name__=='__main__':
    #父进程创建队列，传给子进程
    q = Queue()

    qw = Process( target = write, args=( q, ) )
    qr = Process( target = read, args=( q, ) )

#启动子进程写入
    qw.start()
#启动子进程 读取
    qr.start()
#等待pw进程结束
    qw.join()
#读进程是死循环强制推出
    qr.terminate()
