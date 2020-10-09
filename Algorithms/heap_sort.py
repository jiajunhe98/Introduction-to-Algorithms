import math
class MaxHeap():
    '''a class implementing max heap'''
    def __init__(self,list):
        '''initial the heap'''
        self.size = len(list)
        self.elements = [0]*(self.size + 1)
        self.parents = [0]*(self.size + 1)
        self.leftchild = [0]*(self.size + 1)
        self.rightchild = [0]*(self.size + 1)
        for i,val in enumerate(list):
            heap_index = i + 1
            self.elements[heap_index] = val
            if heap_index == 1:
                self.parents[heap_index] = None
            else:
                self.parents[heap_index] = int(heap_index/2)
            if heap_index > self.size/2 :
                self.leftchild[heap_index] = None
                self.rightchild[heap_index] = None
            else:
                self.leftchild[heap_index] = 2 * heap_index
                if 2 * heap_index + 1 <= self.size:    #in case that the parent node only has one child node
                    self.rightchild[heap_index] = 2 * heap_index + 1
                else:
                    self.rightchild[heap_index] = None


    def max_heapify(self,i):
        '''take an index as input, and put that element into proper position'''
        if i > self.size:
            return -1
        value = self.elements[i]
        left_index = self.leftchild[i]
        right_index = self.rightchild[i]
        if left_index == None and right_index == None:
            return 0
        if left_index != None:
            left = self.elements[left_index]
        else:
            left = -math.inf
        if right_index != None:
            right = self.elements[right_index]
        else:
            right = -math.inf
        largest =  value
        largest_index = 0 # 0 parents ; 1 left child ; 2 right child
        if right > largest:
            largest = right
            largest_index = 2
        if left > largest:
            largest = left
            largest_index = 1
        if left_index == 0:
            return 0
        if largest_index == 1:
            self.elements[left_index] = value
            self.elements[i] = largest
            self.max_heapify(left_index)
        if largest_index == 2:
            self.elements[right_index] = value
            self.elements[i] = largest
            self.max_heapify(right_index)

    def build_max_heap(self):
        '''build a max heap'''
        for i in range(int(self.size/2),0,-1):
            self.max_heapify(i)

    def output(self):
        '''output a list of this max heap'''
        return self.elements[1:self.size+1]

    def get_size(self):
        return self.size

    def pop(self):
        '''pop the last element'''
        if self.size%2 == 0:
            self.leftchild[int(self.size/2)] = None
        else:
            self.rightchild[int(self.size/2)] = None
        self.parents[self.size] = None
        self.size -= 1
        return self.elements[self.size+1]


    def exchange_element(self,a,b):
        '''change the ath and bth elements'''
        ele_a = self.elements[a]
        self.elements[a] = self.elements[b]
        self.elements[b] = ele_a


def heap_sort(list):
    '''build a heap and sort in descending order, this function will NOT change the original list'''
    result = []
    max_heap = MaxHeap(list)
    max_heap.build_max_heap()
    while(max_heap.get_size() > 0):
        max_heap.exchange_element(1,max_heap.get_size())
        result.append(max_heap.pop())
        max_heap.max_heapify(1)
    return result


