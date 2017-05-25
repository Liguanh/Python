#coding:utf-8

import time, threading

#余额默认为0
balance = 0

def change_balance( n ):
    global balance
    balance = balance + n
    balance = balance - n

lock = threading.Lock()
def run_thread( n ):
    for n in range(10000):
        #获取🔒
        lock.acquire()
        try:
            change_balance( n )
        finally:
            #释放锁
            lock.release()

t1 = threading.Thread( target = run_thread, args = ( 5, ) )
t2 = threading.Thread( target = run_thread, args = ( 9, ) )

t1.start()
t2.start()

t1.join()
t2.join()

print( balance )

