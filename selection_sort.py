def selection_sort(list):
    min_index = 0
    for i in range(len(list)):
        min_index = i
        for j in range(i+1,len(list)):
            if list[j] < list[min_index]:
                min_index = j
        temp = list[i]
        list[i]=list[min_index]
        list[min_index]= temp
    return list

print (selection_sort([2,4,1,5,7,23,67,45,12,65,98,43,12,43,76,11,99]))