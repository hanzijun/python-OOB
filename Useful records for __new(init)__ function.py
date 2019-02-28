#!/usr/bin/python 
"""
__new/init__ use case for python
"""
class Person(object):
    def __new__(cls, age):
        print "Person.__new__ called"
        return super(Person, cls).__new__(cls, age)
        
    def __init__(self, age):
        print "Person.__init__ called"
        self.age = age
    def fn(self):
        print "Person fn"

class Man(object):
    def __new__(cls, age):
        print "Man.__new__ called"
        if age > 10:
            return super(Man, cls).__new__(cls, age)
        return Person(age)
      
    def __init__(self, age):
        print "Man.__init__ called"
        self.age = age
    def fn(self):
        print "Man fn"

a = Man(5)
The results are :
#Man.__new__ called
#Person.__new__ called
#Person.__init__ called
a = Man(15)
The results are :
#Man.__new__ called
#Man.__init__ called
