#!/usr/bin/env python3
"""
exercise1 file including game start
"""
# Importing needed modules
import othello_testing
import datetime
import time
import argparse

if __name__ == '__main__':
    """
    Initiating game play
    """
    for i in [True, False]:
        for j in range(0,250):
            cur_tim = time.time()
            game = othello_testing.start_game(i, False, 4)
            game.play()
            end_time = time.time()
            x = ",{},{},{},{},{}\n".format(i, j+1, 4, datetime.datetime.now(), end_time - cur_tim )
            with open("test_results.txt", "a") as f:
                f.write(x)
    # DEBUG MAIN (END)
