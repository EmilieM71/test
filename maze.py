from position import Position


class Maze:

    def __init__(self, filename):  # Notre méthode constructeur
        """définition de l'attribut filename"""
        self.filename = filename
        self.wall = self.load_maze_from_file()

    def load_maze_from_file(self):
        """function that generates the map of the maze, and generates 3 objects randomly in the maze."""

        with open(self.filename, "r") as file:
            wall = []
            for x, line in enumerate(file):
                for y, c in enumerate(line):  # c for character
                    if c == 'w':
                        wall.append(Position(x, y))


            # objects = random.sample(path, 3)
            # objects[0] = needle

        return wall

    def display(self, window_name, wall_name):
        """function that displays the map of the maze"""

        for position in self.wall:
            x = position[0]
            y = position[1]
            window_name.blit(wall_name, (x, y))


def main():
    level = Maze("l1")
    level.load_maze_from_file
    print(level.load_maze_from_file())


if __name__ == '__main__':
    main()

