def recursiveMethod(n):
    if n<1:
        print("n is less than 1")
    else:
        recursiveMethod(n-1)
        print(n)
n = int(input("Enter your number:"))
recursiveMethod(n)
