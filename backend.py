#sudoku backend data loader
import csv
import math
import random

class Backend():
    def __init__(self):
        self.puzzle = []
        self.name = None

    #creates a puzzle from scratch
    def create(self):
        pass

    #loads the puzzle from a file
    def load(self, path):
        with open(path) as csvfile:
            self.puzzle = list(csv.reader(csvfile))[:9]
            
        h = path.split("\\")[-1]
        self.name = h.removesuffix(".csv")

    #saves a puzzle or solution to a file
    def save(self, puz=True):
        if(puz):
            with open("sudoku_puzzles/"+self.name+".csv",'w') as csvfile:
                csv.writer(csvfile).writerows(self.puzzle)
        else:
            with open("sudoku_puzzles/"+self.name+".csv",'w') as csvfile:
                csv.writer(csvfile).writerows(self.puzzle)

    #solves the puzzle using the given algorithm
    def solve(self, sol="opt"):
        if(sol == "opt"):
            pass

        if(sol == "force"):
            x,y = 0
            solve_puzzle = copy.deepcopy(self.puzzle)
            cont = True
            stack = []
            
                    
                
            
                        

    #checks the puzzle to make sure there are no errors
    def check_square(self, val, val_col, val_row, puzzle):
        check = True
        if(val == "0"):
            return False
        
        #checks the row that the value is in
        row = puzzle[val_row]
        row[val_col] = "0"
        for i in row:
            if(i == val):
                check = False
        row[val_col] = val

        #checks the column
        puzzle[val_row][val_col] = "0"
        for row in puzzle:
            if(row[val_col] == val):
                check = False       

        puzzle[val_row][val_col] = val

        #checks the block that the value is in
        block_y = math.floor(val_col/3)
        block_x = math.floor(val_row/3)

        puzzle[val_row][val_col] = "0"

        for i in range(block_y*3,block_y*3+3):
            for j in range(block_x*3,block_x*3+3):
                if(puzzle[j][i] == val):
                    check = False

        puzzle[val_row][val_col] = val

        return check

    #formats the puzzle for the command line
    def __str__(self):
        out = ""
        for k,i in enumerate(self.puzzle):
            for x,j in enumerate(i):
                out += j + " "
                if(x == 2 or x == 5):
                    out += "| "
            out += "\n"
            if(k == 2 or k == 5):
                out += "- "*11 + "\n"
        return out
