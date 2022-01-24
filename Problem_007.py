# Euler Problem 007
# Solved January 2021

# 10001st prime
# Using Sieve of Eratosthenes
MAX_PRIME = 2000000
A = [True]*(MAX_PRIME+1)
count = 0
for i in range(2, int(MAX_PRIME**(1/2)+1)):
    if A[i]:
        j = i**2
        #print(i)
        while j <= MAX_PRIME:
            A[j] = False
            j += i
for i in range(2, MAX_PRIME):
    if A[i]:
        count = count + 1
        if count == 10001:
            print(i)
            break

