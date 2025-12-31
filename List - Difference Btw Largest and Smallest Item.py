'''
Task: Write a function that takes in a list of integers lst 
and returns the difference between the smallest and largest value in the list.

Input: a list of integers
Output: an integer

Questions:
Is the list sorted? no
can the list contain negative integers? yes

Edgecases:
# if list is empty: return 0
# if list has 1 element: return 0
# if first and last element are the same: return 0
#make sure difference isn't negative, should always be positive number

Plan:
# use sort function on lst to sort in ascending order
# if the list if is empty or only 1 item, return 0
# get element at 0th index, and element at index len(lst)-1
# use a function to return their difference

Pseudocode:
# if length of list is 1 or less:
#     return 0
# sort list in place
# get the list's 0th element and store in variable first
# get list's last element at lenght of list - 1 and store in variable last
# take the difference of these two and store in variable difference
# return absolute value fuction with difference as parameter

'''

def max_difference(lst):
    # if length of list is 1 or less: return 0
    if len(lst) <= 1:
        return 0

    # sort list in place
    lst.sort()
   
    # get the list's 0th element and store in variable first
    first = lst[0]

    # get list's last element at lenght of list - 1 and store in variable last
    last = lst[len(lst)-1]

    # take the difference of these two and store in variable difference
    difference = first - last
    
    # return absolute value fuction with difference as parameter
    return abs(difference)

#testcases
lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)

# if list is empty: return 0
lst = []
max_diff = max_difference(lst)
print(max_diff)

# if list has 1 element: return 0
lst = [9]
max_diff = max_difference(lst)
print(max_diff)

# if first and last element are the same: return 0
lst = [2, 2]
max_diff = max_difference(lst)
print(max_diff)

#if the list if negative numbers. 
lst = [-5, -22, -8, -10, -2] #return 20
max_diff = max_difference(lst)
print(max_diff)
