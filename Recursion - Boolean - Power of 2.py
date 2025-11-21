#Task: given an integer n as a parameter, determine if it is a power of 2. n = 2^x, where x is an integer
'''
IOEC:
Input: integer n, determine if n is a power of 2
Output: Boolean true/false. return True if n is a power of 2. False otherwise
Edgecases: n is 0 or less. bc the smallest integer value that is a power of 2 is 1
Constraints on time complexity and memory? no

1) integer n
2) 2^x = n, when x is an integer
3) a boolean true or false
4) i need to keep dividing by 2 and checking if that result is an even number, if so keep going til the result is 1
'''
def is_power_of_two(n):
    #base cases:
    if n == 1:
        return True
    
    if n < 1:
        return False

    #recursive case:
    return n % 2 == 0 and is_power_of_two(n/2)
    
    
    #n%2==0 is the universal test for checking if a number is even. if a number has no remainder when divded by 2 then it is even

#test cases:
print(is_power_of_two(16)) #return True
print(is_power_of_two(1)) #return True
print(is_power_of_two(12)) #return False

#edgecases
print(is_power_of_two(0)) #return False
print(is_power_of_two(-1)) #return False
