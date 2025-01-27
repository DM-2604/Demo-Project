class Test:
    a=10
    def __init__(self):
        self.__b=20
    # @property
    def setter(self,t):
        print("set value")
        self.__b=t

    def getter(self):
        return self.__b
          

t1=Test()
t1.setter(500)

print(t1.getter())
# print(t1.a,t1.b)
# print(t2.a,t2.b)
