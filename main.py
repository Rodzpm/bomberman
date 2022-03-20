from game import Game

def run(case):
    #lancer le jeu
    jeu = Game(case)
    jeu.run()

if __name__ == "__main__" :
    run((25,13))

