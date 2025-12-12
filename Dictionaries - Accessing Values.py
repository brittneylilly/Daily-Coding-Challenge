'''
Task:
Given a dictionary that stores votes for
presidential candidates. As a candidate is voted
for their name is automatically added to the dictionary as the key
and the number of votes cast for them as the value.

You are given as parameters, the current status of the dictionary.
Update the dictionary with the new candidate vote passed into the parameter.

If the candidate is already in the dictionary, increase their vote count by 1
if the candidate is not in the dictionary, add them and make their vote count = 1

Input: a dictionary, a candidates name as a string
Output: updated dictionary

Edgecases:
# if the dictionary is currently empty --> it will return {candidate name: 1}

Plan:
if candidate not in votes, 
add candidate to votes and set value to 1
else if candidate in votes
increase value +1
return votes

'''

def cast_vote(votes, candidate):
    if candidate not in votes:
        votes[candidate] = 1
    else:
        votes[candidate] += 1
    return votes


#testcases
votes = {'Alice': 5, 'Bob': 3}
candidate = 'Alice'
print(cast_vote(votes, candidate)) #return {'Alice': 6, 'Bob': 3}

votes = {'Alice': 5, 'Bob':3}
candidate = 'Gina'
print(cast_vote(votes, candidate)) #return {'Alice': 5, 'Bob': 3, 'Gina': 1}

votes = {}
candidate = 'Gina'
print(cast_vote(votes, candidate)) #return {'Gina': 1}
