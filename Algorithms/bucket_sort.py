import insertion_sort
def bucket_sort(list):
    '''a function to sort a list of floats in [0,1), this function will NOT change the original list'''
    bucket_num = len(list)
    bucket_list = []
    for i in range(bucket_num):
        bucket_list.append([])
    for i in list:
        index = int(bucket_num*i)
        bucket_list[index].append(i)
    for i in range(len(bucket_list)):
        insertion_sort.insertion_sort(bucket_list[i])
    result = []
    for i in bucket_list:
        for j in i:
            result.append(j)
    return result

#test
a = [0.1,0.2,0.3,0.2,0.111,0.3,0.2,0.5,0.3,0.53,0.8,0.57,0.85,0.67,0.99]
print(bucket_sort(a))
print("")

b = []
import random
for i in range(int(1e5)):
    b.append(random.random())
import time
start = time.time()
newb = bucket_sort(b)
end = time.time()
print ("time:"+ str(end -start))
