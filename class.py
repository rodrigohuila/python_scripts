#! /usr/bin/python3

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        return "My name is %s and I am %i years old" % (self.name, self.age)


e = Student("Arturo", 21)
print(e.hello())

