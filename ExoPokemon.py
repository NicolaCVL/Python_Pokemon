import random, string, time, pypokedex, keyboard

# 1 - créer une liste des pokémons, incluant une chance de spawn (0% - 100%) 
# 2 - créer une méthode spwan, qui, en fonction de la chance de spawn, fait spawn un pokémon (affiche son nom)
# 3 - faire spawn 10000 pokémons, calculer le % de chaque pokémon spawn
# 4 - comparer le % de spawn avec la chance de spawn du pokémon. Afficher pour chaque pokémon spawn,
# s'il y en a eu + ou - que la proba de spawn initiale
# bonus: créer des pokeballs avec des chances de captures, notamment les spécialdes en fonction du type de pokémon, et pourquoi pas du biome dans lequel on se trouve
# double bonus: faire des combats avec les pokemon capturé histoire de pouvoir baisser les pdv et augmenter les chances de captures

pokeball = [
    {
        'name' : "pokeball",
        'catchrate' : 30

    },
    {
        'name' : "superball",
        'catchrate' : 50
        
    },
    {
        'name' : "hyperball",
        'catchrate' : 70
        
    },
    {
        'name' : "masterball",
        'catchrate' : 100
        
    }
]

def lePokemonSpawn(name): 
    print("----------------------------------------")
    print("                                        ")
    print("    Un ",name," sauvage est apparu !    ")
    print("                                        ")
    print("    1- Attaquer  2- Capturer  3- Fuir   ")
    print("                                        ")
    print("----------------------------------------")

    while True:
            input1 = int(input())
            if  input1 == 1:
                capture(name)
                break
            elif input1 == 2:
                print("-----------------------------------")
                print("                                  -")
                print("          Vous avez fui !         -")
                print("                                  -")
                print("-----------------------------------")
                break

def capture(name):
      
        print("-----------------------------------")
        print("-                                 -")
        print("-   1- Pokeball    2- Superball   -")
        print("-                                 -")
        print("-   3- Hyperball   4- Masterball  -")
        print("-                                 -")
        print("-----------------------------------")

        while True:
            input3 = int(input())
            poke = Pokemon(1)
            a = random.randint(1, 100)
            if input3 == 4:
                print("-----------------------------------")
                print("-                                 -")
                print("-    Vous avez capturé",name,"!   -")
                print("-                                 -")
                print("-----------------------------------")
                break
            if (pokeball[input3-1]['catchrate']/(1+(poke.resistancerate/100))) >= a:
                print("-----------------------------------")
                print("-                                 -")
                print("-    Vous avez capturé",name,"!   -")
                print("-                                 -")
                print("-----------------------------------")
                break
            else:
                print("Raté ! ")
                capture(name)
            
            
class Pokemon():
    max = 0

    def __init__(self, id):
        self.timeStart = time.time_ns()           
        self.pokemon = pypokedex.get(dex = id)
        self.spawnrate = random.randint(0,100)
        self.resistancerate = random.randint(0,50)
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
                lePokemonSpawn(i)




        









    


