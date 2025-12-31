'''
Write a function that takes in a list of integers numbers 
and an integer threshold as parameters and returns the number of items in numbers that are less than threshold.

Input: a list of integers
Output: an integer

Questions
? is the list sorted? No

Edgecases
# numbers is empty list: return 0
# if no numbers are less than threshold: return 0

#Plan:
initialize count variable and set equal to 0
For loop through the list
at each iteration check if list item is less than threshold
if so, increase count by 1
return count

'''

def count_less_than(numbers, threshold):
    count = 0
    for num in numbers:
        if num < threshold:
            count+=1
    return count


#testcases
numbers = []
threshold = 5
print(count_less_than(numbers, threshold)) #return 0

numbers = [12,8,2,4,4,10]
counter = count_less_than(numbers,5)
print(counter)

numbers = [12,8,10]
counter = count_less_than(numbers,5)
print(counter)
