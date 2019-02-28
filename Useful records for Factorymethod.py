#!/usr/bin/python 

class LeiFeng():
    def buy_rice(self):
        pass
    def sweep(self):
        pass

class Student(LeiFeng):
    def buy_rice(self):
        print 'Student buy_rice'

    def sweep(self):
        print 'Student sweep'


class Volunteer(LeiFeng):
    def buy_rice(self):
        print 'Volunteer buy_rice'

    def sweep(self):
        print 'Volunteer sweep'

class LeiFengFactory():
    def create_lei_feng(self, type):
        map_ = {'stu': Student(),'vol': Volunteer()}
        return map_[type]

leifeng1 = LeiFengFactory().create_lei_feng('stu')
leifeng2 = LeiFengFactory().create_lei_feng('stu')
leifeng3 = LeiFengFactory().create_lei_feng('stu')
leifeng1.buy_rice()
leifeng1.sweep()

# 简单工厂: 写一个雷锋类，定义buy_rice和sweep两个方法，写一个student和volunteer类继承雷锋类，写一个factory类，根据输入的类型返回student类或volunteer类。

class LeiFeng():
    def buy_rice(self):
        pass

    def sweep(self):
        pass
        
class Student(LeiFeng):
    def buy_rice(self):
        print 'Student buy_rice'

    def sweep(self):
        print 'Student sweep'

class Volunteer(LeiFeng):
    def buy_rice(self):
        print 'Volunteer buy_rice'

    def sweep(self):
        print 'Volunteer sweep'

class LeiFengFactory():
    def create_lei_feng(self):
        pass
        
class StudentFactory(LeiFengFactory):
    def create_lei_feng(self):
        return Student()

class VolunteerFactory(LeiFengFactory):
    def create_lei_feng(self):
        return Volunteer()

myFactory = StudentFactory()
leifeng1 = myFactory.create_lei_feng()
leifeng2 = myFactory.create_lei_feng()
leifeng3 = myFactory.create_lei_feng()
leifeng1.buy_rice()
leifeng1.sweep()
# 工厂方法：雷锋类，student类，volunteer类和简单工厂一样，新写一个工厂方法基类，定义一个工厂方法接口，然后写一个student工厂类，volunteer工厂类，返回各自的类。

工厂方法相对于简单工厂的优点：

1.在简单工厂中，如果需要新增类，例如加一个MiddleStudent类，就需要新写一个类，同时要修改工厂类的map_，加入'MiddleStudent':MiddleStudent()。
这样就违背了封闭开放原则中的一个类写好后，尽量不要修改里面的内容的原则。
而在工厂方法中，需要增加一个MiddleStudent类和一个MiddleStudentFactory类，虽然比较繁琐，但是符合封闭开放原则。
在工厂方法中，将判断输入的类型，返回相应的类这个过程从工厂类中移到了客户端中实现，所以当需要新增类时，也是要修改代码的，
不过是改客户端的代码而不是工厂类的代码。

2.对代码的修改会更加方便。例如在客户端中，需要将student的实现改为volunteer，如果在简单工厂中，就需要把

LeiFengFactory().create_lei_feng('student') 改为 LeiFengFactory().create_lei_feng('volunteer')，但是在工厂方法中，
只需把 myFactory = StudentFactory() 改成 myFactory = VolunteerFactory()。
