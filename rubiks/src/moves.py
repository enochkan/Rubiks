
import numpy as np
from copy import deepcopy

class CubeMoves:
    def __init__(self, n):
        self.n = n

    def rotate_face_clockwise(self, face):
        if self.n == 3:
            return [
                face[6], face[3], face[0],
                face[7], face[4], face[1],
                face[8], face[5], face[2]
            ]
        elif self.n == 4:
            return [
                face[12], face[8], face[4], face[0],
                face[13], face[9], face[5], face[1],
                face[14], face[10], face[6], face[2],
                face[15], face[11], face[7], face[3]
            ]
        elif self.n == 5:
            return [
                face[20], face[15], face[10], face[5], face[0],
                face[21], face[16], face[11], face[6], face[1],
                face[22], face[17], face[12], face[7], face[2],
                face[23], face[18], face[13], face[8], face[3],
                face[24], face[19], face[14], face[9], face[4]
            ]

    def rotate_face_counterclockwise(self, face):
        if self.n == 3:
            return [
                face[2], face[5], face[8],
                face[1], face[4], face[7],
                face[0], face[3], face[6]
            ]
        elif self.n == 4:
            return [
                face[3], face[7], face[11], face[15],
                face[2], face[6], face[10], face[14],
                face[1], face[5], face[9], face[13],
                face[0], face[4], face[8], face[12]
            ]
        elif self.n == 5:
            return [
                face[4], face[9], face[14], face[19], face[24],
                face[3], face[8], face[13], face[18], face[23],
                face[2], face[7], face[12], face[17], face[22],
                face[1], face[6], face[11], face[16], face[21],
                face[0], face[5], face[10], face[15], face[20]
            ]

    def make_move(self, cube, move):
        new_cube = deepcopy(cube)
        front, back, left, right, up, down = range(6)
        
        row = lambda face, i: face[i * self.n:(i + 1) * self.n]
        col = lambda face, i: face[i::self.n]

        if move == "F":
            new_cube[front] = self.rotate_face_clockwise(cube[front])
            temp = row(cube[up], self.n - 1)
            new_cube[up][(self.n-1)*self.n:self.n*self.n] = col(cube[left], self.n - 1)[::-1]
            for i in range(self.n):
                new_cube[left][i * self.n + (self.n-1)] = cube[down][i]
            new_cube[down][0:self.n] = col(cube[right], 0)[::-1]
            for i in range(self.n):
                new_cube[right][i * self.n] = temp[i]
        
        elif move == "F'":
            new_cube[front] = self.rotate_face_counterclockwise(cube[front])
            temp = row(cube[up], self.n - 1)
            new_cube[up][(self.n-1)*self.n:self.n*self.n] = col(cube[right], 0)
            for i in range(self.n):
                new_cube[right][i * self.n] = cube[down][self.n - 1 - i]
            new_cube[down][0:self.n] = col(cube[left], self.n - 1)
            for i in range(self.n):
                new_cube[left][i * self.n + (self.n-1)] = temp[self.n - 1 - i]

        # TODO: Implement the rest of the moves

        return new_cube
