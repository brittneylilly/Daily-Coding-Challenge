'''
Task: Given an array bins and an integer position:
Return bins[position] - bins[last]
If position is out of bounds (negative or too large), return -1
If array is empty, return -1
'''

'''
Given = inputs
where = definitions
return = output

IOEQC

Input: an array of integers called bins; 
Input2: an integer called position that represents the an index
Output: an integer that is the result of array[position] - array[-1]

Edgecases:
#if the array is empty, there's no numbers to compare, return -1
#if position parameter is less than 0, or greater than the length of the array -1, index is out of bounds so return -1
#if there is only one element in the array, the difference between the same number is 0, so the code needs to return 0

Questions:
? Can i assume that if positions is negative it is invalid? yes

Constraints on time and space complexity? N/A
'''

'''
Pseudo code:
def funciton (bins, position):
    if length of bins is less than 1:
        return -1
    if position is less than 0 or greater than lenght of bins -1:
        return -1
    return bins[position] - bins[-1]

'''

def inventory(bins, position):
    #edge case: if the array is empty, there's no numbers to compare, return -1
    if len(bins) < 1:
        return -1
    #edge case: if position parameter is less than 0, 
    #or greater than the length of the array -1, index is out of bounds so return -1
    elif position < 0 or position > len(bins)-1:
        return -1
    #main logic: return difference between integer and position index and integer at last item in array
    else:
        return bins[position] - bins[-1]

bins = [10, 20, 30, 40, 50]
position = 2
print(inventory(bins, position))
#return -20
