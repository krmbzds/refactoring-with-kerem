import random
from enum import *
from Parameters import *


def get_index(current, north, east, south, west):
    return current + 3 * north + 3**2 * east + 3**3 * south + 3**4 * west


def get_random_move_action():
    temp = [ACTIONS.MOVE_NORTH, ACTIONS.MOVE_EAST, ACTIONS.MOVE_SOUTH, ACTIONS.MOVE_WEST]
    return random.choice(temp)


def get_random_action():
    temp = [ACTIONS.MOVE_NORTH, ACTIONS.MOVE_EAST, ACTIONS.MOVE_SOUTH, ACTIONS.MOVE_WEST, ACTIONS.MOVE_RANDOM, ACTIONS.STAY_PUT, ACTIONS.PICK_UP_CAN]
    return random.choice(temp)


class Robby:
    gene = []  # length should be 3^5
    grid = None
    position_r = 1
    position_c = 1
    move_count = 0

    def __init__(self, gene):
        self.gene = gene

    def set_grid(self, grid):
        self.grid = grid

    def clean(self):
        self.grid = None
        self.position_r = 1
        self.position_c = 1
        self.move_count = 0

    def get_r(self):
        return self.position_r

    def get_c(self):
        return self.position_c

    @staticmethod
    def get_random_robby():
        r_val, actions = [], list(range(7))
        for i in range(243):
            r_val.append(random.choice(actions))
        return Robby(r_val)

    @staticmethod
    def get_robby_from_file(file_name):
        file = open(file_name, "r")
        str_arr = file.read().split(',')
        int_arr = map(int, str_arr)
        return Robby(int_arr)

    def move_direction(self, current, north, east, south, west, action):
        score = 0

        if action == ACTIONS.MOVE_NORTH:
            if north == OBSTACLES.WALL:
                score -= 5
            else:
                self.position_r -= 1
        elif action == ACTIONS.MOVE_EAST:
            if east == OBSTACLES.WALL:
                score -= 5
            else:
                self.position_c += 1
        elif action == ACTIONS.MOVE_SOUTH:
            if south == OBSTACLES.WALL:
                score -= 5
            else:
                self.position_r += 1
        elif action == ACTIONS.MOVE_WEST:
            if west == OBSTACLES.WALL:
                score -= 5
            else:
                self.position_c -= 1

        return score

    def get_next_action(self):

        current = self.grid[self.position_r][self.position_c]
        north = self.grid[self.position_r-1][self.position_c]
        east = self.grid[self.position_r][self.position_c+1]
        south = self.grid[self.position_r+1][self.position_c]
        west = self.grid[self.position_r][self.position_c-1]

        # your code goes here... (TODO #1)
        # return the next action using
        # current, north, east, south, west and self.gene

        return action

    def move(self):
        score = 0
        self.move_count += 1

        action = self.get_next_action()

        current = self.grid[self.position_r][self.position_c]
        north = self.grid[self.position_r-1][self.position_c]
        east = self.grid[self.position_r][self.position_c+1]
        south = self.grid[self.position_r+1][self.position_c]
        west = self.grid[self.position_r][self.position_c-1]

        if action == ACTIONS.MOVE_NORTH or action == ACTIONS.MOVE_EAST or action == ACTIONS.MOVE_SOUTH or action == ACTIONS.MOVE_WEST:
            score = self.move_direction(current, north, east, south, west, action)
        elif action == ACTIONS.MOVE_RANDOM:
            score = self.move_direction(current, north, east, south, west, get_random_move_action())
        elif action == ACTIONS.STAY_PUT:
            pass
        elif action == ACTIONS.PICK_UP_CAN:
            if current == OBSTACLES.EMPTY:
                score -= 1
            elif current == OBSTACLES.CAN:
                score += 10
                self.grid.pickup_can(self.position_r, self.position_c)

        return score

    def mutate(self, gene):

        # your code goes here ... (TODO #3)
        # mutate the input variable gene
        # using MUTATION_PROBABILITY

        gene = mutatedGene

    def give_birth(self, other_robot):
        i = random.randint(0, 244)
        r1a, r1b = self.gene[:i], self.gene[i:]
        r2a, r2b = other_robot.gene[:i], other_robot.gene[i:]
        robot1 = r1a + r2b
        robot2 = r2a + r1b

        return [robot1, robot2]

    def save(self, file_name):
        outfile = open(file_name, "w")
        outfile.write(','.join(str(number) for number in self.gene))
