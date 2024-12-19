# def merge(a,b): # Returns sorted(a+b).
#     c = []
#     len_c = len(a+b)
#     i = 0
#     j = 0
#     len_a = len(a)
#     len_b = len(b)
#     for k in range(len_c):
#         if i == len_a:
#             c = c + b[j:]
#             break
#         elif j == len_b:
#             c = c + a[i:]
#             break
#         elif a[i]>b[j]:
#             c = c + [b[j]]
#             j+=1
#         else:
#             c = c + [a[i]]
#             i+=1 
#     return c

# def main():
#     unsorted_list = [5,4,3,2,1]
#     print(partition(unsorted_list))

# def partition(unsorted_list): # Patitions the list until there is only 1 element left in the list and then rturnes the sorted merged list.
#     length = len(unsorted_list)
#     if length == 0 or length==1:
#         return unsorted_list # Base case.
#     else:
#         mid = length//2
#         a = partition(unsorted_list[:mid])# first half of Unsorted_list 
#         b = partition(unsorted_list[mid:])# Second half of Unsorted_list 
#         return merge(a,b)# sorted two halves along with combining them.
# main()

# Divide and merge.
# time(all cases) : O(n * log(n))
# Space(all cases) : O(n*5) = O(n)

def mergeSort(arr):

    len_arr = len(arr)

    if len(arr) == 1:
        return arr

    l = (len_arr//2)

    left_arr = mergeSort(arr[:l])
    right_arr = mergeSort(arr[l:])

    sorted_arr = []
    len_left_arr = len(left_arr)-1
    len_right_arr = len(right_arr)-1
    i = len_left_arr
    j = len_right_arr

    while i>=0 or j>=0:
        if i<0:
            sorted_arr+=right_arr[(len_right_arr-j):]
            break

        elif j<0:
            sorted_arr+=left_arr[(len_left_arr-i):]
            break

        if left_arr[len_left_arr-i] < right_arr[len_right_arr-j]:
            sorted_arr+=[left_arr[len_left_arr-i]]
            i-=1

        else:
            sorted_arr+=[right_arr[len_right_arr-j]]
            j-=1
    return sorted_arr

print(mergeSort([4,1,3,9,2,10]))