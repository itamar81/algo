
def merge(list1,list2):
    combined = []
    i = j = 0
    while i < len(list1) and j <len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i< len(list1):
        combined.append(list1[i])
        i += 1
    while j< len(list2):
        combined.append(list2[j])
        j += 1
    return combined
  
def sort(arr):
    if len(arr) == 1:
        return arr
    mid_idx = len(arr) // 2
    left_arr = sort(arr[:mid_idx])
    right_arr = sort(arr[mid_idx:])
    return merge(left_arr,right_arr)

arr= [5,7,6,1,7,547,456,3547,37,48,98,66,3563,48,9,66,33,33,11,4,8,78,65,27,48,15,35,55]

print(sort(arr))