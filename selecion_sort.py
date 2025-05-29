# def selectionSort( arr):
#     #code here
    
#     len_arr = len(arr)
    
#     for i in range(len_arr):
#         min_num = arr[i]
#         min_index = i

#         for j in range(i+1,len_arr):
#             if arr[j] < min_num:
#                 min_num = arr[j]
#                 min_index = j

#         arr[i], arr[min_index] = arr[min_index], arr[i]
        
#     return arr
# print(selectionSort([4,1,3,9,7]))

def bubbleSort(arr):
    # code here
    len_arr = len(arr)
    for i in range(len_arr-1):
        swap = 0
        for j in range(len_arr-i-1):
            if arr[j] > arr[j+1] :
                swap = 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if swap == 0:
            return arr
        # print("runs")
    return arr

print(bubbleSort([4,1,3,9,7]))
