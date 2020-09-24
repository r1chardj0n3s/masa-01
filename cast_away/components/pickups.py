class _PickupData:
    def __init__(
        self, image, hud_image, inventory_item_component_classes, scale=0.2, radius=25
    ):
        self.image = image
        self.hud_image = hud_image
        self.scale = scale
        self.inventory_item_component_classes = inventory_item_component_classes
        self.radius = radius


class Pickup:
    hud_scale = 0.4
    is_unique = False


class SawThrower(Pickup):
    is_unique = True


class LazorGun(Pickup):
    ...


PICKUP_DATA = {
    "saw": _PickupData(
        image=":resources:images/enemies/saw.png",
        hud_image=":resources:images/enemies/saw.png",
        inventory_item_component_classes=[SawThrower],
    ),
    "lazorgun": _PickupData(
        image=":resources:images/items/star.png",
        hud_image=":resources:images/items/star.png",
        inventory_item_component_classes=[LazorGun],
    ),
}
