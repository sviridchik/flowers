from plants_base.choices import ChoicesMixin


class WateringTypes(ChoicesMixin):
    ABOVE = "from_above"
    BELOW = "from_below"
    SUBMERSIBLE = "submersible"
