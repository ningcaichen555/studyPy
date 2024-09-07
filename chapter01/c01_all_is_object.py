# 可以赋值给一个变量
def ask(name='li'):
    print(name)


my_func = ask


class Person:
    def __init__(self):
        print("bobby")


my_class = Person

objList = []

objList.append(my_func)
objList.append(my_class)

for item in objList:
    print(item())
# li
# None 返回值
# bobby
# <__main__.Person object at 0x101657fe0> 返回值


def printType(item):
    print(type(item))


for item in objList:
    printType(item)
# <class 'function'>
# <class 'type'>

# my_func("hi")
# my_class()


def decorator_func():
    print("dec start")
    return ask


decorator_func()()

# dec start
# li
