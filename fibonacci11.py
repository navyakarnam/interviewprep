#0 1 1 2 3 5 8 13 21....
def fib(n):
   a=0
   b=1

   if n==1:
        print(a)

   elif n<0:
       print("negative no is not allowed")

   else:
        print(a)
        print(b)

        for n in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)

n=int(input("enter the no: "))
fib(n)
