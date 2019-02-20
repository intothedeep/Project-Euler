#!/bin/python3

def sum_even_in_fib(n):
    result = 0
    pre_pre = 1
    pre = 1
    while 1:
        cur = pre + pre_pre
        pre_pre = pre
        pre = cur
        if cur > n:
            break
        if cur % 2 == 0:
            result += cur
    return result

result_list = []

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result_list.append(str(sum_even_in_fib(n)))
    
print('\n'.join(result_list))
