class SoilTypes:
    CHERN = "Chernozem"
    SAN = "Sandy"
    MOSS = "Moss"
    AGRO = "Agrovata"
    COCO = "Coconut"
    LIN = "Linen"


soil_choose = (
    (SoilTypes.CHERN, "Chernozem"),
    (SoilTypes.SAN, "Sandy"),
    (SoilTypes.MOSS, "Moss"),
    (SoilTypes.AGRO, "Agrovata"),
    (SoilTypes.COCO, "Coconut"),
    (SoilTypes.LIN, "Linen"),
)

class WateringTypes:
    FA = "from_above"
    FB = "from_below"
    SUB = "submersible"


watering_choose = (
    (WateringTypes.FA, "from_above"),
    (WateringTypes.FB, "from_below"),
    (WateringTypes.SUB, "submersible"),
)

class BreedingTypes:
    SE = "seeds"
    DI = "division"
    K = "kids"

breeding_choose = (
    (BreedingTypes.SE, "seeds"),
    (BreedingTypes.DI, "division"),
    (BreedingTypes.K, "kids"),
)


class ColorTypes:
    W = "white"
    R = "red"
    Y = "yellow"

color_choose = (
    (ColorTypes.W, "white"),
    (ColorTypes.R, "red"),
    (ColorTypes.Y, "yellow"),
)

