#!/bin/python3

#sieve of Eratosthenes
def prime_list_less(n):
    if n >= 2:
        prime_list = [2]
    else:
        prime_list = []
        
    candidate = {}
    for i in range(int((n - 1) / 2)):
        cur = 2 * i + 3
        if cur not in candidate.keys():
            candidate[cur] = 1
            prime_list.append(cur)
            k = 1
            while cur * (2 * k + 1) <= n:
                candidate[cur * (2 * k + 1)] = 0
                k += 1
    
    return prime_list

max_num = 1000000
num = {}
t = int(input().strip())
for i in range(t):
    num[i] = int(input().strip())
    
num = sorted(num.items(), key=lambda kv: kv[1])

prime_list = prime_list_less(max_num)
result = {}
idx = 0
sum = 0
for kv in num:
    while prime_list[idx] <= kv[1]:
        sum += prime_list[idx]
        idx += 1
    result[kv[0]] = sum

for i in range(t):
    print(result[i])
    
