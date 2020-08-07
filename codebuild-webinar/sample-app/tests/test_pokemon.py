

from copy import deepcopy

import pytest

from src.pokemon import (
    Pokemon,
    FireType,
    WaterType,
    Charmander,
    Squirtle
)

class TestBattle:
    def test_battle_comparison(self):
        # Water types should beat Fire types
        ash = Charmander('ash')
        gary = Squirtle('gary')
        assert gary > ash

    def test_same_names(self):
        # Water types should beat Fire types
        ash = Charmander('gary')
        gary = Squirtle('gary')
        assert gary == ash
