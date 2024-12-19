# Check pair of 2 elements and Select maximum and keep it at end.
# worst and average : O(n*(n+1)/2) = O(n)
# best : O(n)
def bubbleSort(arr):
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
