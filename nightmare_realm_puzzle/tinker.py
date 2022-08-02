import random


class GameField:
    game_field = [['@', '#', '@', '#', '@'],
                    ['@', ' ', '@', ' ', '@'],
                    ['@', '#', '@', '#', '@'],
                    ['@', ' ', '@', ' ', '@'],
                    ['@', '#', '@', '#', '@']]

    game_tokens = ['a', 'a', 'a', 'a', 'a',
                   'b', 'b', 'b', 'b', 'b',
                   'c', 'c', 'c', 'c', 'c']

    def __init__(self):
        # fill the field with tokens
        random.shuffle(self.game_tokens)
        for i, row in enumerate(self.game_field):
            for j, place in enumerate(row):
                if place == '@':
                    self.game_field[i][j] = self.game_tokens.pop()

    def change_cursor_position(self):
        pass

    def info(self):
        for row in self.game_field:
            print(' '.join(row))


if __name__ == "__main__":
    field = GameField()
    field.info()
