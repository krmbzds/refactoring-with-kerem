from Parameters import *
from Session import *
from Grid import *
import copy


class MultipleSessions:
    robby = None

    def __init__(self, robby):
        self.robby = robby
        if not hasattr(MultipleSessions, 'grids'):
            self.refresh_grids()

    @staticmethod
    def refresh_grids():
        MultipleSessions.grids = []
        for i in range(NUM_SESSIONS):
            grid = Grid.get_random_grid()
            MultipleSessions.grids.append(grid)

    def run(self):
        total_score = 0.0
        for grid in MultipleSessions.grids:
            session = Session(self.robby, copy.deepcopy(grid))
            score = session.run()
            self.robby.clean()
            total_score = total_score + score
        return total_score / len(MultipleSessions.grids)
