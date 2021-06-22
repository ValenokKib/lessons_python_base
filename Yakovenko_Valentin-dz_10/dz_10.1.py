from copy import deepcopy

class Matrix():
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        return '\n'.join('\t'.join(map(str, l)) for l in self.matrix)

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))

    def __add__(self, other):
        matrix = []
        for i in range(len(self.matrix)):
            matrix.append([])
            for j in range(len(self.matrix[0])):
                matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
        return Matrix(matrix)


a1 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
a2 = Matrix([[3, 2, -10], [6, 5, 4], [77, 12, 1]])
#a2 = Matrix([[1, 2, 4], [6, 8, 4]])

print(str(a1))
print(str(a1.size()))
print(str(a2.size()))
print(a1 + a2)