import tkinter as tk

class Game:
    def __init__(self, board, root):
        self.board = board
        self.queen = tk.PhotoImage(file="my_queen.png")
        self.solution = []
        self.board_size = [[0 for i in range(8)] for j in range(8)]
        # --------------------------------------------------------------------------
        self.root = root
        self.sols = 0
        self.display_solutions = False
        # -----------------------------------------------------------------------
        self.init = tk.Button(self.board, text="Inicio", fg = 'yellow', bg = 'grey', font = ('Verdana', 16), command=self.one_solution)
        self.init.place(x=650, y=100)

        self.re_init = tk.Button(self.board, text="Reinicio", fg = 'yellow', bg = 'grey', font = ('Verdana', 16), command=self.one_solution)
        self.re_init.place(x=635, y=155)

        self.sol = tk.Button(self.board, text="Soluciones", fg = 'yellow', bg = 'grey', font = ('Verdana', 16), command=self.solutions)
        self.sol.place(x=621, y=210)

        self.label = tk.Label(self.board, text="")
        self.label.place(x=650, y=260)

    def isSafe(self, board, row, column):
        for i in range(len(board)):
            if board[row][i] == 1:
                return False
        for i in range(len(board)):
            if board[i][column] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(column, len(board))):
            if board[i][j] == 1:
                return False
        return True

    def solve(self, board, row):
        if row >= len(board) and self.display_solutions is True:
            self.solution.append(board)
            self.printboard(board)
            return
        elif row >= len(board) and self.display_solutions is False:
            self.sols += 1
            self.label.configure(text=(str(self.sols) + "º Solución encontrada"))
            return

        for i in range(len(board)):
            if self.isSafe(board, row, i):
                board[row][i] = 1
                if not self.display_solutions:
                    self.board.addpiece(name="a"+str(i), image=self.queen, row=row, column=i)
                    self.root.update()
                    self.root.after(100, self.solve(board, row + 1))
                else:
                    self.root.after(40, self.solve(board, row + 1))
                board[row][i] = 0
        return False

    def printboard(self, board):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    self.board.addpiece(name="a" + str(i), image=self.queen, row=i, column=j)
                    self.root.update()
                else:
                    print(".", end=" ")
            print()
        self.sols += 1
        self.label.configure(text=("Soluciones " + str(self.sols)))
        for widget in self.board.winfo_children():
            print(widget)

    def solutions(self):
        self.label.configure(text=(""))
        self.board.remove_images()
        self.sols = 0
        if not self.display_solutions:
            self.display_solutions = True
            self.solve(self.board_size,0)

    def one_solution(self):
        self.display_solutions = False
        self.label.configure(text=(""))
        self.board.remove_images()
        self.sols = 0
        self.solve(self.board_size, 0)




