from queue import PriorityQueue
from rubiks import Rubiks


def a_star_search(cube):
    queue = PriorityQueue()
    queue.put((0, cube))

    visited = set()
    steps = {cube: 0}

    while not queue.empty():
        
        cost, current_cube = queue.get()

        if current_cube.is_solved():
            return steps[current_cube]

        visited.add(current_cube)

        possible_moves = current_cube.get_possible_moves()
        for move in possible_moves:
            next_cube = current_cube.make_move(move)

            next_cost = steps[current_cube] + 1 + next_cube.get_heuristic()

            # Check if the next state has already been visited or has a higher cost
            if next_cube not in visited or next_cost < steps[next_cube]:
                # Update the number of steps taken to reach the next state
                steps[next_cube] = steps[current_cube] + 1

                # Add the next state to the priority queue
                queue.put((next_cost, next_cube))
    return -1

# Initialize the Rubik's Cube
rubiks_cube = Rubiks(n = 3)

# Solve the Rubik's Cube using A* search
steps_to_solve = a_star_search(rubiks_cube)

# Print the number of steps it takes to solve the Rubik's Cube
print(f"Number of steps to solve the Rubik's Cube: {steps_to_solve}")