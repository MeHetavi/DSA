def selection_sort(nums):
    for index,num in enumerate(nums):
        try:
            minimum = min(nums[index+1:])
        except Exception:
            break
        if num > minimum:
            nums[nums.index(minimum)] =  num
            nums[index] = minimum
    return nums

nums= [1,4,3,60,77,23,11,26]
selection_sort(nums)
print(nums)