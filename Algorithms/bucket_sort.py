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


