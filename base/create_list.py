#coding:utf-8

#快速生成list
#请利用列表生成式生成列表 [1x2, 3x4, 5x6, 7x8, ..., 99x100]
L = [i*(i+1) for i in range(1,100,2)]

print L

#dict 迭代key和value
dict = {'lgh': 85,'wcm':90}
for index,name in dict.items():
    print index,':',name


