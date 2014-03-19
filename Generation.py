import os
from Parameters import *
from MultipleSessions import *
from Robby import *
import random


class Generation:
    robots = []
    num_stay_put = 0

    def __init__(self, id, robots=None):
        self.id = id

        if robots is None:
            for i in range(POPULATION_SIZE):
                self.robots.append(Robby.get_random_robby())
        else:
            self.robots = robots

    @staticmethod
    def get_roulette_wheel_selection(size):
        return 200 - (int((2 * random.randint(1, size + 1)) ** 0.5))

    def get_score(self):
        r_val = 0.0
        for i in range(len(self.robots)):
            m = MultipleSessions(self.robots[i])
            r_val = r_val + m.run()
        return r_val / len(self.robots)

    def apply_evolution(self):
        tuples = []
        total_score = 0.0

        MultipleSessions.refresh_grids()
        for i in range(len(self.robots)):
            m = MultipleSessions(self.robots[i])
            score = m.run()
            total_score = total_score + score
            tuples.append((self.robots[i], score))

        tuples.sort(key=lambda x: x[1], reverse=True)
        normalized_score = total_score / len(self.robots)
        best_score = tuples[0][1]

        child_robots = []
        roulette_size = (POPULATION_SIZE * (POPULATION_SIZE + 1) / 2)

        for i in range(POPULATION_SIZE / 2):
            parent_1 = tuples[self.get_roulette_wheel_selection(roulette_size)][0]
            parent_2 = tuples[self.get_roulette_wheel_selection(roulette_size)][0]
            child_1, child_2 = parent_1.give_birth(parent_2)
            child_robots.append(child_1)
            child_robots.append(child_2)

        self.num_stay_put = child_1.gene.count(5) + child_2.gene.count(5)

        return Generation(self.id + 1, child_robots), normalized_score, best_score
