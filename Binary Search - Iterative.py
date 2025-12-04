'''
Task: return the index of the target value using iterative approach

Input: array of integers, target integer value
Output: integer value of index

Questions:
Is the list only integers? yes
Can target be a non integer? no

Edgecases:
# if list is empty --> return -1
# if target not in list --> return -1

Plan:
initialize a variable called index_of_target to -1
return this variable if the list is empty
initialize a left pointer at index 0
initialize a right pointer at the last index, length of array - 1
calculate the middle value between these two left and right values, and floor it so that it's a whole number. Store in variable called middle_index
ask is the middle number equal to the target value.
if it is equal to the target value, get the index of that value and return it
if it is not equal:
    ask is middle value greater than target
        if yes, move right pointer to the index at middle index - 1
	ask is middle value less than target
        if yes, move left pointer to the index at middle index + 1

repeat until target's index is found or until the entire list is searched as indicated by when the two pointer meet at the same index. 
(once the pointers pass each other, we've searched the whole list)

return the value of index
'''

def binary_search_iterative(arr, target):
	index_of_target = -1
	left= 0
	right = len(arr) - 1
	while left <= right:
		middle_index = (left + right)//2
		if arr[middle_index] == target:
			return middle_index
		elif arr[middle_index] > target:
			right = middle_index -1
		else:
			left = middle_index + 1
	return index_of_target


#testcases
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11
print(binary_search_iterative(arr, target)) #return 5

arr = [1, 3]
target = 1
print(binary_search_iterative(arr, target)) #return 0

arr = [1, 3]
target = 11
print(binary_search_iterative(arr, target)) #return -1

arr = []
target = 11
print(binary_search_iterative(arr, target)) #return -1
