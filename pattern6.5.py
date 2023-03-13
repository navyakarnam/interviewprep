'''
1234
234
34
4
'''

x = int(input("enter no or rows"))
for i in range(x):                  #rows
    for j in range(x-i):            #columns
        print(j+i+1, end=" ")
    print()
