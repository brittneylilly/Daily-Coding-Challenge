'''
Task: add together all elements in a list and return the sum recursively

IOEC
Input: list
Output: integer value that is the sum of all items in the list
Edgecases: 
# list is empty --> return 0
# list only has 1 value --> return that value
# 0 is the only value in the list --> return 0
# list has negative numbers, ensure sum is correct


Questions
# can values in the list be negative? yes
# is the list only integers? can it be decimals? can it be strings etc? No its only integers

Constraints on time complexity and memory? none


Match: recursion w list problem. make list smaller and smaller

1. parameter is a list
2. values can be negative, values are all integers
3. output is an integer
4. what to do to get the answer if i were doing it iteratively:
get the first value in the list and store it in sum. then take second value in list and add to sum. repeat til 
list is empty.
5. write recursive case

'''
def sum_list(lst):
    
    #base case
    if lst == []:
        return 0

    #recursive case:
    return lst[0] + sum_list(lst[1:])

#test cases
#happy cases
lst = [1, 2, 3, 4, 5]
print(sum_list(lst)) #return 15

#edgecases: 
lst = []
print(sum_list(lst)) #return 0


lst = [1]
print(sum_list(lst)) #return 1


lst = [0]
print(sum_list(lst)) #return 0


lst = [1, 2, -3, 4, 5]
print(sum_list(lst)) #return 9

#Time complexity: linear O(n) because the number of function calls is directly proportionate to the number of items in the list. 
#Space (memory usage) Complexity: linear O(n) bc the recursive memory stack grows with each recursive call, as each time a frame is added to
#the memory stack. frames are only popped from the stack once the basecase is reached.
