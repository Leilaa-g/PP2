x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)
    
myfunc()

print("Python is " + x)

def myfunc():
    global y
    y = "Fantastic"
    
myfunc()

print("Python is " + y)