nums = [1,3,5,8,9,9,9]
def remove_duplicate(nums):
    if not nums:
        return 0 
    remove_end = 0
    for i in range(len(nums)):
        if (nums[i] != nums[remove_end]) :
            remove_end +=1
            nums[remove_end] = nums[i]
    return remove_end+1,nums

print(remove_duplicate(nums))