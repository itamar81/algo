
MAX_INT=9999999

arr= [5,7,6,1,7,547,456,3547,37,48,98,66,3563,48,9,66,33,33,11,4,8,78,65,27,48,15,35,55]
def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        # if not swapped:
        #     # if we haven't needed to make a single swap, we
        #     # can just exit the main loop.
        #     return 

bubbleSort(arr)
print(arr)
