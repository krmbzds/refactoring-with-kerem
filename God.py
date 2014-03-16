import time
from Generation import *
from Parameters import *


class God:
    generation = None

    def initializeFirstGeneration(self):
        self.generation = Generation(0)

    def applyEvolution(self):
        for i in range(NUM_GENERATIONS):
            self.generation, normalizedScore, bestScore = self.generation.applyEvolution()
            print(str(normalizedScore) + ',' + str(bestScore))
            with open('results.txt', 'a') as file:
                file.write(str(normalizedScore) + ',' + str(bestScore) + '\n')
