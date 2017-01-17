#coding:utf-8

'''
slice list 切片
'''
# 1、切片100数字计算
L= range(1,100)

#前10个数
print L[0:10]

#3的倍数
print L[2::3]

#不大于50的5的倍数
print L[4:50:5]

#最后10个5的倍数
print L[4::5][-10:]


##首字母大写

def firstCharUpper(s):
    s = s.lower()
    return s[:1].upper()+s[1:]

print firstCharUpper('HELLO')
