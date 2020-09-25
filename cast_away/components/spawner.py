from dataclasses import dataclass


@dataclass
class EnemySpawner:
    spawning = False
    spawn_timer = 0
