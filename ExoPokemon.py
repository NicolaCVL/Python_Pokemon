import random, string, time, pypokedex, keyboard

# Different array for my Pokemon inventory and My Inventory
myPokemonInventory = [{'name' : "ouisticram",'Attack' : 35,'Defense' : 20, 'CapacitéSpé' : "Flamméche"}]

myBackPackInventory = [
    {
        'name' : "pokeball",
        'catchrate' : 30,
        'price' : 200,
        'count' : 20
    },
    {
        'name' : "superball",
        'catchrate' : 50,
        'price' : 600,
        'count' : 10
    },
    {
        'name' : "hyperball",
        'catchrate' : 70,
        'price' : 1200,
        'count' : 5
    },
    {
        'name' : "masterball",
        'catchrate' : 100,
        'price' : 50000,
        'count' : 1  
    },
    {
        'name' : "Pokedollars",
        'Money' : 10000,
    }
]

# Different print methods
def mainMenuPrint():
    print("----------------------------------------")
    print("                                        ")
    print("  Bienvenue dans le monde des Pokemons !")
    print("                                        ")
    print("        1- Mes Pokemons  2- Mon Sac     ")
    print("                                        ")
    print("        3- Combattre     4-  Exit       ")
    print("                                        ")
    print("----------------------------------------")
def pokemonSpawnPrint(name):
    print("----------------------------------------")
    print("                                        ")
    print("    Un ",name," sauvage est apparu !    ")
    print("                                        ")
    print("    1- Attaquer  2- Capturer            ")
    print("    3- Pokeshop  4-  Fuir               ")
    print("----------------------------------------")
def shopPrint():
    print("-----------------------------------")
    print("-                                 -")
    print("-         1- Pokeball : 200$      -")
    print("-         2- Superball : 600$     -")
    print("-         3- Hyperball : 1200$    -")
    print("-         4- Masterball : 50.000$ -")
    print("-         5- Back                 -")
    print("-                                 -")
    print("-----------------------------------")
def choixPokeballPrint():
    print("-----------------------------------")
    print("-                                 -")
    print("-   1- Pokeball    2- Superball   -")
    print("-                                 -")
    print("-   3- Hyperball   4- Masterball  -")
    print("-                                 -")
    print("-----------------------------------")
def successfullCatchPrint(name):
    print("-----------------------------------")
    print("-                                 -")
    print("-    Vous avez capturé",name,"!   -")
    print("-                                 -")
    print("-----------------------------------")
def welcomePokeShop():
    print("-----------------------------------")
    print("                                  -")
    print("    Bienvenue dans le PokeShop !  -")
    print("                                  -")
    print("-----------------------------------")
def combatPrint():
    print("-----------------------------------")
    print("-                                 -")
    print("- 1-",myPokemonInventory[0]["CapacitéSpé"], "2- Back -")
    print("-                                 -")
    print("-----------------------------------")
def laFuite():
    print("-----------------------------------")
    print("                                  -")
    print("    Vous avez pris la fuite !     -")
    print("                                  -")
    print("-----------------------------------")

# Main Menu for my PokemonGame
def mainMenu(name):
    mainMenuPrint()
    while True:
            input1 = int(input())
            if  input1 == 1:
                print(myPokemonInventory)
                break
            elif input1 == 2:
                print(myBackPackInventory)
                break
            elif input1 == 3:
                lePokemonSpawn(name)
            elif input1 == 4:
                exit()
    mainMenu(name)

# Method to Spawn a pokemon
def lePokemonSpawn(name): 
    pokemonSpawnPrint(name)
    while True:
            input1 = int(input())
            if  input1 == 1:
                attack(name)
            elif input1 == 2:
                capture(name)
            elif input1 == 3:
                welcomePokeShop()
                shop(name)
            elif input1 == 4:
                laFuite()
                mainMenu(name)

