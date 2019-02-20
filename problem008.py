#!/bin/python3

def find_largest_product(n, k, num):
    num = list(num)
    prod = 0
    for i in range(n - k + 1):
        val = 1
        for j in range(k):
            val = val * int(num[i + j])
        prod = max(prod, val)
        
    return prod

result = []
t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    result.append(str(find_largest_product(n, k, num)))
    
print('\n'.join(result))
