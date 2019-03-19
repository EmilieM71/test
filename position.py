class Position:

    def __init__(self, x, y):
        self.position = (x*30, y*30)

    def __repr__(self):
        return str(self.position)

    # Comparateur d'égalité pour 2 positions
    def __eq__(self, pos):
        return self.position == pos.position
