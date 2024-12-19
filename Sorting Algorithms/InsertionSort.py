# Select min and insert at it's correct position.
# worst and average : O(n*(n+1)/2) = O(n)
# best : O(n)
def insertionSort(self, arr):
    len_arr = len(arr)
    for i in range(len_arr):
        while i>0 and arr[i-1] > arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i] 
                i-=1
    return arr