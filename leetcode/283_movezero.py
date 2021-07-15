list1 = [0,1,3,0,12,0]

def move_zero(nums):
    index = 0
    for i in nums:
        if i !=0:
            nums[index] = i
            index +=1
    for i in range(index,len(nums)):
        nums[i] =0
    return nums

print(move_zero(list1))



