#Task: Update Pokemon class to include method that can change the name of a pokemon object

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

def main():
    jigglypuff = Pokemon("Jigglypuff", ["Normal"])
    jigglypuff.add_type("Fairy")
    jigglypuff.catch()
    jigglypuff.print_pokemon()

if __name__ == "__main__":
    main()
