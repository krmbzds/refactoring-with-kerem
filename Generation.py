import os
from Parameters import *
from MultipleSessions import *
from Robby import *
import random


class Generation:
    robots = []

    def __init__(self, id, robots=None):
        self.id = id
        if robots is None:
            for i in range(POPULATION_SIZE):
                self.robots.append(Robby.get_random_robby())
        else:
            self.robots = robots

    def get_roulette_wheel_selection(self, count):

        # your code goes here ... (TODO #4)
        # return a number between [0, count-1]
        # search for roulette wheel selection on google.

        return 0

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
        # your code goes here ... (TODO #5)
        # fill the child_robots array with POPULATION_SIZE children
        # using get_roulette_wheel_selection() and Robby.give_birth()

        return Generation(self.id + 1, child_robots), normalized_score, best_score
