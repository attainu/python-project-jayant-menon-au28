class MazeSolver:
    """
    A class that contains the maze solving logic and helper functions
    """
    def is_valid_location(location, maze):
        """checks if the coordinates are valid to move to"""
        rows = len(maze)
        columns = len(maze[0])
        (x, y) = location
        if x >= 0 and x < columns and y >= 0 and y < rows and maze[x][y] != 0:
            return True
        return False

    def bfs_maze_solver(start, end, maze):
        """solves the maze using a breadth first approach"""
        queue = []
        visited = set()   

        queue.append((start, []))
        
        while queue:
            ((x, y), path) = queue.pop(0)
            cur_path = path + [(x ,y)] 
            visited.add((x, y))
            if (x, y) == end:
                return cur_path
            
            neighbors = {
                "up" : (x, y-1),
                "down" : (x, y+1),
                "left" : (x-1, y),
                "right" : (x+1, y)
            }
            for v in neighbors.values():
                if v not in visited and MazeSolver.is_valid_location(v, maze): 
                    queue.append((v, cur_path))
        return -1

    def dfs_maze_solver(start, end, maze):
        """solves the maze using a depth first approach"""
        stack = []
        visited = set()

        stack.append((start, []))

        while stack:
            ((x, y), path) = stack.pop(-1)
            cur_path = path + [(x, y)]
            visited.add((x, y))
            if (x, y) == end:
                return cur_path

            neighbors = {
                "up" : (x, y-1),
                "down" : (x, y+1),
                "left" : (x-1, y),
                "right" : (x+1, y)
            }
            for v in neighbors.values():
                if v not in visited and MazeSolver.is_valid_location(v, maze):
                    stack.append((v, cur_path))
        return -1

    def solve_maze(start, end, maze, algo):
        """calls the appropriate method as per user input"""
        if algo.lower() == "dfs":
            return MazeSolver.dfs_maze_solver(start, end, maze)
        else:
            return MazeSolver.bfs_maze_solver(start, end, maze)

    def print_path(path, maze):
        """prints the solved path to console"""
        solved_maze = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
        
        for location in path:
            x, y = location
            solved_maze[x][y] = 1
        
        for i in range(len(maze)):
            print(*solved_maze[i])