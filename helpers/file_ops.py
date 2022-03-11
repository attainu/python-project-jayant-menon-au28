class FileOps:
    """
    docstring
    """
    def read_file(file_path):
        """docstring"""
        with open(file_path, "r") as file:
            return file.readlines() 

    def write_output_file(maze, path, outfile):
        """docstring"""
        if path == -1:
            with open(f"{outfile}", "w") as file:
                file.write("-1")
            return

        solved_maze = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
        for location in path:
            x, y = location
            solved_maze[x][y] = 1

        string = ""
        for row in solved_maze:
            for digit in row:
                string += str(digit) + " "
            string += '\n'

        with open(f"{outfile}", "w") as file:
            file.writelines(string)
