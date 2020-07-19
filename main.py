import tkinter as tk
from screen import GameBoard
from game import Game

if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(width=False, height=False)
    root.title("Las Ocho Reinas")
    root.geometry("800x600")

    board = GameBoard(root)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)

    game = Game(board, root)

    root.mainloop()
