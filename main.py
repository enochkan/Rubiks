from enum import Enum

class Color(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3
    ORANGE = 4
    WHITE = 5
    YELLOW = 6

class Rubiks:
    def __init__(self, size: tuple = (3, 3, 3)):
        self.dimensions = size
        self.cube = self._initialize_cube()
    
    def _initialize_cube(self):
        n = self.dimensions[0]
        return {
            'front': [[Color.RED for _ in range(n)] for _ in range(n)],
            'back': [[Color.ORANGE for _ in range(n)] for _ in range(n)],
            'left': [[Color.GREEN for _ in range(n)] for _ in range(n)],
            'right': [[Color.BLUE for _ in range(n)] for _ in range(n)],
            'top': [[Color.WHITE for _ in range(n)] for _ in range(n)],
            'bottom': [[Color.YELLOW for _ in range(n)] for _ in range(n)],
        }

    def print_cube(self):
        for face, colors in self.cube.items():
            print(f"{face} face:")
            for row in colors:
                print(" ".join(color.name for color in row))
            print()