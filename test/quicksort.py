def swap(arr,index1,index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp

def pivot(arr,pivot_index,end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1,end_index+1):
        if arr[i] < arr[pivot_index]:
            swap_index += 1
            swap(arr,swap_index,i)
    swap(arr,pivot_index,swap_index)
    return swap_index

def _quicksort(arr,left,right):
    if left < right:
        pivot_index = pivot(arr,left,right)
        _quicksort(arr,left,pivot_index-1)
        _quicksort(arr,pivot_index+1,right)
    return arr
def quicksort(arr):
    return _quicksort(arr,0,len(arr)-1)
my_list =[4,6,1,7,43,12,54,3,2,5,12,65,87,9]
print(pivot(my_list,0,len(my_list)-1))
print(quicksort(my_list))