#coding:utf-8
import random
import sys


grocery_list = ['Juice','Tomatoes','Potatoes','Bananas']

print "First Item",grocery_list[0]

grocery_list[0]='Green Juice'

print "First Item",grocery_list[0]

print grocery_list[0:4]

other_events=['Wash Car','Pick up Kids','Cash Check']

to_do_list = [grocery_list,other_events]

print to_do_list[0][1]

grocery_list.append('Onions')

print to_do_list
print "\n"*5
for value in to_do_list:
    for name in value:
        print name

other_events.insert(1,"Pickle")

print "\n"*5
for value in to_do_list:
    for name in value:
        print name

to_do_list2 = grocery_list+other_events

print (len(to_do_list2))

print