from Visualizer import *

g = Grid.get_random_grid()
#r = Robby.get_random_robby()
r = Robby.get_robby_from_file('generations/generation-1-robot-best.txt')
g.set_robby(r)
r.set_grid(g)

a = Alien(g)
