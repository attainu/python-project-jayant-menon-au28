
"""
TODO: test code with multiple input files - including no solution files (HIGH )
TODO: DFS (Optional - Low Priority)
TODO: write docstrings (MEDIUM )
TODO: comment code (MEDIUM )


TODO: write README.md file (HIGH )

TODO: record video walkthrough (HIGH )
"""

from helpers.argument_parser import ArgumentParser as ap
from helpers.file_ops import FileOps
from maze_solver.maze_solver import MazeSolver

def main():
    in_path, out_path = ap.take_input()
    infile = FileOps.read_file(in_path)

    matrix = MazeSolver.create_matrix(infile) 
    start, end = MazeSolver.get_start_and_end(matrix)
    solved_maze = MazeSolver.bfs_maze_solver(start, end, matrix)

    FileOps.write_output_file(matrix, solved_maze, out_path)


if __name__ == "__main__": 
    main()
