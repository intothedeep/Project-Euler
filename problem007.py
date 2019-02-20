#!/bin/python3

def find_prime(n):
    prime_list = []
    i = 2
    while 1:
        is_prime = 1
        for j in prime_list:
            if i % j == 0:
                is_prime = 0
                i += 1
                break
        if is_prime == 1:
            prime_list.append(i)
        if len(prime_list) == n:
            break
    return prime_list

t = int(input().strip())
num_list = []
for i in range(t):
    num_list.append(int(input().strip()))

prime_list = find_prime(max(num_list))        
result = []
for i in num_list:
    result.append(str(prime_list[i - 1]))
    
print('\n'.join(result))
