from dataclasses import dataclass

battle_dict = {
    'fire': 'grass',
    'water': 'fire',
    'grass': 'water'
}

@dataclass
class Pokemon():
    name: str
    _type: str
    def __eq__(self, other):
        return self.name == other.name
    
    def __ne__(self, other):
        return not self.__eq__(self, other)
    
    def __lt__(self, other):
        return self._type in battle_dict[other._type]
    
    def __gt__(self, other):
        return other._type in battle_dict[self._type]
        

class FireType(Pokemon):
    def __init__(self, name: str) -> None:
        super().__init__(name=name, _type='fire')

class WaterType(Pokemon):
    def __init__(self, name: str) -> None:
        super().__init__(name=name, _type='water')

class GrassType(Pokemon):
    def __init__(self, name: str) -> None:
        super().__init__(name=name, _type='grass')

class Charmander(FireType):
    def __init__(self, name: str) -> None:
        super().__init__(name)

class Squirtle(WaterType):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        