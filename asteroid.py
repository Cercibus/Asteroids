import pygame
import circleshape
import random
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid (circleshape.CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		pygame.sprite.Sprite.kill(self)
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			log_event("asteroid_split")
			angle = random.uniform(20, 50)
			size = self.radius - ASTEROID_MIN_RADIUS
			a1 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
			a2 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
			a1.velocity = self.velocity.rotate(angle) * 1.2
			a2.velocity = self.velocity.rotate(-angle) * 1.2
