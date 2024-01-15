#sudoku solver main

from backend import Backend


backend = Backend()

backend.load("sudoku_puzzles\sudoku1.csv")

backend.solve(sol="force")
