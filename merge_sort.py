def merge_lists(list1,list2):
    '''a function to merge two lists by order'''
    result_list = []
    max_len = max(len(list1),len(list2))
    min_len = min(len(list1),len(list2))
    index_1 = 0
    index_2 = 0
    while(index_1 < len(list1) and index_2 < len(list2)):
        if list1[index_1] <= list2[index_2]:
            result_list.append(list1[index_1])
            index_1 += 1
        else:
            result_list.append(list2[index_2])
            index_2 += 1
    if index_1 >= len(list1):
        for i in list2[index_2:len(list2)]:
            result_list.append(i)
    else:
        for i in list1[index_1:len(list1)]:
            result_list.append(i)
    return result_list

def merge_sort(list):
    '''a function to sort a list of numbers by merge-sort algorithm, this function will NOT change the original list'''
    length = len(list)
    if length == 1:
        return list
    list1 = list[:int(length/2)]
    list2 = list[int(length/2):]
    return merge_lists(merge_sort(list1),merge_sort(list2))


#test
a = [1,2,3,2,1,3,2,100,3,53,-20,2,222]
a = merge_sort(a)
print(a)
print("")

b = []
import random
for i in range(int(1e5)):
    b.append(random.randint(-100,100))
import time
start = time.time()
b = merge_sort(b)
end = time.time()
print ("time:"+ str(end -start))
