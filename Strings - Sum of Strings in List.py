"""
Given a list of strings that are numbers, eg. "50",
turn the strings into integer values and add them up

Input: a list containing string elements
Output: an integer

Edgecases:
#list is empty: return 0
#list has 1 item: return item

Questions:
#Can the list contain negative numbers? No

Plan:
instantiate a sum variable and set equal to 0
iterate through the list, 
    casting each element to a char 
    and adding it to the sum
return sum

"""

def sum_of_number_strings(nums):
    sum = 0

    for elem in nums:
        sum += int(elem)
        
    return sum


#testcases
nums = ["10", "20", "30"]
print(sum_of_number_strings(nums)) #return 60

#Edgecases:
#list is empty: return 0
nums = []
print(sum_of_number_strings(nums)) #return 0

#list has 1 item: return item
nums = ["2"]
print(sum_of_number_strings(nums)) #return 2

