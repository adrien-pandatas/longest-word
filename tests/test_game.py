# tests/test_game.py
from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
            # setup
            game = Game()

            # exercise
            grid = game.grid

            # verify
            assert isinstance(grid, list)
            assert len(grid) == 9
            for letter in grid:
                assert letter in string.ascii_uppercase

            # teardown

    def test_empty_word_is_invalid(self):
        # setup
        new_game = Game()
        # verify
        assert new_game.is_valid('') is False

    def test_word_is_invalid(self):
        # setup
        new_game = Game()
        word = "BLA"
        new_grid = 'BHYFHJAOI'

        new_game.grid = new_grid
        assert new_game.is_valid(word) is False

    def test_word_is_valid(self):
        # setup
        new_game = Game()
        word = "JAY"
        new_grid = 'BHYFHJAOI'

        new_game.grid = new_grid
        assert new_game.is_valid(word) is True

    def test_unknown_word_is_invalid(self):
        """A word that is not in the English dictionary should not be valid"""
        new_game = Game()
        new_game.grid = 'KWIENFUQW' # Force the grid to a test case:
        assert new_game.is_valid('FEUN') is False
