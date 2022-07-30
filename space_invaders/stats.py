import os
from constants import *


class Stats:
    """Counts lives and scores"""

    def __init__(self):
        """Initiate stats"""
        self.guns_left = 2
        self.run_game = True
        self.score = 0
        if not os.path.exists(HIGHSCORE_FILE):
            self.high_score = self.score
            with open(HIGHSCORE_FILE, 'w') as high_score:
                high_score.write(f"{self.high_score}\n")
        else:
            with open(HIGHSCORE_FILE) as high_score:
                self.high_score = int(high_score.readline())
