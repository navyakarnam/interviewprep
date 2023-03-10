num=int(input("Enter the no: "))
for i in range(2,num):
    if num%i==0:
        print("Not a prime")
        break
else:
    print("is a prime")