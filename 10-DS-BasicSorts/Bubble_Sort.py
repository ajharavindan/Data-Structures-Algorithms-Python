def bubble_sort(li):
    length = len(li)
    while length > 1:
        for i in range(length-1):
            if li[i] > li[i+1]:
                temp = li[i]
                li[i] = li[i+1]
                li[i+1] = temp
        length -= 1
    return li

print(bubble_sort([1000,4,2,6,10,11,100,1,5,1,3]))


        

