from constants import SHOT_RADIUS
from circleshape import CircleShape
import pygame


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen , color="white", center=self.position, radius=self.radius)

    def update(self, dt: float):
        self.position+=self.velocity*dt
