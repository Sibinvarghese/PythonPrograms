def fact(num1):
    fact=1
    if(num1<0):
        print("sorry Factorial For Negative Numbers Does Not Exist ")
    elif(num1==0):
        print("The Factorial Of Zero is 1")

    else:
        for i in range(1,(num1+1)):
            fact=fact*i
        print("The Factorial Of",num1,"is",fact)

num2=int(input("enter a number : "))
fact(num2)