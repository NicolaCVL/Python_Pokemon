import random, string, time, pypokedex

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

class Pokemon():
    max = 0

    def __init__(self, id):
        self.timeStart = time.time_ns()           
        self.pokemon = pypokedex.get(dex = id)
        self.spawnrate = random.randint(0,100)
        self.startSpawn = self.__class__.max
        self.__class__.max += self.spawnrate
        self.endSpawn = self.__class__.max

    def __repr__(self):
        return self.pokemon.name


if __name__ == "__main__" :
    sum = 0
    test = {}
    result = {}
    for i in range (1, 100):
        test[i] = Pokemon(i)
        print(test[i].pokemon.name)
        sum += test[i].spawnrate
        result[test[i].pokemon.name] = 0
    
    for i in test:
         print("le pokémon : ", test[i].pokemon.name, "  a une chance de spawn de : ", "{:.2f}".format(test[i].spawnrate/(test[i].max/100)), "%")

    for i in range(10000):
        spawn = random.randint(1, test[1].max)
        for i in test:
            if spawn >= test[i].startSpawn and spawn < test[i].endSpawn:
                # print("le pokemon est spawn: ", test[i].pokemon.name, "   et son taux de spawn est:  ", test[i].spawnrate, "%")
                result[test[i].pokemon.name] += 1
                break
    
    for i in result:
        print("pokémon: ", i, "  quantité:  ", result[i], "pourcentage: ", "{:.2f}".format(result[i]/100))



        
