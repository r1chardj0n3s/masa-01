
class Entity:
    def __init__(world, entity):
        self.world = world
        self.entity = entity
    
    def has_component(c):
        return self.world.has_component(self.entity)
    
    def component(c):
        return self.world.component_for_entity(self.entity, c)

    def try_component(c):
        return self.world.try_component(self.entity, c)

    def destroy():
        return self.world.delete_entity(self.entity)
    
    def add_component(c):
        return self.world.add_component(self.entity, c)

    def remove_component(c):
        return self.world.remove_component(self.entity, c)