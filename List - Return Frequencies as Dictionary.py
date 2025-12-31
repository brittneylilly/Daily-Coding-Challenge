'''
Given a list of integers, return a dictionary with the frequency of each integer in the list,
with the integer as the key and its frequency as the value

Input: list
Output: dictionary
Edgecases
# if list is empty: return empty dictionary

Plan:
initialize an empty dictionary
For loop through the list
at each iteration, if the num is not in the dictionary add it and set its value to 1
if the num is already in the dictionary, increase its value by 1
return dictionary
'''

def count_occurrences(nums):
    dict = {}
    for num in nums:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num]+=1
    return dict

#testcases
nums = [1, 2, 2, 3, 3, 3, 4]
print(count_occurrences(nums)) #return {1: 1, 2: 2, 3: 3, 4: 1}

nums = []
print(count_occurrences(nums)) #return {}
