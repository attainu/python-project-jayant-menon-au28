class MazeSolver:
    """
    docstring
    """
    def get_start_and_end(matrix):
        return (0,0), (len(matrix[0])-1, len(matrix)-1)

    def is_valid_location(location, maze):
        """
        docstring
        """
        rows = len(maze)
        columns = len(maze[0])
        (x, y) = location
        if x >= 0 and x < columns and y >= 0 and y < rows and maze[x][y] != 0:
            return True
        return False

    def bfs_maze_solver(start, end, maze):
        """docstring"""
        queue = []
        visited = set()   

        queue.append((start, []))
        
        while len(queue) != 0:
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

    def print_path(path, maze):
        """
        docstring
        """
        solved_maze = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
        
        for location in path:
            x, y = location
            solved_maze[x][y] = 1
        
        for i in range(len(maze)):
            print(*solved_maze[i])

