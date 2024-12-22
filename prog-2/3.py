from multipledispatch import dispatch
@dispatch(int, int)
def add(x , y):
    return x+y
@dispatch(int, int , int)
def add(x , y , z):
   return x+y+z

print(add(6, 4))