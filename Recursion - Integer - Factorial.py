'''
Task: return the factorial of the given parameter n using recursion
The factorial is n x n-1 x n-2 x ..... x 1

Input: a non-negative integer n
Output: an integer
Edgecases:
if n = 0 --> return 1 bc 0! = !

Constraints on time complexity and memory

1. param integer n
2. n is non-negative, so lowest it can be is 0
3. integer
4. n * n-1 * n-2....1
5. recursive case
'''
def factorial(n):
    #base case
    if n == 1 or n==0:
        return 1

    #recursive case
    return n * factorial(n-1)


#test cases:
#happy case
print(factorial(5)) #return 6
print(factorial(2)) # return 2
print(factorial(1)) # return 1
# Edgecases:
print(factorial(0)) #return 1 # if n = 0 --> return 1 bc 0! = !
