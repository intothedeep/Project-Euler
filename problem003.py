#!/bin/python3

def ff(n, arr):
    factor =  2
    sub_arr = []
    while factor <= n ** 0.5:
        if n % factor == 0:
            sub_arr = ff(factor, []) + ff(n // factor, [])
            break
        factor += 1
    if len(sub_arr) == 0:
        sub_arr.append(n)
    return arr + sub_arr

result = []

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    factors = ff(n, [1])
    result.append(str(max(factors)))
    
print('\n'.join(result))
