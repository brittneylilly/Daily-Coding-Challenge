'''
Task: Given an array of integers called requests, return an array of the indices in requests who's array values are greater than both its neighbors

Pseudocode:
#edgecases: need at least 3 elements in array to have a spike
if length of array < 3: return []

#maincase: if a value is greater than than both its neighbors, record its index as a spike
create new result array

start at index 1
and keep looping while index + 1 is still in bounds

stop for loop at second to last index:
for i in range(start, stop, step)
for i in range(1, len(requests) -1, 1)

if requests[i] > requests [i-1] and requests[i] > requests [i+1]:
requests.append(i)

return result array
'''

def spike(requests):
    #edgecases: need at least 3 elements in array to have a spike
    if len(requests) < 3:
        return []

    #maincase: if a value is greater than than both its neighbors, record its index as a spike
    result = []

    for i in range(1, len(requests) -1):
        if requests[i] > requests [i-1] and requests[i] > requests [i+1]:
            result.append(i)

    return result

requests = [1, 5, 2, 7, 3, 8, 4]
print(spike(requests)) #return [1, 3, 5]
