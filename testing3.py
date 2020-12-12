#!/usr/bin/env python3
"""
exercise1 file including game start
"""
# Importing needed modules
import othello_testing3
import datetime
import time
import argparse

if __name__ == '__main__':
    """
    Initiating game play
    """
    for i in [False]:
        for j in range(0,15):
            cur_tim = time.time()
            game = othello_testing3.start_game(i, False, 6)
            game.play()
            end_time = time.time()
            x = ",{},{},{},{},{},test3\n".format(i, j+1, 6, datetime.datetime.now(), end_time - cur_tim )
            with open("test_results3.txt", "a") as f:
                f.write(x)
    # DEBUG MAIN (END)
