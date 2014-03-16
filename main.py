from God import *

print('hello ..')

start_time = time.time()

g = God()
g.initialize_first_generation()
g.applyEvolution()

print time.time() - start_time, "seconds"

print('bye ..')
