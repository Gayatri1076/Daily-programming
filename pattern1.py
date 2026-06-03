for i in range(7):
    for j in range(4):
        if j>=i and j<=8-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
