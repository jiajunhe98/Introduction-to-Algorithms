def partition(list,start,end):
    '''partition a list into 2 parts between main element, the 1st part is smaller than this element, while the second part is larger'''
    k = start
    for j in range(start,end):
        if list[j] < list[end-1]:
            list_k = list[k]
            list[k] = list[j]
            list[j] = list_k #exchange k and j
            k += 1
    list_last_element = list[end-1]
    list[end-1] = list[k]
    list[k] = list_last_element
    return k


def quick_sort(list,start = 0, end = None):
    '''a function to sort a list of numbers by quick-sort algorithm, this method will change the original list'''
    if end == None:
        end = len(list)
    if start == end:
        return 0
    k = partition(list, start, end)
    quick_sort(list, start = start, end = k)
    quick_sort(list, start = k+1, end = end)
    return 0

'''
#test
a = [1,2,3,2,1,3,2,100,3,53,-20,2,222]
quick_sort(a)
print(a)
print("")

b = []
import random
for i in range(int(3*1e4)):
    b.append(random.randint(-100,100))
import time
start = time.time()
quick_sort(b)
end = time.time()
print ("time:"+ str(end -start))
'''