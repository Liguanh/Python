#coding:utf-8

'module testing'

from datetime import datetime, timedelta, timezone

now = datetime.now()

print( now )

print( type( now ) )

dt = datetime( 2017,5,22,18,43 )

print( dt )

tp = dt.timestamp()
print( tp )

print( datetime.fromtimestamp( tp ) )

print( datetime.utcfromtimestamp( tp ) )

print( datetime.strptime( '2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S' ) )

print( now.strftime( '%a, %b %H:%M' ) )
#时间加减
print( now + timedelta( hours = 2 ) )

print( now - timedelta( days =1 ) )

#UTC 时间

tz_utc_8 = timezone( timedelta( hours = 8 ) )

now = datetime.now()
print( now )

dt = now.replace( tzinfo = tz_utc_8 )
print( dt )

#时区转换

utc_dt = datetime.utcnow().replace( tzinfo = timezone.utc )

print( utc_dt )

bj_dt = utc_dt.astimezone( timezone( timedelta( hours = 8 )))

print(bj_dt)
