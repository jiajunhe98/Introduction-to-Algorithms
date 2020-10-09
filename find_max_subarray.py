def find_max_subarray(list, print_array = False):
    '''a function to find the maxium subarray of an input list, whose time complexity is O(n)'''
    max_subarray = [list[0],0,1]
    max_subarray_to_end = [list[0],0,1]
    for i in range(2,len(list)+1):
        max_subarray_to_end[2] = i
        if max_subarray_to_end[0] < 0:
            max_subarray_to_end[0] = list[i-1]
            max_subarray_to_end[1] = i-1
        else:
            max_subarray_to_end[0] += list[i-1]
        if list[max_subarray[2]] >= 0:
            max_subarray[0] += list[max_subarray[2]]
            max_subarray[2] += 1
        if max_subarray_to_end[0] > max_subarray[0]:
            max_subarray = max_subarray_to_end.copy()
    result = {}
    result["max value"] = max_subarray[0]
    if print_array == True:
        result["max array"] = list[max_subarray[1]:max_subarray[2]]
    result["index"] = (max_subarray[1],max_subarray[2]-1)
    return result








#test
arr = [-1, -3, 3, 5, -4, 3, 2, -2, 3, 6,100,20,10,-302,-20]
print(find_max_subarray(arr))

b = []
import random
for i in range(int(1e5)):
    b.append(random.randint(-1000,1000))
import time
start = time.time()
print(find_max_subarray(b))
end = time.time()
print ("time:"+ str(end -start))
