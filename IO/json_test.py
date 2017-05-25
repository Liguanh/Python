#coding:utf-8

'json type test'
__author__='linguanghui'

import json
from classProvider  import Students

d = dict( name='Bob', age =20, score=88 )

jsons  = json.dumps( d )
print( jsons )

dejson = json.loads( jsons )

print( dejson )

s = Students( 'Bob', 10, 88 )

classJson = json.dumps( s, default=lambda obj: obj.__dict__ )
print( classJson )

deloads = json.loads( classJson )

print( deloads )
