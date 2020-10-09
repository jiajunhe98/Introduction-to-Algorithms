def insertion_sort(list):
    '''a function to sort a list of number by insertion-sort algorithm, this function will change the original list'''
    length = len(list)
    for i in range(1,length):
        sorted_num = list[i]
        for j in range(i-1,-1,-1):
            if sorted_num < list[j]:
                list[j+1] = list[j]
                list[j] = sorted_num
            else:
                break
    return 0

'''
#test
a = [1,2,3,2,1,3,2,100,3,53,-20,2,222]
insertion_sort(a)
print(a)
print("")

b = []
import random
for i in range(int(3*1e4)):
    b.append(random.randint(-100,100))
import time
start = time.time()
insertion_sort(b)
end = time.time()
print ("time:"+ str(end -start))
'''



