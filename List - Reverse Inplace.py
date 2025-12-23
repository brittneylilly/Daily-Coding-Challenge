'''
Task: Reverse the list in place using the two pointer technique

Edgecases: 
#if the list is empty, return empty list
#if the list has 1 element, return same list
'''

def reverse_list(lst):
    if len(lst) < 2:
        return lst
    
    left = 0
    right = len(lst) - 1

    while left <= right:
        temp = lst[left]
        lst[left] = lst[right]
        lst[right] = temp
        left += 1
        right -= 1

    return lst
        
   
#testcases
lst = [1, 2, 3, 4, 5]
print(reverse_list(lst)) #return [5, 4, 3, 2, 1]

lst = []
print(reverse_list(lst)) #return []

lst = [5]
print(reverse_list(lst)) #return [5]

lst = [4,7]
print(reverse_list(lst)) #return [7,4]
