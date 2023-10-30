def swap(arr,index1,index2):
    arr[index1],arr[index2] =arr[index2],arr[index1]
def pivot(arr,pivot_index,end_index):
    swap = pivot_index
    for i in range(len(arr),end_index+1):
        if arr[i]<arr[pivot_index]:
            swap+=1
            swap(arr,i,pivot_index)
            
    swap(arr,swap,pivot_index)

def _quicksort(arr,right,left):
    if right 
def quicksort(arr):
