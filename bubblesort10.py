def sort(nums):
    for i in range(len(nums)-1,0,-1):#iterations
        for j in range (i):#swapping
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp

nums=[2,6,3,8,4,7,9,6]
sort(nums)
print(nums)