import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.heart import Heart


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200, 300)
            power_up_class = random.choice([Shield, Hammer])
            self.power_ups.append(power_up_class())


def generate_power_up(self, score):
    if len(self.power_ups) == 0 and self.when_appears == score:
        self.when_appears += random.randint(200, 300)
        power_up_class = random.choice([Shield, Hammer, Heart])
        self.power_ups.append(power_up_class())


def update(self, game):
    self.generate_power_up(game.score)
    for power_up in self.power_ups:
        power_up.update(game.game_speed, self.power_ups)

        if game.player.dino_rect.colliderect(power_up.rect):
            power_up.start_time = pygame.time.get_ticks()
            if isinstance(power_up, Shield):
                game.player.shield = True
            elif isinstance(power_up, Hammer):
                self.power_ups.remove(power_up)
            elif isinstance(power_up, Heart):
                game.player.health += 10
                self.power_ups.remove(power_up)
            game.player.has_power_up = True
            game.player.type = power_up.type
            game.player.power_up_time = power_up.start_time + \
                (power_up.duration * 1000)


def draw(self, screen):
    for power_up in self.power_ups:
        power_up.draw(screen)


def reset_power_ups(self):
    self.power_ups = []
    self.when_appears = random.randint(200, 300)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)
