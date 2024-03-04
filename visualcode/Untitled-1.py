def openRussianDoll(Doll):
    if Doll == 1:
        print("All dolls are opened")
    else:
        print("opening doll {Doll}") 
        openRussianDoll(Doll - 1)

    numDolls = int(input("enter the number of Russian dolls:"))
    openRussianDoll(numDolls)