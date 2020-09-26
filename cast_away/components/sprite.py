import arcade
from dataclasses import dataclass
from cast_away.components.draw_layer import DEFAULT_LAYER


def _prop(key):
    return property(lambda s: s._get(key), lambda s, v: s._set(key, v), None, None)


class Sprite:
    def __init__(self, path, scale=1, angle=0, alpha=255, draw_layer=DEFAULT_LAYER):
        self._state = {"path": path, "scale": scale, "alpha": alpha, "angle": angle}
        self.draw_layer = draw_layer
        self._changes = {}
        self._arcade_sprite = arcade.Sprite(path, scale=scale)

    def __repr__(self):
        return f"<Sprite state={self._state} changes={self._changes}"

    def _get(self, key):
        if key in self._changes:
            return self._changes[key]
        return self._state.get(key, None)

    def _set(self, key, value):
        self._changes[key] = value
        if self._changes.get(key) == self._state.get(key):
            self._changes.pop(key)

    def apply_changes(self):
        for key, value in self._changes.items():
            if key == "path":
                self.apply_path_change(value)
            else:
                setattr(self._arcade_sprite, key, value)
            self._state[key] = value
        self._changes = {}

    def apply_path_change(self, path):
        self._arcade_sprite.texture = arcade.load_texture(path)

    path = _prop("path")
    scale = _prop("scale")
    center_x = _prop("center_x")
    center_y = _prop("center_y")
    alpha = _prop("alpha")
    angle = _prop("angle")


@dataclass
class SpriteList:
    def __init__(self, _arcade_sprite_list):
        self._arcade_sprite_list = _arcade_sprite_list
