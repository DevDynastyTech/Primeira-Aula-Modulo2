import random
import pygame

from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus, LargeCactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstacleManager:
    OBSTACLE_TYPES = [
        (Cactus, SMALL_CACTUS),
        (LargeCactus, LARGE_CACTUS),
        (Bird, BIRD),
    ]

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle_type = random.choice(self.OBSTACLE_TYPES)
            obstacle_class, obstacle_image = obstacle_type
            self.obstacles.append(obstacle_class(obstacle_image))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
                else:
                    self.obstacles.remove(obstacle)

    def remove_all_obstacles(self):
        self.obstacles = []

    def reset_obstacles(self):
        self.obstacles = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
