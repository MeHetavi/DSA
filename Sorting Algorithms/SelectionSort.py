# Select the minimum and swap.
# worst, average and best: O(n^2)
def selectionSort(self, arr):
    len_arr = len(arr)
    for i in range(len_arr-1):
        mini = i
        for j in range(i+1,len_arr):
            if arr[j] < arr[mini]:mini = j            
        arr[i], arr[mini] = arr[mini], arr[i]
    return arr
