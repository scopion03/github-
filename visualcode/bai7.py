def sum(positive_integer):
    if (positive_integer / 10) == 0:
        f = positive_integer % 10
        return int(f)
    else:
        f = positive_integer % 10 + sum(positive_integer / 10)
        return int(f)

positive_integer = int(input("Enter a positive integer: "))
print(int(sum(positive_integer)))
