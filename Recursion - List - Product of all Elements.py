'''
#Task: Given a list of integers, write a recursive algorithm to return the product of all the integers
in the list. If the list is empty, return 1.

Input: a list of integers
Output: integer value (the result of all elements in the list when multiplied
together)

Edgecases:
# if the list is empty --> return 1 bc in coding the product of no elements is typically considered 1
# if the list is one number --> return just that number
# if there's one 0 in the list --> return 0
# if there are negative values

##Questions
# Will it ever pass in a list of non-numbers? No
# Will the list contain only integers? Yes
# Can the list contain negative integers? Yes

Constraints in time and space complexity? No

#My recursion steps
1. what are the parameter(s): a list
2. What other mathematical info am i given? none
3. What output do I return: an integer value
4. What do I need to do to get the answer?
[5, 9, 2, 3]

lst[0] x lst[1] x lst[2] x lst[4]
'''

def list_product(lst):
	#basecase(s)
    if not lst:
        return 1

    #recursive case
    return lst[0] * list_product(lst[1:])


#testcases
lst = [1, 2, 3, 4, 5]
print(list_product(lst)) #return 120


lst = []
print(list_product(lst)) #return 1


lst = [1]
print(list_product(lst)) #return 1

lst = [5]
print(list_product(lst)) #return 5

lst = [0]
print(list_product(lst)) #return 0


lst = [5, 0, 7]
print(list_product(lst)) #return 0


lst = [5, -3]
print(list_product(lst)) #return -15

lst = [-5, -3, 1]
print(list_product(lst)) #return 15
