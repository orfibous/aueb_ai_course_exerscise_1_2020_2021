from tkinter import *
import time
from tkinter import ttk

import board
import othello

class Viz:
    def __init__(self):
        self.root = Tk()
        self.root.title("Othello")
        self.root.iconbitmap("tkinterData/icon.ico")
        self.screen = Canvas(self.root, width=500, height=500, background="#353535", highlightthickness=0)
        self.screen.pack(expand=YES, fill=BOTH)
        self.screen.delete("highlight")
        self.screen.delete("tile")
        for rows in range(0, 8):
            for columns in range(0, 8):
                self.screen.create_oval(54 + 50 * rows, 54 + 50 * columns, 96 + 50 * rows, 96 + 50 * columns,
                                        tags="tile {0}-{1}".format(rows, columns),
                                        fill="#aaa", outline="#aaa")
                if rows == 0:
                    ln = [1, 2, 3, 4, 5, 6, 7, 8]
                    self.screen.create_text(54 - 15 + 50 * rows, 54 + 21 + 50 * columns, fill="white", font="Times 20 "
                                                                                                            "bold",
                                            text=ln[columns])
                if rows == 7:
                    ln = [1, 2, 3, 4, 5, 6, 7, 8]
                    self.screen.create_text(96 + 15 + 50 * rows, 54 + 21 + 50 * columns, fill="white", font="Times 20 "
                                                                                                            "bold",
                                            text=ln[columns])
                if columns == 0:
                    ll = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
                    self.screen.create_text((54 + 50 * rows) + 21, (54 - 20 + 50 * columns), fill="white",
                                            font="Times 20 bold", text=ll[rows])
                if columns == 7:
                    ll = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
                    self.screen.create_text((54 + 50 * rows) + 21, 94 + 20 + 50 * columns,
                                            fill="white", font="Times 20 bold", text=ll[rows])
        self.screen.update()
        # self.popup("Are you read to play Othello?")
        time.sleep(5)

    def update_output(self, ls: list):
        for rows in range(0, 8):
            for columns in range(0, 8):
                if ls[rows][columns] == 'L':
                    self.screen.create_oval(54 + 50 * rows, 54 + 50 * columns, 96 + 50 * rows, 96 + 50 * columns,
                                            tags="tile {0}-{1}".format(rows, columns),
                                            fill="#fff", outline="#fff")
                elif ls[rows][columns] == 'D':
                    self.screen.create_oval(54 + 50 * rows, 54 + 50 * columns, 96 + 50 * rows, 96 + 50 * columns,
                                            tags="tile {0}-{1}".format(rows, columns),
                                            fill="#000000", outline="#000000")
                elif ls[rows][columns] == 'X':
                    self.screen.create_oval(70 + 50 * rows, 70 + 50 * columns, 80 + 50 * rows, 80 + 50 * columns,
                                            tags="tile {0}-{1}".format(rows, columns),
                                            fill="#ff0000", outline="#ff0000")
        self.screen.update()
        self.root.mainloop()
        time.sleep(3)

    def popup(self, msg):
        win = Toplevel()
        win.wm_title("Window")

        l = Label(win, text="Input")
        l.grid(row=0, column=0)

        b = ttk.Button(win, text="Okay", command=win.destroy)
        b.grid(row=1, column=0)


x = Viz()
brc = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', 'X', ' ', ' ', ' ', ' '],
                [' ', ' ', 'X', 'L', 'D', ' ', ' ', ' '],
                [' ', ' ', ' ', 'D', 'L', 'X', ' ', ' '],
                [' ', ' ', ' ', ' ', 'X', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

x.update_output(brc)
# game = othello.start_game(True, True, 3)
# game.play()
