class Matrix:
    """
    A class to perform matrix functions
    """
    def create_matrix(lines):
        """takes list of strings input and returns a 2d matrix"""
        matrix = []
        for string in lines:
            string = string.replace("\n", "")
            string = string.replace(" ", "")
            row = list(map(int, string))
            matrix.append(row)
        return matrix

    def get_start_and_end(matrix):
        """returns the start and destination in (x, y) coordinates"""
        return (0,0), (len(matrix[0])-1, len(matrix)-1)