import string
import random
import requests

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = (random.choices(string.ascii_uppercase,k=9))

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        li = []
        if word == '' or requests.get(f'https://dictionary.lewagon.com/{word}').json()['found'] == False:
            return False
        else:
            for letter in list(word):
                if letter in self.grid:
                    li.append(True)
                else:
                    li.append(False)
        if False in li:
            return False
        return True
