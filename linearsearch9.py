#Linear Search
lst=[]#create an empty list
n=int(input("enter the no of elements to be entered in the list: "))
for i in range(0,n):
    ele=int(input("Enter the elements: "))

    lst.append(ele)
print(lst)


pos=-1
def search(lst,x):   # creating a search function
    i=0
    while i<n:
        if lst[i]==x:
            globals()['pos']=i
            return True
        i=i+1
    return False


x=int(input("enter the element to be searched: "))
if search(lst,x):
    print("found at", pos)
else:
    print("not found")
