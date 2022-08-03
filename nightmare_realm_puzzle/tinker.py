import random


class GameField:
    """Class that describes game field and position of assets on it"""
    # game_field describes the game field
    game_field = [['@', '#', '@', '#', '@'],
                  ['@', ' ', '@', ' ', '@'],
                  ['@', '#', '@', '#', '@'],
                  ['@', ' ', '@', ' ', '@'],
                  ['@', '#', '@', '#', '@']]

    # game_tokens describes the groups of tokens
    game_tokens = ['a', 'a', 'a', 'a', 'a',
                   'b', 'b', 'b', 'b', 'b',
                   'c', 'c', 'c', 'c', 'c']

    def __init__(self):
        """Initializes game field: draws graphical representation
            and adds a cursor onto it"""
        # fill the field with tokens
        random.shuffle(self.game_tokens)
        for i, row in enumerate(self.game_field):
            for j, place in enumerate(row):
                if place == '@':
                    self.game_field[i][j] = self.game_tokens.pop()
        # set cursor at (0, 0)
        self.cursor_position = {'x': 0, 'y': 0}
        self._make_upper()

    def move_cursor(self, move_x, move_y):
        """Moves cursor"""
        if ((move_x < 0) and (self.cursor_position['x'] > 0)) or \
                ((move_x > 0) and (self.cursor_position['x'] < len(self.game_field[0]) - 1)):
            self._make_lower()
            self.cursor_position['x'] += move_x
            if self.game_field[self.cursor_position['y']][self.cursor_position['x']] in ('a', 'b', 'c'):
                self._make_upper()
        if ((move_y < 0) and (self.cursor_position['y'] > 0)) or \
                ((move_y > 0) and (self.cursor_position['y'] < len(self.game_field) - 1)):
            self._make_lower()
            self.cursor_position['y'] += move_y
            if self.game_field[self.cursor_position['y']][self.cursor_position['x']] in ('a', 'b', 'c'):
                self._make_upper()

    def _make_lower(self):
        """Make the symbol lower at current position"""
        self.game_field[self.cursor_position['y']][self.cursor_position['x']] \
            = self.game_field[self.cursor_position['y']][self.cursor_position['x']].lower()

    def _make_upper(self):
        """Make symbol upper at current position"""
        self.game_field[self.cursor_position['y']][self.cursor_position['x']] = \
            self.game_field[self.cursor_position['y']][self.cursor_position['x']].upper()

    def is_tile(self):
        return self.game_field[self.cursor_position['y']][self.cursor_position['x']].lower() in ('a', 'b', 'c')

    def info(self):
        """Shows game field"""
        print("  1 2 3 4 5")
        for row_number, row in enumerate(self.game_field):
            print(f"{row_number + 1} ", end='')
            print(' '.join(row))
        print(self.cursor_position)
        print(f"It's tile: {self.is_tile()}")


class Tile:
    """Class that describes one tile that you can move"""

    def __init__(self, tile_type='a'):
        if tile_type.lower() in 'abc':
            self.tile_type = tile_type
        else:
            raise AttributeError(f"Cannot create a tile with symbol \"{tile_type}\"")


if __name__ == "__main__":
    field = GameField()
    while True:
        field.info()
        command = input("> ").lower()
        if command == "left":
            field.move_cursor(-1, 0)
        elif command == "right":
            field.move_cursor(1, 0)
        elif command == "up":
            field.move_cursor(0, -1)
        elif command == "down":
            field.move_cursor(0, 1)
        elif command == "quit":
            break
