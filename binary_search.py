# list is sorted
from typing import List
import numpy as np
import csv
import random
import time

def naive_search(list, target):
    for i in range(len(list)):
        #print(str(i) + ', ' + str(target))
        if list[i] == target:
            return i
    return -1


def binary_search(list, target, l_ind=None, r_ind=None):
    #first time init
    if l_ind == None:
        l_ind = 0
    if r_ind == None:
        r_ind = len(list)
    #if nothing found
    if (r_ind - l_ind) < 1:
        return -1

    #print(list[l_ind: r_ind])
    mid_index = (r_ind + l_ind) // 2
    #print(mid_index)
    if list[mid_index] == target:
        return mid_index
    elif list[mid_index] > target:
        next_left_index = l_ind
        next_right_index = mid_index
        
    else: 
        next_left_index = mid_index + 1
        next_right_index = r_ind
    
    return binary_search(list, target, next_left_index, next_right_index)



if __name__=='__main__':

    list1 = np.loadtxt('list.txt', delimiter=',', unpack=True)
    #print(naive_search(list1, 34))
    #print(len(list1))
    #print(len(list1) // 2)
    targ = 66
    print(binary_search(list1, targ))

    #random list
    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))

    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for every_target in sorted_list:
        #naive_search(sorted_list, every_target)
        #2.8 sec
        binary_search(sorted_list, every_target)
        #0.06 sec
    #print(naive_search(sorted_list, targ))
    end = time.time()
    print(end-start)
