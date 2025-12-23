'''
Task: Write a function that takes in a sorted list of integers nums as a parameter and 
removes all duplicates in the list. The function returns the modified list.

Given a sorted input list that contains integers,
the list may or may not contain duplicates,
but 

Input: sorted list containting integers
Output: list with no duplicates

Edgecases:
#if list contains no duplicates, return same list
#if list is empty return list
#only 1 item in list, return that list

Question:
-Return the list in place or a new list? return the list in place
'''

def remove_duplicates(nums):
    if not nums:
        return []
    
    left = 0
    right = 1

    while right < len(nums):
        if nums[left] == nums[right]:
            nums.pop(right)
            #if they are equal, left stays at 0 and right stays at 1
        #if they are not equal, move the pointers by 1    
        else:
            left+=1
            right+=1

    return nums


#testcases:
nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums)) #return [1,2,3,4,5,6]

#empty list
nums = []
print(remove_duplicates(nums)) #return[]
