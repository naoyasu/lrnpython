# http://tinyurl.com/j2scn4f

a = input("type a number:")
b = input("type another:")
a = int(a)
b = int(b)
try:
    print(a/b)
except ZeroDivisionError:
    print("b can't be zero.")

