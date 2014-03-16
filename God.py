import time
from Generation import *
from Parameters import *


class God:
    generation = None

    def initialize_first_generation(self):
        self.generation = Generation(0)

    def apply_evolution(self):
        for i in range(NUM_GENERATIONS):
            self.generation, normalized_score, best_score = self.generation.apply_evolution()
            print(str(normalized_score) + ',' + str(best_score))
            with open('results.txt', 'a') as file:
                file.write(str(normalized_score) + ',' + str(best_score) + '\n')
