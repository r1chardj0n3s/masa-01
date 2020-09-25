class Entity:
    def __init__(self, world, entity):
        self.world = world
        self.entity = entity

    def has_component(self, c):
        return self.world.has_component(self.entity)

    def component(self, c):
        return self.world.component_for_entity(self.entity, c)

    def try_component(self, c):
        return self.world.try_component(self.entity, c)

    def destroy(self):
        return self.world.delete_entity(self.entity)

    def add_component(self, c):
        return self.world.add_component(self.entity, c)

    def remove_component(self, c):
        return self.world.remove_component(self.entity, c)
