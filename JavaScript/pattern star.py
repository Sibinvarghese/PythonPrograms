for row in range(1,5):
    for col in range(1 ,8):
        if((row==4) | (row+col==5) | (col-row==3)):
            print("*",end=" ")
        else:
            print(end=" ")
    print()