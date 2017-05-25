#coding:utf-8
'worker testing'

import time, sys, queue

from multiprocessing.managers import BaseManager

#创建QueueManager extends BaseManager
class QueueManager(BaseManager):
    pass

#这个只是从网络上获取Queue，so register only provide name
QueueManager.register( 'get_task_queue' )
QueueManager.register( 'get_result_queue' )

#connect the service ,the machine which run the file task_master.py
server_addr = '172.16.2.168'
print( 'connect to server %s'%server_addr )

#Port and authkey must keep same with the mater server
manager = QueueManager( address = ( server_addr, 5000 ), authkey=b'abc' )
#connect from internet
manager.connect()

# get Queue's object

task = manager.get_task_queue()
result = manager.get_result_queue()

# get task from task-Queue, put the result into the result-Queue

for i in range(10):
    try:
        n = task.get(timeout =1 )
        print( 'run task %d*%d'% (n,n))
        r = '%d*%d = %d'%(n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print( 'task queue is empty.' )

#due the end
print( 'task is exit.' )


