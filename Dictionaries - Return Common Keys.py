'''
Task: Write a function that takes in two dictionaries dict1 and dict2 
and finds all keys common to both dictionaries. 
The function returns a list of common keys.

Input: two dictionaries
Output: list containing common keys

Questions:
-If a key is the same letter but different cases, are they the same?
-Are the dictionaries always the same length? no

'''

def common_keys(dict1, dict2):
	result_lst = []
	for key1 in dict1:
		if key1 in dict2:
			result_lst.append(key1)
	return result_lst		

#testcases
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
print(common_keys(dict1, dict2)) #return ["b", "c"]

#empty dictionary
dict1 = {}
dict2 = {"a": 4, "c": 5, "d":6}
print(common_keys(dict1, dict2)) #return []
