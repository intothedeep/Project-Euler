#!/bin/python3

#transform formula such as (1+2+3+...+n)**2 - (1**2+2**2+3**2+..n**2) = 2*(n((n-1)+(n-2)+...+1)+(n-1)*((n-2)+(n-3)+...1)+...2*1) = n**2*(n-1)+...+2**2*1
def square_diff(n):
    sum = 0
    for i in range(n, 1, -1):
        sum += i * i * (i - 1)
    return sum

result = []

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result.append(str(square_diff(n)))

print('\n'.join(result))
