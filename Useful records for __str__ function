#!/usr/bin/python 
"""
__str__ use case for python
"""
class Person(object):
    def __new__(cls, age):
        print "Person.__new__ called"
        return super(Person, cls).__new__(cls, age)
        
    def __init__(self, age):
        print "Person.__init__ called"
        self.age = age
    def __str__(self):
        return "The age of Person: %d" % (self.age)
		
a = Person(5)
print a

use case one: __str__
The results are:
#Person.__new__ called
#Person.__init__ called
#The age of Person: 5

use case two: without __str__
The results are:
#Person.__new__ called
#Person.__init__ called
#<__main__.Person object at 0x7f68b41ea5d0>
