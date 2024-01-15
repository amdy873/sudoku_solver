#sudoku backend data loader
import csv

class Backend():
    def __init__(self):
        self.puzzle = []
        self.name = None

    def create(self):
        pass

    def load(self, path):
        with open(path) as csvfile:
            self.puzzle = list(csv.reader(csvfile))[:9]
            
        h = path.split("\\")[-1]
        self.name = h.removesuffix(".csv")

    def solve(self, sol="opt"):
        if(sol == "opt"):
            pass

        if(sol == "force"):
            pass

    def save(self):
        with open("sudoku_puzzles/"+self.name+".csv",'w') as csvfile:
            csv.writer(csvfile).writerows(self.puzzle)

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
