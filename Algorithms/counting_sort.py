def counting_sort(list):
    '''a function to sort a list of integers, the function will NOT change the original list'''
    max_int = list[0]
    min_int = list[0]
    for i in list:
        if int(i) != i:
            print("Must be a list of integers")
            return None
        if i > max_int:
            max_int = i
        if i < min_int:
            min_int = i
    for i in range(len(list)):
        list[i] -= min_int  #normalize all elements to [0,inf)

    new_max_int = max_int-min_int
    new_list = [0]*len(list)
    count_list = [0]*(new_max_int+1)
    for i in list:
        count_list[i] += 1
    for i in range(1,len(count_list)):
        count_list[i] += count_list[i-1]
    for i in range(len(list)-1,-1,-1):
        new_list[count_list[list[i]]-1] = list[i]
        count_list[list[i]] -= 1
    for i in range(len(list)):
        list[i] += min_int
        new_list[i] += min_int
    return new_list





