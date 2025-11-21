#Task: given a list of pokemon objects and a target type, return a list of object names with that type.

class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   
            "types": self.types, 
            "is_caught": self.is_caught 
        })

    def catch(self):
        self.is_caught = True
    
    def choose(self):
        if self.is_caught == True:
            print(self.name + " I choose you!")
        print(self.name + " is wild! Catch them if you can!")

    def add_type(self, new_type):
        self.types = new_type
'''
IOEC
Input: list of objects' name parameter, a "type" parameter
Output: a list of the objects' names whose "type" matches that of the parameter
Edgecases: 
#Empty input list --> return []
#No type in list matches pokemon_type --> return []
Constraints on time and memory complexity: none

Plan - will be used to comment my code
create an empty results list
loop through my_pokemon 
at each iteration, get it's .types value and compare it to pokemon_type
if the types match, add the pokemon to the results list
return the results list

Pseudocode 
# create an empty results list
# loop through my_pokemon 
# at each iteration, get it's .types value and compare it to pokemon_type
# if the types match, add the pokemon to the results list
# return the results list


'''
def get_by_type(my_pokemon, pokemon_type):
    # create an empty results list
    result = []

    # loop through my_pokemon 
    # at each iteration, get it's .types value and store it in a variable
    # check if the pokemon_type is in the .types list
    # if the types match, add the pokemon to the results list

    for i in my_pokemon:
       types_list = i.types
       if pokemon_type in types_list:
           result.append(i.name)

     # return the results list
    return result
   

#TESTCASES:

#happy case:
# initializing pokemons
jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])

my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
print(get_by_type(my_pokemon, "Normal")) #return: [jigglypuff, meowth, pidgeot]

# #Edgecases: 

# #Empty input list --> return []
my_pokemon2 = []
print(get_by_type(my_pokemon2, "Normal")) #return: []

# #No type in list matches pokemon_type --> return []
jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])

my_pokemon3 = [jigglypuff, diglett, meowth, pidgeot, blastoise]
print(get_by_type(my_pokemon3, "Jabbawoki")) #return: []
