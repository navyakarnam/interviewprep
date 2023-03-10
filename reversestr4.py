#1.by slicing
'''
str=str(input("enter a string to reverse: "))
reverse=str[-1: :-1] #start,end,step
print(reverse)
'''

#2.using for loop

#inputstr=str(input("Enter a string to reverse: "))
#reverse=" "

#for i in range(len(inputstr)-1,-1,-1):
 #   reverse=reverse+inputstr[i]
#print(reverse)



#using reversed() function

inputstr=str(input("enter the string to reverse"))

reverse=reversed(inputstr)
print(''.join(reverse))