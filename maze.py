import random


class Cell:

    wall_pairs = {"N": "S", "S": "N", "E": "W", "W": "E"}

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {"N": True, "S": True, "E": True, "W": True}

    def has_all_walls(self):
        return all(self.walls.values())

    def knock_down_wall(self, other, wall):
        self.walls[wall] = False
        other.walls[Cell.wall_pairs[wall]] = False


class Maze:
    def __init__(self, num_rows, num_cols, start_x=0, start_y=0):
        """ """
        self.num_rows, self.num_cols = num_rows, num_cols
        self.start_x, self.start_y = start_x, start_y
        self.maze_map = [
            [Cell(x, y) for y in range(num_cols)] for x in range(num_rows)
        ]  # noqa E501

        self.add_begin_end = False
        self.add_treasure = False
        self.treasure_x = random.randint(0, self.num_rows - 1)
        self.treasure_y = random.randint(0, self.num_cols - 1)
