def merge(my_list1, my_list2):
    i = j = 0
    combined_list = []
    while i < len(my_list1) and j < len(my_list2):
        if my_list1[i] < my_list2[j]:
            combined_list.append(my_list1[i])
            i += 1
        else:
            combined_list.append(my_list2[j])
            j += 1

    while i<len(my_list1):
        combined_list.append(my_list1[i])
        i += 1
    while j<len(my_list2):
        combined_list.append(my_list2[j])
        j += 1

    return combined_list

print(merge([1,2,7,100],[3,6,8,16]))
