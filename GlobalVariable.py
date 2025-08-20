x = 55
def func():
    global y
    y = 53
    y = x ++ y
    print("Python is ",x)
func()
print(y)

