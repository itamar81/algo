def bubble_sort(list):
    print("len: ",str(len(list)))
    iteration = 0
    for i in range(len(list)):
        for j in range(len(list)-i):
            iteration +=1
            if list[j] > list[i]:
                temp = list[j]
                list[j] = list[i]
                list[i] = temp
    print("iter: ",str(iteration))
    return list

print(bubble_sort([2,4,1,5,7,23,67,45,12,65,98,43,12,43,76,11,99]))