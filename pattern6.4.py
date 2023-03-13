'''
1234
123
12
1
'''

x = int(input("enter no or rows"))
for i in range(x):                  #rows
    for j in range(x-i):            #columns
        print(j+1, end=" ")
    print()
