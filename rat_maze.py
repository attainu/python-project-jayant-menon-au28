from helpers.argument_parser import ArgumentParser as ap
from helpers.file_ops import FileOps
from helpers.matrix import Matrix
from maze_solver.maze_solver import MazeSolver

def main():
    in_path, out_path, algo = ap.take_input()
    infile = FileOps.read_file(in_path)

    matrix = Matrix.create_matrix(infile) 
    start, end = Matrix.get_start_and_end(matrix)
    solved_maze = MazeSolver.solve_maze(start, end, matrix, algo)
    
    FileOps.write_out_file(matrix, solved_maze, out_path)

if __name__ == "__main__": 
    main()