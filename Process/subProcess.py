#coding:utf-8

'subProcess testing'

__author__='linguanghui'

import subprocess
from multiprocessing import Process, Queue
import os, time, random

print( 'Process git:(master) ✗ ls ./' )

r = subprocess.call( ['ls', './'] )

print( 'Exit code:', r )

