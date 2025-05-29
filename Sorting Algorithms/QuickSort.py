# def quickSort(nums):
    
#     if len(nums) <= 1:
#         return nums
    
#     pivot = nums[0]
#     larger_elements= []
#     smaller_elements = []
#     mid_elements = []
#     for num in nums:
#         if num>pivot:
#             larger_elements += [num]
#         elif num<pivot:
#             smaller_elements += [num]
#         else :
#             mid_elements += [pivot]

#     return quickSort(smaller_elements) + mid_elements + quickSort(larger_elements)

# print(quickSort([5,4,3,1,2,8,2,3,1,6,8,90,33,21,122,343,221,113,445,2345]))

# def s(arr, low, high):
#     pivot = arr[low]
#     while True:
#         while arr[low] and arr[low] < pivot:
#             low+=1
#         while arr[high] and arr[high] > pivot:
#             high -= 1
#         if high < low:
#             break
#         arr[low] , arr[high] = arr[high] , arr[low]
#         ...


# def quickSort(arr):
#     low = 0
#     high = len(arr) - 1

#     if low < high :
#         pivot_index = s(arr, low, high)
#         quickSort(arr, low, pivot_index-1)
#         quickSort(arr, pivot_index+1, high)
#     ...