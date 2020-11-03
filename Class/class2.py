class MyClass:
    '''This is second class'''
    a=10
    def func(self):
        print("HELLO")
print(MyClass.a)

MyClass.func(True)
print(MyClass.__doc__)


ob = MyClass()
ob.func()
