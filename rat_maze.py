
"""
TODO: test code with multiple input files - including no solution files (HIGH )


TODO: move maze_solver to logic package
TODO: write_outfile function - default argument vs input argument
TODO: clean up code and modules, further organize

TODO: write README.md file (HIGH )
TODO: write docstrings (MEDIUM )
TODO: comment code (MEDIUM )

TODO: record video walkthrough (HIGH )

TODO: DFS (Optional - Low Priority)

# python mazesolver.py -i inputfile -o outputfile
"""

from helpers.argument_parser import ArgumentParser as ap
from helpers.file_ops import FileOps
from maze_solver import MazeSolver

if __name__ == "__main__": 

    arguments = ap.take_input()
    print(arguments)

    file_path = arguments.inputfile
    file = FileOps.read_file(file_path)
    # # print(file)
    
    matrix = FileOps.create_matrix(file) 

    # # print(matrix)

    start, end = MazeSolver.get_start_and_end(matrix)
    path = MazeSolver.bfs_maze_solver(start, end, matrix)
    FileOps.write_output_file(matrix, path)

    # print(path)



    