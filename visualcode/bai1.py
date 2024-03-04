def openRussianDoll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        print(doll)
        openRussianDoll(doll-1)

doll = int(input("Enter the number of Russian dolls: "))
openRussianDoll(doll )
