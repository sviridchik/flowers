from enum import Enum


class ChoicesMixin(Enum):
    @classmethod
    def choices(cls):
        # return tuple((member[-1].name, member[-1].value) for member in cls.__members__.items())
        return tuple((name, member) for name, member in cls.__members__.items())


class SoilTypes(ChoicesMixin):
    CHERNOZEM = "Chernozem"
    SANDY = "Sandy"
    MOSS = "Moss"
    AGROVATA = "Agrovata"
    COCONUT = "Coconut"
    LINEN = "Linen"


class WateringTypes(ChoicesMixin):
    ABOVE = "from_above"
    BELOW = "from_below"
    SUBMERSIBLE = "submersible"


class BreedingTypes(ChoicesMixin):
    SEEDS = "seeds"
    DIVISION = "division"
    KIDS = "kids"


class ColorTypes(ChoicesMixin):
    WHITE = "white"
    RED = "red"
    YELLOW = "yellow"
