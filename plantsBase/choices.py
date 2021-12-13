class SoilTypes:
    CHERNOZEM = "Chernozem"
    SANDY = "Sandy"
    MOSS = "Moss"
    AGROVATA = "Agrovata"
    COCONUT = "Coconut"
    LINEN = "Linen"


soil_choose = (
    (SoilTypes.CHERNOZEM, "Chernozem"),
    (SoilTypes.SANDY, "Sandy"),
    (SoilTypes.MOSS, "Moss"),
    (SoilTypes.AGROVATA, "Agrovata"),
    (SoilTypes.COCONUT, "Coconut"),
    (SoilTypes.LINEN, "Linen"),
)

class WateringTypes:
    ABOVE = "from_above"
    BELOW = "from_below"
    SUBMERSIBLE = "submersible"


watering_choose = (
    (WateringTypes.ABOVE, "from_above"),
    (WateringTypes.BELOW, "from_below"),
    (WateringTypes.SUBMERSIBLE, "submersible"),
)

class BreedingTypes:
    SEEDS = "seeds"
    DIVISION = "division"
    KIDS = "kids"

breeding_choose = (
    (BreedingTypes.SEEDS, "seeds"),
    (BreedingTypes.DIVISION, "division"),
    (BreedingTypes.KIDS, "kids"),
)


class ColorTypes:
    WHITE = "white"
    RED = "red"
    YELLOW = "yellow"

color_choose = (
    (ColorTypes.WHITE, "white"),
    (ColorTypes.RED, "red"),
    (ColorTypes.YELLOW, "yellow"),
)

