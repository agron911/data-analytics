# list1 = [1,3,4,5,1]
list1 = [1,3,2]



def next_permu(nums):
    length = len(nums)
    index =length-1
    while index>=1:
        if nums[index] >nums[index-1]:
            for i in range(length-1,index-1,-1):
                if nums[i] >nums[index-1]:
                    nums[i],nums[index-1] = nums[index-1],nums[i]
                    nums[index:] = sorted(nums[index:])
                    print(nums)
                    return nums
        else:
            index -=1
    
    nums.reverse()
    
    return nums

print(next_permu(list1))
def next_(nums):
    length = len(nums)
    index = length-1
    while index>=1:
        if nums[index]>nums[index-1]:
            for i in range(length-1,index-1,-1):
                if nums[i]> nums[index-1]:
                    nums[i],nums[index-1] = nums[index-1],nums[i]
                    nums[index:] = sorted(nums[index:])
                    print(nums)
                    return nums
        else:
            index -= 1
    nums.reverse()
    return nums

print(next_(list1),'=\n')

list1=[1,3,2]
def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    length = len(nums)
    index = length-1
    
    while index>=1:
        if nums[index]>nums[index-1]:
            for i in range(length-1,index-1,-1):
                if nums[i]> nums[index-1]:
                    nums[i] , nums[index-1] = nums[index-1], nums[i]
                    print('.',nums)
                    nums[index:] = sorted(nums[index:])
                    print(nums)
                    return nums
        else:
            index-=1
        nums.reverse()
        return nums
print(nextPermutation(list1))



