import random, string, time, pypokedex, keyboard

# 1 - créer une liste des pokémons, incluant une chance de spawn (0% - 100%) 
# 2 - créer une méthode spwan, qui, en fonction de la chance de spawn, fait spawn un pokémon (affiche son nom)
# 3 - faire spawn 10000 pokémons, calculer le % de chaque pokémon spawn
# 4 - comparer le % de spawn avec la chance de spawn du pokémon. Afficher pour chaque pokémon spawn,
# s'il y en a eu + ou - que la proba de spawn initiale
# bonus: créer des pokeballs avec des chances de captures, notamment les spécialdes en fonction du type de pokémon, et pourquoi pas du biome dans lequel on se trouve
# double bonus: faire des combats avec les pokemon capturé histoire de pouvoir baisser les pdv et augmenter les chances de captures

myPokemonInventory = [
    {
        'name' : "Ouisticram",
        'Attack' : 35,
        'Defense' : 20
    }
]

myInventory = [
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

def mainMenu(name):
    print("----------------------------------------")
    print("                                        ")
    print("  Bienvenue dans le monde des Pokemons !")
    print("                                        ")
    print("        1- My Pokemon  2- Mon Sac       ")
    print("                                        ")
    print("        3- Combattre     4-  Exit       ")
    print("                                        ")
    print("----------------------------------------")
    while True:
            input1 = int(input())
            if  input1 == 1:
                print(myPokemonInventory)
                break
            elif input1 == 2:
                print(myInventory)
                break
            elif input1 == 3:
                lePokemonSpawn(name)
            elif input1 == 4:
                exit
    mainMenu(name)


def lePokemonSpawn(name): 
    poke = Pokemon(i)
    print("----------------------------------------")
    print("                                        ")
    print("    Un ",name," sauvage est apparu !    ")
    print("                                        ")
    print("    1- Attaquer  2- Capturer            ")
    print("    3- Pokeshop      4-  Fuir           ")
    print("----------------------------------------")
    
    newPokemon = [
    {
        'name' : name,
        'Attack' : poke.pokemonAttack,
        'Defense' : poke.pokemonDefense
    }
]

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
                break

def attack(name):
    pokemonAttack = myPokemonInventory[0]['Attack'] 
    pokemonDefense = myPokemonInventory[0]['Defense']
    # newPokemonAttack = newPokemon[0]['Attack']
    # newPokemonDefense = newPokemon[0]['Defense']

    while True:
        poke = Pokemon(1)
        poke.pokemonAttack
        poke.pokemonDefense
        print("-----------------------------------")
        print("-                                 -")
        print("-   1- Charge    2- Flammèche     -")
        print("-                                 -")
        print("-   3- Double-Pied   4- Back      -")
        print("-                                 -")
        print("-----------------------------------")
        input2 = int(input())
        if input2 == 1:
            print(myPokemonInventory[0]['name'],"Attaque Charge !")
            ratio1 = int(pokemonAttack/pokemonDefense)
            ratio2 = int(newPokemonAttack/newPokemonDefense)
            max_number = ratio1 + ratio2 
            winRate = int(random.randint(0, max_number))

        elif input2 == 2:
            print(myPokemonInventory[0]['name'],"Attaque Flammèche !")
        elif input2 == 3:
            print(myPokemonInventory[0]['name'],"Attaque Double-Pied !")
        elif input2 == 4:
            print(myPokemonInventory[0]['name'],"Reviens !")
            lePokemonSpawn(myPokemonInventory[0]['name'])
            break


def capture(name):
    
    print("-----------------------------------")
    print("-                                 -")
    print("-   1- Pokeball    2- Superball   -")
    print("-                                 -")
    print("-   3- Hyperball   4- Masterball  -")
    print("-                                 -")
    print("-----------------------------------")
    poke = Pokemon(1)
    while True:
        input3 = int(input())
        myInventory[input3-1]['count'] -=1
        a = random.randint(1, 100)
        myPokemonInventory.append(poke)

        if myInventory[input3-1]['count'] >= 1:
            if input3 == 4:
                print("-----------------------------------")
                print("-                                 -")
                print("-    Vous avez capturé",name,"!   -")
                print("-                                 -")
                print("-----------------------------------")
                myPokemonInventory.append(poke)
                mainMenu(name)
            elif (myInventory[input3-1]['catchrate']/(1+(poke.resistancerate/100))) >= a:
                print("-----------------------------------")
                print("-                                 -")
                print("-    Vous avez capturé",name,"!   -")
                print("-                                 -")
                print("-----------------------------------")
                myPokemonInventory.append(newPokemon)
                mainMenu(name)
            else:
                print("Raté ! ")
                print(myInventory)
                capture(name)
                
def shop(name):
    count = 0
    while True:
        print("-----------------------------------")
        print("-                                 -")
        print("-         1- Pokeball : 200$      -")
        print("-         2- Superball : 600$     -")
        print("-         3- Hyperball : 1200$    -")
        print("-         4- Masterball : 50.000$ -")
        print("-         5- Back                 -")
        print("-                                 -")
        print("-----------------------------------")
        input2 = int(input())
# Modifier le while pour ne pas aller en Negatif !

        while myInventory[4]['Money'] != 0:
            if input2 == 5:
                mainMenu(name)
            if input2 == 1:

                input3 = int(input(" T'en veux combien sale rat ? "))
                count = input3*myInventory[input2-1]['price']
                
                myInventory[input2-1]['count'] += input3
                myInventory[4]['Money'] -= count 
                print("Vous avez acheter", input3,"pokeball !")
                print("Il vous reste ", myInventory[4]['Money'])
                break
                
            elif input2 == 2:

                input3 = int(input(" T'en veux combien ? "))
                count = input3*myInventory[input2-1]['price']
                
                myInventory[input2-1]['count'] += input3
                myInventory[4]['Money'] -= count 

                myInventory[input2-1]['count'] += input3
                myInventory[4]['Money'] -= count
                print("Vous avez acheter", input3, "superball ! ah bien !")
                print("Il vous reste ", myInventory[4]['Money'])
                break
            elif input2 == 3:
                input3 = int(input(" Bonjour Monsieur, Vous en voulez combien ? "))
                count = input3*myInventory[input2-1]['price']
                
                myInventory[input2-1]['count'] += input3
                myInventory[4]['Money'] -= count 

                myInventory[input2-1]['count'] +=input3
                myInventory[4]['Money'] -= count
                print("Vous avez acheter", input3, "hyperball !")
                print("Il vous reste ", myInventory[4]['Money'])
                break

            elif input2 == 4:

                input3 = int(input(" Bonjour Monsieur, Vous en voulez combien ? "))
                count = input3*myInventory[input2-1]['price']
                
                myInventory[input2-1]['count'] += input3
                myInventory[4]['Money'] -= count 

                myInventory[input2-1]['count'] += input3
                myInventory[4]['Money'] -= count
                print("Vous avez acheter", input3, "masterball ! waaah excusez moi MONSIEUR ! Vous avez de l'argent a ce que je vois !")
                print("Il vous reste ", myInventory[4]['Money'])
                break
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
                # lePokemonSpawn(i)




        









    


