from Visualizer import *

g = Grid.getRandomGrid()
#r = Robby.getRandomRobby()
r = Robby.getRobbyFromFile('generations/generation-1-robot-best.txt')
g.setRobby(r)
r.setGrid(g)

a = Alien(g)
