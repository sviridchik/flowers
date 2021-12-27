from enum import Enum


class ChoicesMixin(Enum):
    @classmethod
    def choices(cls):
        return tuple((name, member) for name, member in cls.__members__.items())


class SoilTypes(ChoicesMixin):
    CHERNOZEM = "Chernozem"
    SANDY = "Sandy"
    MOSS = "Moss"
    AGROVATA = "Agrovata"
    COCONUT = "Coconut"
    LINEN = "Linen"


class BreedingTypes(ChoicesMixin):
    SEEDS = "seeds"
    DIVISION = "division"
    KIDS = "kids"


class ColorTypes(ChoicesMixin):
    WHITE = "white"
    RED = "red"
    YELLOW = "yellow"
