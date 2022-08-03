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
        self.cursor_position = [0, 0]

    def change_cursor_position(self):
        """Moves cursor"""
        pass

    def info(self):
        """Shows game field"""
        for row in self.game_field:
            print(' '.join(row))


class Tile:
    """Class that describes one tile that you can move"""

    def __init__(self, tile_type='a'):
        if tile_type.lower() in 'abc':
            self.tile_type = tile_type
        else:
            raise AttributeError(f"Cannot create a tile with symbol \"{tile_type}\"")


if __name__ == "__main__":
    field = GameField()
    field.info()
