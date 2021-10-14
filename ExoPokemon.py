import random, string, time, pypokedex, keyboard

# Different array for my Pokemon inventory and My Inventory
myPokemonInventory = [
    {
        'name' : "Ouisticram",
        'Attack' : 35,
        'Defense' : 20
    }
]

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
def mainMenuPrint():
    print("----------------------------------------")
    print("                                        ")
    print("  Bienvenue dans le monde des Pokemons !")
    print("                                        ")
    print("        1- My Pokemon  2- Mon Sac       ")
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
    print("    3- Pokeshop      4-  Fuir           ")
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
def captureReussiePrint(name):
    print("-----------------------------------")
    print("-                                 -")
    print("-    Vous avez capturé",name,"!   -")
    print("-                                 -")
    print("-----------------------------------")

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


def lePokemonSpawn(name): 
    pokemonSpawnPrint(name)
    while True:
            input1 = int(input())
            if  input1 == 1:
                attack(name)
            elif input1 == 2:
                capture(name)
            elif input1 == 3:
                print("-----------------------------------")
                print("                                  -")
                print("    Bienvenue dans le PokeShop !  -")
                print("                                  -")
                print("-----------------------------------")
                shop(name)
            elif input1 == 4:
                print("-----------------------------------")
                print("                                  -")
                print("    Vous avez pris la fuite !     -")
                print("                                  -")
                print("-----------------------------------")
                mainMenu(name)

def attack(name):
    poke = Pokemon(1)
    newPokemon = [
        {
            'name' : name,
            'Attack' : poke.pokemonAttack,
            'Defense' : poke.pokemonDefense
        }
    ]
    pokemonAttack = myPokemonInventory[0]['Attack'] 
    pokemonDefense = myPokemonInventory[0]['Defense']
    newPokemonAttack = newPokemon[0]['Attack']
    newPokemonDefense = newPokemon[0]['Defense']

    while True:
        print("-----------------------------------")
        print("-                                 -")
        print("-      1- Flammèche   2- Back     -")
        print("-                                 -")
        print("-----------------------------------")
        input2 = int(input())
        if input2 == 1:
            print(myPokemonInventory[0]['name'],"Attaque Flammèche !")
            ratio1 = int(pokemonAttack/pokemonDefense)
            ratio2 = int(newPokemonAttack/newPokemonDefense)
            max_number = ratio1 + ratio2 
            winRate = int(random.randint(0, max_number))
        elif input2 == 2:
            print(myPokemonInventory[0]['name'],"Reviens !")
            mainMenu(name)
            # lePokemonSpawn(myPokemonInventory[0]['name'])
            


def capture(name):
    poke = Pokemon(1)
    print(myPokemonInventory)
    print(poke.pokemonDefense)
    print(poke.pokemonAttack)
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
        myPokemonInventory.append(newPokemon[0])
        if myBackPackInventory[input3-1]['count'] >= 1:
            if input3 == 4:
                captureReussiePrint(name)
                newPokemon.append(poke)
                print(newPokemon)
                print(myPokemonInventory)
                mainMenu(name)
            elif (myBackPackInventory[input3-1]['catchrate']/(1+(poke.resistancerate/100))) >= a:
                captureReussiePrint(name)
                newPokemon.append(poke)
                mainMenu(name)
            else:
                print("Raté ! ")
                print(myBackPackInventory)
                capture(name)

    
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
            print("Il vous reste ", myBackPackInventory[4]['Money'] - count)
            shop(name)

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
    for i in range (1, 10):
        test[i] = Pokemon(i)
        print(test[i].pokemon.name)
        sum += test[i].spawnrate
        result[test[i].pokemon.name] = 0
    
    for i in test:
         print("le pokémon : ", test[i].pokemon.name, "  a une chance de spawn de : ", "{:.2f}".format(test[i].spawnrate/(test[i].max/10)), "%")

    for i in range(1):
        spawn = random.randint(1, test[1].max)
        for i in test:
            if spawn >= test[i].startSpawn and spawn < test[i].endSpawn:
                # print("le pokemon est spawn: ", test[i].pokemon.name, "   et son taux de spawn est:  ", test[i].spawnrate, "%")
                result[test[i].pokemon.name] += 1
                break
        for i in result:
            if result[i] != 0:
                #print("pokémon: ", i, "  quantité:  ", result[i], "pourcentage: ", "{:.2f}".format(result[i]/100))
                mainMenu(i)




        









    


