def selection_sort(my_list):
    length = 0
    while length < len(my_list)-1:
        min_index = length
        for i in range(length+1, len(my_list), 1):
            if my_list[i] < my_list[min_index]:
                min_index = i
        if min_index != length:
            temp = my_list[length] 
            my_list[length] = my_list[min_index]
            my_list[min_index] = temp
        length += 1
    return my_list

print(selection_sort([4,2,6,5,1,3]))

            
