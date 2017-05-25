#coding:utf-8
'regexp test'
import re

#手机号格式匹配
pattern = r'^(13\d|15[012356789]|14[57]|18\d|17[013678])\d{8}$'

phone = '15501191752'

match_result = re.match( pattern, phone )

print( match_result )

#分割字符串
str = 'a,b;;c   d'

splits = re.split( r'[\s\,\;]+', str )

print( splits )

#分组

pattern = r'^(\d{3})-(\d{3,8})'

match_result = re.match( pattern, '010-456900')

print( match_result.groups() )

pattern = r'^([0-1][0-9]|2[0-3]|[0-9])\:([0-5][0-9]|[0-9])\:([0-5][0-9]|[0-9])$'

time_result = re.match( pattern, '23:52:52' )
print( time_result.groups() )

#贪婪模式和非贪婪模式

more_match = re.match( r'^(\d+)(0*)$', '1023000')

print( more_match.groups() )

less_match = re.match( r'^(\d+?)(0*)$', '1023000')

print( less_match.groups() )

#预编译正则表达式
re_telphone = re.compile( r'^(13|15|18)\d{9}$' )

print( re_telphone.match( '15501191752' ).group( 0 ) )

print( re_telphone.match( '15610136645' ).group( 0 ) )

#email正则

pattern = r'^(\w+.)+@(\w+.)+(com|cn|org)$'

re_email = re.compile( pattern )

print( re_email.match('someone@gmail.com').group(0) )
print( re_email.match('bill.gates@micrsoft.com').group(0) )


