#!/usr/bin/env python3

def print_fibonacci(length):
    my_list = []
    first_num = 0
    sec_num = 1
    num = 0
    
    for i in range(length):
        if i in {0,1}:
         my_list.append(i)
         
        else:
         my_list.append(first_num + sec_num)
         num = sec_num
         sec_num = first_num + sec_num
         first_num = num

    print(my_list)

print_fibonacci(0)