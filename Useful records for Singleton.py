#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Singleton():

    def __new__(cls,)
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
        
obj1 = Singleton()
obj2 = Singleton()

obj1.attr1 = 'value1'
print obj1.attr1, obj2.attr1
print obj1 is obj2

The results are:
#value1 value1
#True
