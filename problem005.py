#!/bin/python3

#fractional decomposition function
def factorization(n):
    i = 2
    factors = {}
    while i <= n ** 0.5:
        if n % i == 0:
            fact1 = factorization(i)
            fact2 = factorization(n / i)
            for j in fact2:
                if j in fact1:
                    fact1[j] += fact2[j]
                else:
                    fact1[j] = fact2[j]
            factors = fact1
            break
        i += 1
    if len(factors) == 0:
        factors = {int(n):1}
    
    return factors
    

def find_smallest_multiple(n):
    factor_dict = {}
    for i in range(1, n + 1):
        fact1 = factorization(i)
        for j in fact1:
            if j in factor_dict:
                factor_dict[j] = max(factor_dict[j], fact1[j])
            else:
                factor_dict[j] = fact1[j]
    
    smallest_multiple = 1
    for i in factor_dict:
        smallest_multiple = smallest_multiple * pow(i, factor_dict[i])
        
    return smallest_multiple


result = []
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result.append(str(find_smallest_multiple(n)))
    
print('\n'.join(result))
    
