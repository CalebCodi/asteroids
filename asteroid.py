from circleshape import CircleShape
import pygame
from logger import log_event
import random

from constants import ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen , color="white", center=self.position, radius=self.radius, width=LINE_WIDTH)

    def update(self, dt: float):
        self.position+=self.velocity*dt

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            vel1 = self.velocity.rotate(angle)
            vel2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = 1.2*vel1
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = 1.2*vel2
