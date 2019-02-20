#!/bin/python3

def is_plaindrome(n):
    is_palind = 1
    n = list(str(n))
    if len(n) == 6:
        for i in range(len(n) // 2):
            if n[i] != n[len(n) - i - 1]:
                return 0
        return is_palind

#calculate palindromes which is the product of two 3-digit numbers in advance
palindrome_compound = []
for i in range(100, 1000):
    for j in range(i, 1000):
        if is_plaindrome(i * j) == 1:
            palindrome_compound.append(i * j)

result = []

t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    while n > 100000:
        n -= 1
        if n in palindrome_compound:
            result.append(str(n))
            break
            
print('\n'.join(result))
