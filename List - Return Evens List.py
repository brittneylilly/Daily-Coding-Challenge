'''
Write a function that takes in a list of integers lst as a parameter
and returns a list of all even numbers in the list.

Input: list of integers
Output: list of even numbers only

Question:
# Is 0 considered even? Yes

Edgecases:
# list is empty: return empty list
# list has no even numbers: return empty list []
# list has the number 0 and no other even numbers: return empty list [0]

See if i can reverse the list in place. 

Plan:
initialize new list
For loop through list,
at each iteration check if number is divisible by 2 w/o a remainder
if it is, add it to the new list
return the new list

'''

def get_evens(lst):
    result = []
    for num in lst:
        if num%2==0:
            result.append(num)
    return result



#testcases
lst = [1, 2, 3, 4]
print(get_evens(lst)) #return 2,4

lst = [2, 4]
print(get_evens(lst))

lst = [1, 3]
print(get_evens(lst))

lst = [0]
print(get_evens(lst))

lst = []
print(get_evens(lst))

lst = [1, 0, 3]
print(get_evens(lst))

#Time Complexity: O(n) Linear
#Space Complexity: O(n) Linear

