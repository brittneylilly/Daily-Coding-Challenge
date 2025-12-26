'''
Task: Flip the sign of every integer in the list and return the list.

Plan: 
1. Instantiate a new empty result list
2. Iterate through the list with a for loop
3. Multiply each element by -1
4. Append the multiplied element to the new list


#Pseudo code
def function(lst)
    result_lst = empty list
    for every element in lst
        multiply by -1 and append to result_lst
    return result_lst
end
'''


def flip_sign(lst):
    result_lst = []

    for elem in lst:
        result_lst.append(elem * -1)
    return result_lst


#test cases
lst = [1, -2, -3, 4]
print(flip_sign(lst)) #return [-1, 2, 3 -4]

#edgecases:
#empty list:
lst=[]
print(flip_sign(lst))

lst=[0]
print(flip_sign(lst))


'''
Time Complexity: O(n) Linear
bc the loop essentially runs the same number of times as the input size, which is O(n);
and inside the loop the "worst case" time complexit for any operation is
O(1), since all the operations inside this loop are O(1).
So the time complexity = O(n) x O(1) = O(n)
'''
