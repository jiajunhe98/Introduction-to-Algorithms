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




