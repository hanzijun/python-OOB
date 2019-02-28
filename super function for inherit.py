class Foo:
  def bar(self, message):
    print(message)

Foo().bar("Hello, World.")
# Hello, World.

当存在继承关系的时候，有时候需要在子类中调用父类的方法，此时最简单的方法是把对象调用转换成类调用，例如：
class FooParent:
  def bar(self, message):
    print(message)
class FooChild(FooParent):
  def bar(self, message):
    FooParent.bar(self, message)

FooChild().bar("Hello, World.")
#Hello, World.

这样做有一些缺点，如修改父类名称，那么在子类中会涉及多处修改，另外，Python是允许多继承的语言，如上所示的方法在多继承时就需要重复写多次，显得累赘。
为了解决这些问题，Python引入了super()机制，如下：

class FooParent(object):
  def bar(self, message):
    print(message)
class FooChild(FooParent):
  def bar(self, message):
    super(FooChild, self).bar(message)

FooChild().bar("Hello, World.")
# Hello, World.

表面上，super(FooChild, self).bar(message) 和FooParent.bar(self, message)方法的结果是一致的。
实际上这两种方法的内部处理机制大大不同，当涉及多继承情况时，就会表现出明显的差异来：

代码一：

class A:
  def __init__(self):
    print("Enter A")
    print("Leave A")

class B(A):
  def __init__(self):
    print("Enter B")
    A.__init__(self)
    print("Leave B")

class C(A):
  def __init__(self):
    print("Enter C")
    A.__init__(self)
    print("Leave C")

class D(A):
  def __init__(self):
    print("Enter D")
    A.__init__(self)
    print("Leave D")

class E(B, C, D):
  def __init__(self):
    print("Enter E")
    B.__init__(self)
    C.__init__(self)
    D.__init__(self)
    print("Leave E")

E()
结果：
Enter E
Enter B
Enter A
Leave A
Leave B
Enter C
Enter A
Leave A
Leave C
Enter D
Enter A
Leave A
Leave D
Leave E
执行顺序很好理解，唯一需要注意的是公共父类A被执行了多次。

代码二：

class A:
  def __init__(self):
    print("Enter A")
    print("Leave A")

class B(A):
  def __init__(self):
    print("Enter B")
    super(B, self).__init__()
    print("Leave B")

class C(A):
  def __init__(self):
    print("Enter C")
    super(C, self).__init__()
    print("Leave C")

class D(A):
  def __init__(self):
    print("Enter D")
    super(D, self).__init__()
    print("Leave D")

class E(B, C, D):
  def __init__(self):
    print("Enter E")
    super(E, self).__init__()
    print("Leave E")

E()
结果：
Enter E
Enter B
Enter C
Enter D
Enter A
Leave A
Leave D
Leave C
Leave B
Leave E

在super机制里可以保证公共父类仅被执行一次，至于执行的顺序，是按照mro进行的（E.__mro__）。

*Note: mro全名为方法解析顺序列表（Method Resolution Order, mro），它代表了类继承的顺序。
mro通过C3 线性化算法实现（图的遍历：深度优先搜索，DFS）。总的来说，一个类的 MRO 列表就是合并所有父类的 MRO 列表，并遵循以下三条原则：
1. 子类永远在父类前面
2. 如果有多个父类，会根据它们在列表中的顺序被检查
3. 如果对下一个类存在两个合法的选择，选择第一个父类

因此，super 和父类没有实质性的关联。
super(cls, inst) 获得的是 cls 在 inst 的 mro 列表中的下一个类。
