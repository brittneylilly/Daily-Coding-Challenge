#Task: Given an array of integers, keep a count of frequency that the value at index i+1 is less than the value at index i, then return frequency

'''
Pseudocode
# #edgecase: if scores is empty, return 0 because there are no numbers to compare

# #edgecase: if only 1 element in the array, there's no value to i+1 to compare to, so would get an index out of bounds,
# so return 0

#main case
set a counter to start at i= 0 to track momentum drops. the counter represents the current index
start while loop at i=0 and keep looping as long as i+1 is less than len(scores); this ensures
we don't go out of bounds and stops once we've compare the last 2 elements in the array
if the value at index i+1 is less than the value at index i, the increase the counter by 1
compare the value at index i and the value is index i+1
else: increment i by 1 to move to the next element in the array
'''
def momentum(scores):
    #edgecase: must have at least 2 elements to compare
    if len(scores) < 2:
        return 0
    
    #main case: increase momentum counter when next value is less than current value at index
    momentum_counter = 0
    i = 0
    while i+1 < len(scores):
        if scores[i+1] < scores[i]:
            momentum_counter += 1
        i+=1

    return momentum_counter

scores = [5, 5, 5, 5]
print(momentum(scores)) 
