#Task: A pokemon object has an instance variable called evolution that can be None or 
#another pokemon object. Write a function that takes in a pokemon object and returns
#a list containing that object's name and the subsequent names of evolution objects

class Pokemon():
	def  __init__(self, name, types, evolution = None):
		self.name = name
		self.types = types
		self.is_caught = False
		self.evolution = evolution
 
'''

IOEC
Input: a pokemon object's .name as a list
Output: a list of successive pokemon .name values
Edgecases: 
# no objects in starter_pokemon --> return []
Constraints on time complexity and memory? No


Plan:
# create an empty result list
# add the first pokemon object's name to the result list
# loop through the list of pokemon objects while each objects evolution is not none
# access the .evolution of each object 
# if it is not equal to none,
# 	get the .name of that object and add it to the result list
# else
# 	return the result list
'''

def get_evolutionary_line(starter_pokemon):
	# create an empty result list
	result = []

	#edgecase were starter_pokemon is empty
	if starter_pokemon is None:
		return result

	#add the first pokemon object's name to the result list
	result.append(starter_pokemon.name)
	
	# loop through the list of pokemon objects while each objects evolution is not none
	# append the .evolution.name of each object to the result list
	# and store the evolution object it in the starter_pokemon variable


	while starter_pokemon.evolution is not None:
		result.append(starter_pokemon.evolution.name)
		starter_pokemon = starter_pokemon.evolution 
	
	# return the result list
	return result

##Testcases

#happycase:
charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)
nothing = Pokemon(None, None, None)

charmander_list = get_evolutionary_line(charmander)
print(charmander_list) #--> ["Charmander", "Charmeleon", "Charizard"]

charmeleon_list = get_evolutionary_line(charmeleon)
print(charmeleon_list) #--> ["Charmeleon", "Charizard"]

charizard_list = get_evolutionary_line(charizard)
print(charizard_list) # --> ["Charizard"]

nothing_list= get_evolutionary_line(nothing)
print(nothing_list) #--> []
