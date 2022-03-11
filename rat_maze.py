
"""
TODO: test code with multiple input files - including no solution files (HIGH )

TODO: make input a required argument
TODO: move maze_solver to logic package
TODO: write_outfile function - default argument vs input argument
TODO: clean up code and modules, further organize

TODO: write README.md file (HIGH )
TODO: write docstrings (MEDIUM )
TODO: comment code (MEDIUM )

TODO: record video walkthrough (HIGH )

TODO: DFS (Optional - Low Priority)
"""

from helpers.argument_parser import ArgumentParser as ap
from helpers.file_ops import FileOps
from maze_solver import MazeSolver

#  python mazesolver.py -i inputfile -o outputfile

if __name__ == "__main__": 

    arguments = ap.take_input()
    
    # file_path = "input/input1.txt"
    # file = fo.read_file(file_path)
    # # print(file)
    
    # matrix = fo.create_matrix(file) 

    # # print(matrix)

    # start, end = ms.get_start_and_end(matrix)
    # path = ms.bfs_maze_solver(start, end, matrix)
    # outfile = 

    # print(path)
    # fo.write_output_file(matrix, path)


    