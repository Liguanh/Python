#coding:utf-8

'test service process'

__author__='linguanghui'

import random, time, queue

from multiprocessing.managers import BaseManager

#发送任务的队列
task_queue = queue.Queue()
#接收结果的队列
result_queue = queue.Queue()

#从BaseManager继承的QueueManger的类

class QueueManager ( BaseManager ):
    pass

#把两个队列注册到网络上, callable 关联到Queue的对象
QueueManager.register( 'get_task_queue', callable= lambda:task_queue )
QueueManager.register( 'get_result_queue', callable= lambda:result_queue )

#绑定端口5000，设置验证码abc
manager = QueueManager( address = ('', 5000), authkey=b'abc' )

#启动Queueu
manager.start()

#获得通过网络访问的queue的对象
task = manager.get_task_queue()
result = manager.get_result_queue()

#put some task in it

for i in range( 10 ):
    n = random.randint( 0,10000 )
    print( 'Put task %d ....' %n )
    task.put( n )

#get content from task queue
print( 'try get results....' )

for i in range( 10 ):
    r = result.get( timeout = 10 )
    print( 'Result %s' % r )

#关闭
manager.shutdown()
print('master exit')
