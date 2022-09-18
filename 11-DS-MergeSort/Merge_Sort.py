from operator import le
from turtle import right

def merge(my_list1, my_list2):
    i = 0
    j = 0
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

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid = int(len(my_list)/2)
    left = my_list[:mid]
    right = my_list[mid:]
    return merge(merge_sort(left), merge_sort(right))

print(merge_sort([4,2,6,5,1,3]))
