'''
Task: reverse the sign of the list inplace (without creating a new list)
'''
def reverse_sign(lst):
    left = 0

    while left < len(lst):
        temp = lst[left]
        lst[left] = temp * -1
        left +=1
    
    return lst

#testcases
lst = [-1, 3, 6, -9]
print(reverse_sign(lst)) #return [1, -3, -6, 9]

lst = []
print(reverse_sign(lst))

lst = [0]
print(reverse_sign(lst))

'''
Time Complexity: O(n) Linear
Bc the loop essentially runs the same number of times as the size of the list,
and the "worst" time complexity for operations inside the loop is O(1) 
(all the operations inside this loop were O(1))
So O(n) x O(1) = O(n)
'''
