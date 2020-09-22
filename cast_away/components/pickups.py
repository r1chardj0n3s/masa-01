
class Pickup:
    image: str
    scale = 0.2
    hud_scale = 0.4
    is_unique = False
    pickup_distance = 50


class SawThrower(Pickup):
    image = ":resources:images/enemies/saw.png"
    is_unique = True


class StarThrower(Pickup):
    image = ":resources:images/items/star.png"
