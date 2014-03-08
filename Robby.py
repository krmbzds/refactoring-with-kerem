import random
from enum import *
from Parameters import *

def getIndex(current, north, east, south, west):
	return current + 3 * north + 3**2 * east + 3**3 * south + 3**4 * west

def getRandomMoveAction()
	temp = [ACTIONS.MOVE_NORTH, ACTIONS.MOVE_EAST, ACTIONS.MOVE_SOUTH, ACTIONS.MOVE_WEST]
	return random.choice(temp)

def getRandomAction():
	temp = [ACTIONS.MOVE_NORTH, ACTIONS.MOVE_EAST, ACTIONS.MOVE_SOUTH, ACTIONS.MOVE_WEST, ACTIONS.MOVE_RANDOM, ACTIONS.STAY_PUT, ACTIONS.PICK_UP_CAN]
	return random.choice(temp)

class Robby:
	gene = [] # length should be 3^5
	grid = None
	positionR = 1
	positionC = 1
	moveCount = 0

	def __init__(self, gene):
		self.gene = gene

	def setGrid(self, grid):
		self.grid = grid	

	def clean(self):
		self.grid = None
		self.positionR = 1
		self.positionC = 1
		self.moveCount = 0

	def getR(self):
		return self.positionR

	def getC(self):
		return self.positionC

	@staticmethod
	def getRandomRobby():
		rVal = []
		
		# your code goes here ... (TODO #0)
		# fill the rVal array with random actions of length 3**5
		
		return Robby(rVal)
	
	@staticmethod
	def getRobbyFromFile(fileName):
		file = open(fileName, "r")
		strArr = file.read().split(',')
		intArr = map(int, strArr)
		return Robby(intArr)

	def moveDirection(self, current, north, east, south, west, action):
		score = 0

		if(action == ACTIONS.MOVE_NORTH):
			if(north == OBSTACLES.WALL):
				score = score - 5
			else:
				self.positionR = self.positionR - 1
		elif(action == ACTIONS.MOVE_EAST):
			if(east == OBSTACLES.WALL):
				score = score - 5		
			else:
				self.positionC = self.positionC + 1
		elif(action == ACTIONS.MOVE_SOUTH):
			if(south == OBSTACLES.WALL):
				score = score - 5
			else:
				self.positionR = self.positionR + 1
		elif(action == ACTIONS.MOVE_WEST):
			if(west == OBSTACLES.WALL):
				score = score - 5		
			else:
				self.positionC = self.positionC - 1

		return score

	def getNextAction(self):

		current = self.grid[self.positionR][self.positionC]
		north = self.grid[self.positionR-1][self.positionC]
		east = self.grid[self.positionR][self.positionC+1]
		south = self.grid[self.positionR+1][self.positionC]
		west = self.grid[self.positionR][self.positionC-1]
		
		# your code goes here... (TODO #1)
		# return the next action using
		# current, north, east, south, west and self.gene

		return action

	def move(self):
		score = 0
		self.moveCount = self.moveCount + 1

		action = self.getNextAction()		

		current = self.grid[self.positionR][self.positionC]
		north = self.grid[self.positionR-1][self.positionC]
		east = self.grid[self.positionR][self.positionC+1]
		south = self.grid[self.positionR+1][self.positionC]
		west = self.grid[self.positionR][self.positionC-1]

		if(action == ACTIONS.MOVE_NORTH or action == ACTIONS.MOVE_EAST or action == ACTIONS.MOVE_SOUTH or action == ACTIONS.MOVE_WEST):
			score = self.moveDirection(current, north, east, south, west, action)	
		elif(action == ACTIONS.MOVE_RANDOM):			
			score = self.moveDirection(current, north, east, south, west, getRandomMoveAction())			
		elif(action == ACTIONS.STAY_PUT):
			pass
		elif(action == ACTIONS.PICK_UP_CAN):
			if(current == OBSTACLES.EMPTY):
				score = score - 1 
			elif(current == OBSTACLES.CAN):
				score = score + 10
				self.grid.pickupCan(self.positionR, self.positionC)			

		return score
	
	def mutate(self, gene):
		
		# your code goes here ... (TODO #3)
		# mutate the input variable gene 
		# using MUTATION_PROBABILITY

		gene = mutatedGene

	def giveBirth(self, otherRobot):

		# your code goes here ... (TODO #2)
		# return two children robots in an array
		# using self.gene and otherRobot.gene and self.mutate()
		
		return [robot1, robot2]

	def save(self, fileName):
		outfile = open(fileName, "w")
		outfile.write(','.join(str(number) for number in self.gene))
