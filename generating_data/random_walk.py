from random import choice

class RandomWalk(): 
    """A class to generate random walks."""
    def __init__(self, num_points=5000):
        """initialize attributes of a walk."""
        self.num_points: int = num_points

        # All walks start at (0,0).
        self.x_values: list[int] = [0]
        self.y_values: list[int] = [0] 

    def fill_walk(self):
        """Calculate all the points in the walk"""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:

            # tracks left or right movement, how far. Multiplied together equals the step.
            x_direction: int = choice([1, -1])
            x_distance: int = choice([0, 1, 2, 3, 4])
            x_step: int = x_direction * x_distance

            # tracks up or down movement, how far. Multiplied together equals the step.
            y_direction: int = choice([1, -1])
            y_distance: int = choice([0, 1, 2, 3, 4])
            y_step: int = y_direction * y_distance
    
            # if no movement, the loops continues 
            if x_step == 0 and y_step == 0:
                continue
            
            # calculate the next x and y values
            next_x: int = self.x_values[-1] + x_step
            next_y: int = self.y_values[-1] + y_step
    
            self.x_values.append(next_x) 
            self.y_values.append(next_y) 