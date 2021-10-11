import random 
from collections import Counter

def spawn(name, percent,):
    randomNumber = random.randint(0,100)
    if randomNumber <= percent:
        return listOfSpawnedPokemon.append(name)
    else:
        #listeOfSpawnedPokemon.append(0)
        randomGetIndex= random.randint(0, len(pokemon)-1)
        spawn(pokemon[randomGetIndex].get('name'), pokemon[randomGetIndex].get('percent'))

randomNumber = 0
randomGetIndex = 0
listOfSpawnedPokemon = []
    
pokemon = [
    {
        "name":"Pikachu",
        "percent":10,
        "counter":0

    },

    {
        "name":"Aspiscot",
        "percent":60,
        "counter":0

    },

    {
        "name":"MiniDraco",
        "percent":2,
        "counter":0

    },

    {
        "name":"Carapuce",
        "percent":5,
        "counter":0

    },

    {
        "name":"Salamèche",
        "percent":5,
        "counter":0

    },

    {
        "name":"Bulbizarre",
        "percent":5,
        "counter":0

    },

    {
        "name":"Ratatac",
        "percent":80,
        "counter":0

    },

    {
        "name":"Lixy",
        "percent":30,
        "counter":0

    },

    {
        "name":"Onyx",
        "percent":30,
        "counter":0

    },

    {
        "name":"Chenipan",
        "percent":75,
        "counter":0

    },
    
    {
        "name":"Mewtwo",
        "percent":0.5,
        "counter":0

    },
]
    
for i in range (0, 10000):
    randomGetIndex = random.randint(0, len(pokemon)-1)
    spawn(pokemon[randomGetIndex].get('name'),pokemon[randomGetIndex].get('percent'))
    
countNbOfPokemons = Counter(listOfSpawnedPokemon)
print(countNbOfPokemons)

for element in countNbOfPokemons:
    print(countNbOfPokemons[element])
    print((countNbOfPokemons[element]/10000)*100)
# formule proba 

"""


"""
# totalSpawnLoops= 10000
#print(listOfSpawnedPokemon)
#print(pokemon[randomGetIndex].get('counter'))

# def spawnProba (nbOfTimesPokemonSpawned):
#     nbOfTimesPokemonSpawned = pokemon[Counter].get([1]) // totalSpawnLoops
#     return nbOfTimesPokemonSpawned

# print(spawnProba)


