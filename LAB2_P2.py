#Problem 2

a = input("Enter a value")
b = input("Enter a second value")
c = input("Enter a third value")

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)
        
        