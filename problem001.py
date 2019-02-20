#!/bin/python3

def all_sum(n):
    return n * (n + 1) // 2

t = int(input().strip())

result = []
for i in range(t):
    n = int(input().strip())
    n = n - 1
    sum = all_sum(n // 3) * 3 + all_sum(n // 5) * 5 - all_sum(n // 15) * 15
    result.append(str(sum))
    
print('\n'.join(result))
