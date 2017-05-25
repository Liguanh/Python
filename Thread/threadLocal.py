#coding:utf-8

'threadlocal test'

__author__='linguanghui'

import threading

#创建全局的ThreadLocal对像
local_school = threading.local()

def process_student():
    #获取当前线程关联的student
    std = local_school.student
    age = local_school.age

    print( 'Hello ,%s, you are %s, ( in %s ) '%( std,age, threading.current_thread().name ) )

def process_thread( student_name, age ):
    #绑定ThreadLocal的student
    local_school.student = student_name
    local_school.age = age
    process_student()

t1 = threading.Thread( target = process_thread,args = ( 'Alice','18' ), name='Thread-A' )
t2 = threading.Thread( target = process_thread,args = ( 'Bob','20' ), name='Thread-B' )

t1.start()
t2.start()
t1.join()
t2.join()

