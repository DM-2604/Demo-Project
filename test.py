# 
def logit(func):
    # def with_logging(*a):
    # print(func.__name__ + " was called")
    print(func(4))
    return func
    # print("this give the multi")
    # return with_logging

@logit
def addition_func(x):
   """Do some math."""
   print("before the return of addi")
   return x + x
   
y=addition_func(5)
print(y)
