#coding:utf-8
'test mutilprocess'

__author__='linguanghui'

from multiprocessing import Process
import os
print( 'Process ( %s ) is starting ....' %os.getpid() )

#Only work unix/Linux/Mac
pid = os.fork()

#父进程返回子进程id子进程返回0
if pid == 0:
    print( 'I am child process ( %s ) and my parent process process is %s.' % ( os.getpid(), os.getppid() ) )
else:
    print( 'I ( %s ) just created a child process ( %s ) ' %( os.getpid(), pid ) )

def run_proc(name):
    print( 'Run child process %s ( %s ) .....'%( name, os.getpid() ) )

if __name__=='__main__':
    print( 'Parent Process is %s ' % os.getpid() )
    p = Process( target= run_proc, args = ('test',) )
    print( 'child process will start ' )
    p.start()
    p.join()
    print( 'child process will end' )
