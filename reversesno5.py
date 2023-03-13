
#same as palindrome

number=int(input("Enter a no: "))
rev=0

while(number>0):
   dig= number%10
   rev=rev*10+dig
   number=number//10

print(rev)