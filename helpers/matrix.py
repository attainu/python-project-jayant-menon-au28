class Matrix:
    """
    docstring
    """
    def create_matrix(lines):
        """docstring"""
        matrix = []
        for i in lines:
            i = i.replace("\n", "")
            i = i.replace(" ", "")
            row = list(map(int, i))
            matrix.append(row)
        return matrix

    def get_start_and_end(matrix):
        """ docstring"""
        return (0,0), (len(matrix[0])-1, len(matrix)-1)