# Method for my pokemon combats
def attack(name):
    poke = Pokemon(1)
    newPokemon = [
        {
            'name' : name,
            'Attack' : poke.pokemonAttack,
            'Defense' : poke.pokemonDefense,
            'CapacitéSpé' : "Charge"
        }
    ]
    ratio1 = int(myPokemonInventory[0]['Attack']/myPokemonInventory[0]['Defense'])
    ratio2 = int(newPokemon[0]['Attack']/newPokemon[0]['Defense'])
    max_number = ratio1 + ratio2 
    winRate = int(random.randint(0, max_number))
    moneyLoss = random.randint(1, 500)
    moneyGain = random.randint(1, 2000)
    
    while True:
        combatPrint()
        input2 = int(input())
        if input2 == 1:
            if winRate <= ratio1:
                print(myPokemonInventory[0]['name'],"Attaque", myPokemonInventory[0]['CapacitéSpé'],"!")
                print(myPokemonInventory[0]['name'], "a gagné le combat !")
                print(newPokemon[0]['name'], "adverse est tombé KO !")
                myBackPackInventory[4]['Money'] += moneyGain
                print("Vous avez gagné", moneyGain, "pokedollars !")
                mainMenu(name)
            else:
                print(myPokemonInventory[0]['name'], "est KO !")
                myBackPackInventory[4]['Money'] -= moneyLoss
                print("Vous avez perdu", moneyLoss, "pokedollars...")
                mainMenu(name)
        else:
            print(myPokemonInventory[0]['name'],"Reviens !")
            mainMenu(name)
            
# Capture method
def capture(name):
    poke = Pokemon(1)
    print(myPokemonInventory)
    choixPokeballPrint()
    newPokemon = [
        {
            'name' : name,
            'Attack' : poke.pokemonAttack,
            'Defense' : poke.pokemonDefense
        }
    ]
    while True:
        input3 = int(input())
        myBackPackInventory[input3-1]['count'] -=1
        a = random.randint(1, 100)
        if myBackPackInventory[input3-1]['count'] >= 1:
            if input3 == 4:
                captureReussiePrint(name)
                myPokemonInventory.append(newPokemon[0])
                lePokemonSpawn(name)
            elif (myBackPackInventory[input3-1]['catchrate']/(1+(poke.resistancerate/100))) >= a:
                captureReussiePrint(name)
                myPokemonInventory.append(newPokemon[0])
                lePokemonSpawn(name)
            else:
                print("Raté ! ")
                capture(name)

# Method for a pokeshop to buy pokeballs
def shop(name):
    shopPrint()
    input2 = int(input())
    if input2 == 5:
        mainMenu(name)
    else: 
        quantity = int(input(" T'en veux combien ? "))
        count = quantity*myBackPackInventory[input2-1]['price']
        if count > myBackPackInventory[4]['Money']:
            print("T'as pas d'argent MEC !")
            lePokemonSpawn(name)
        else:
            print("Vous avez acheter ",quantity, myBackPackInventory[input2-1]['name'],"!")
            myBackPackInventory[input2-1]['count'] += quantity
            print("Il vous reste ", myBackPackInventory[4]['Money'] - count)
            myBackPackInventory[4]['Money'] -= count
            shop(name)

# Class pokemon pokedex library
class Pokemon():
    max = 0
    def __init__(self, id):
        self.timeStart = time.time_ns()           
        self.pokemon = pypokedex.get(dex = id)
        self.spawnrate = random.randint(0,100)
        self.resistancerate = random.randint(0,50)
        self.pokemonAttack = random.randint(10, 50)
        self.pokemonDefense = random.randint(10, 50)
        self.startSpawn = self.__class__.max
        self.__class__.max += self.spawnrate
        self.endSpawn = self.__class__.max
    def __repr__(self):
        return self.pokemon.name
if __name__ == "__main__" :
    sum = 0
    test = {}
    result = {}
    for i in range (1, 15):
        test[i] = Pokemon(i)
        # print(test[i].pokemon.name)
        sum += test[i].spawnrate
        result[test[i].pokemon.name] = 0
    
    """for i in test:
        print("le pokémon : ", test[i].pokemon.name, "  a une chance de spawn de : ", "{:.2f}".format(test[i].spawnrate/(test[i].max/10)), "%")"""

    for i in range(1):
        spawn = random.randint(1, test[1].max)
        for i in test:
            if spawn >= test[i].startSpawn and spawn < test[i].endSpawn:
                # print("le pokemon est spawn: ", test[i].pokemon.name, "   et son taux de spawn est:  ", test[i].spawnrate, "%")
                result[test[i].pokemon.name] += 10
                break
        for i in result:
            if result[i] != 0:
                #print("pokémon: ", i, "  quantité:  ", result[i], "pourcentage: ", "{:.2f}".format(result[i]/100))
                mainMenu(i)




        









    


