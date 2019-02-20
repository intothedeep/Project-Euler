#!/bin/python3

#suppose a<b<c, then a<n/3. a**2 = c**2-b**2 = (c-b)(c+b) = (c-b)(n-a)
def find_biggest_pythagorean_set(n):
    pt_set = []
    for a in range(n // 3, 1, -1):
        if (a ** 2) % (n - a) == 0:
            k = (a ** 2) / (n - a)
            if (n - a - k) % 2 == 0:
                b = (n - a - k) / 2
                c = (n - a + k) / 2
                pt_set.append(int(a * b * c))
    if len(pt_set) == 0:
        return -1
    else:
        return max(pt_set)
    
num = []
t = int(input().strip())
for a0 in range(t):
    num.append(int(input().strip()))

pyth_result = []
for i in range(max(num)):
    pyth_result.append(find_biggest_pythagorean_set(i + 1))

for n in num:
    print(pyth_result[n - 1])
