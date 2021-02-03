import abc

class People(metaclass=abc.ABCMeta):
    age=0
    name=''

    def __init__(self, a, b):
        self.name=b
        self.age=a

    abc.abstractmethod
    def open(self):
        pass

class Specaialist(People):
    wage=0

    def Result(self, a):
        self.wage=a
    def open(self):
        return self.wage/self.age

b=People(10,'45')
b.age=10
a=Specaialist(10,'TEst')
print(a)