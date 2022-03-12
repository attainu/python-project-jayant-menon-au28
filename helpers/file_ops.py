class FileOps:
    """
    A class to perform file operations 
    """
    def read_file(file_path):
        """reads input file and returns list of strings"""
        with open(file_path, "r") as file:
            return file.readlines() 

    def write_out_file(maze, path, outfile):
        """writes solved maze as outfile"""
        if path == -1:
            with open(f"{outfile}", "w") as file:
                file.write("-1")
            return

        solved_maze = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
        for location in path:
            x, y = location
            solved_maze[x][y] = 1

        lines = ""
        for row in solved_maze:
            for digit in row:
                lines += str(digit) + " "
            lines += '\n'

        with open(f"{outfile}", "w") as file:
            file.writelines(lines)