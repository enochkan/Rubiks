import numpy as np
from enum import Enum
from moves import CubeMoves

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
            self.n = n
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

    def get_heuristic(self):
        # only returning misplaced facelets right now
        misplaced_facelets = 0
        for color_idx, row in enumerate(self.cube):
            expected_pattern = [1 if i // self.n == color_idx else 0 for i in range(self.num_facelets)]
            misplaced_facelets += np.sum(row != expected_pattern)
        return misplaced_facelets

    def is_solved(self) -> bool:
        """
        Check if the Rubik's cube is solved.
        Returns:
            bool: True if the cube is solved, False otherwise.
        """
        for color_idx, row in enumerate(self.cube):
            expected_pattern = [1 if i // self.n == color_idx else 0 for i in range(self.num_facelets)]
            if not np.array_equal(row, expected_pattern):
                return False
        return True

    def get_possible_moves(self) -> list:
        """
        Get the possible moves that can be made on the Rubik's cube.
        Returns:
            list: A list of possible moves.
        """
        return ["F", "F'", "B", "B'", "L", "L'", "R", "R'", "U", "U'", "D", "D'"]

    def encode_cube(self):
        """
        Encodes the current state of the Rubik's cube into a tuple.

        Returns:
            tuple: A tuple representing the colors of each face of the cube.
        """
        return tuple([color for face in self.cube for color in face])

    def print_encoded_cube(self):
        encoded = self.encode_cube()
        print(encoded)

    def __eq__(self, other):
        return np.array_equal(self.cube, other.cube)

    def __hash__(self):
        return hash(self.cube.tobytes())

cube = Rubiks()
cube.print_encoded_cube()
