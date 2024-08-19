import numpy as np
from enum import Enum

class Color(Enum):
    RED = 0
    BLUE = 1
    GREEN = 2
    ORANGE = 3
    WHITE = 4
    YELLOW = 5

class Rubiks:
    def __init__(self, n: int = 3):
        if n > 5 or n < 3:
            raise ValueError("Only 3x3, 4x4 and 5x5 Rubik's cubes are supported")
        else:
            self.num_facelets = 6 * n * n
            self.face_mat_size = n * n
            self.cube = self._initialize_cube()

    def _initialize_cube(self):
        # Initialize a solved Rubik's cube with each face having a uniform color
        return [
            [Color.RED] * self.face_mat_size,   
            [Color.BLUE] * self.face_mat_size, 
            [Color.GREEN] * self.face_mat_size, 
            [Color.ORANGE] * self.face_mat_size, 
            [Color.WHITE] * self.face_mat_size,  
            [Color.YELLOW] * self.face_mat_size 
        ]
    
    def encode_cube(self):
        # Initialize a 6x54 matrix with zeros
        encoded_cube = np.zeros((6, self.num_facelets), dtype=int)
        
        # Flatten the cube representation for easier mapping
        flat_cube = [color for face in self.cube for color in face]
        
        # Map the cube colors to the binary matrix
        for index, color in enumerate(flat_cube):
            encoded_cube[color.value][index] = 1
        
        return encoded_cube

    def print_encoded_cube(self):
        encoded = self.encode_cube()
        print(encoded)


cube = Rubiks()
cube.print_encoded_cube()
