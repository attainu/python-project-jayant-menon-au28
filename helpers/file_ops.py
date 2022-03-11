class FileOps:
    """
    1. access file in input dir 
    2. create a matrix from the input
    3. solve (done)
    4. print outfile 
    """
    def read_file(file_path):
        """docstring"""
        with open(file_path, "r") as file:
            return file.readlines() 
        
    def create_matrix(lines):
        """docstring"""
        matrix = []
        for i in lines:
            i = i.replace("\n", "")
            i = i.replace(" ", "")
            row = list(map(int, i))
            matrix.append(row)
        return matrix

    def write_output_file(maze, path):
        """docstring"""
        if path == -1:
            with open("output/solution.txt", "w") as file:
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

        with open("output/solution.txt", "w") as file:
            file.writelines(string)

if __name__ == "__main__":
    maze = [[1, 0, 0, 0], [1, 1, 1, 0], [0, 1, 1, 0], [0, 0, 1, 1]]    
    solution = [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3)]
    FileOps.write_output_file(maze, solution)