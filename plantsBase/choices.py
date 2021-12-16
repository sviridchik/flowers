from enum import Enum


class SoilTypes(Enum):
    CHERNOZEM = "Chernozem"
    SANDY = "Sandy"
    MOSS = "Moss"
    AGROVATA = "Agrovata"
    COCONUT = "Coconut"
    LINEN = "Linen"

    @classmethod
    def choices(cls):
        return tuple((member[-1].name, member[-1].value) for member in cls.__members__.items())


class WateringTypes(Enum):
    ABOVE = "from_above"
    BELOW = "from_below"
    SUBMERSIBLE = "submersible"

    @classmethod
    def choices(cls):
        return tuple((member[-1].name, member[-1].value) for member in cls.__members__.items())


class BreedingTypes(Enum):
    SEEDS = "seeds"
    DIVISION = "division"
    KIDS = "kids"

    @classmethod
    def choices(cls):
        return tuple((member[-1].name, member[-1].value) for member in cls.__members__.items())


class ColorTypes(Enum):
    WHITE = "white"
    RED = "red"
    YELLOW = "yellow"

    @classmethod
    def choices(cls):
        return tuple((member[-1].name, member[-1].value) for member in cls.__members__.items())
