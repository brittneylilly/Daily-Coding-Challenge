'''
Task: Write a function that takes in a parameter list and returns a new list of the doubled numbers.
'''

def doubled(lst):
    result = []
    for elem in lst:
        result.append(elem*2)
    return result


#testcases
lst = [1,2,3]
new_lst = doubled(lst)
print(new_lst) #return [2,4,6]

lst = []
new_lst = doubled(lst)
print(new_lst) #return []
