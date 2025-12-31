import pygame
import sys
from circleshape import CircleShape
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, LINE_WIDTH
from logger import log_state, log_event


def main():
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	Shot.containers = (shots, updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
	asteroidfield = AsteroidField()
	while True:
		for event in pygame.event.get():
			 if event.type == pygame.QUIT:
       				 return
		log_state()
		screen.fill("black")
		for updatable_thing in updatable:
			updatable_thing.update(dt)
		for drawable_thing in drawable:
			drawable_thing.draw(screen)
		for asteroid in asteroids:
			if CircleShape.collides_with(asteroid, player):
				log_event("player_hit")
				print("Game Over!")
				sys.exit()
			for shot in shots:
				if CircleShape.collides_with(shot, asteroid):
					log_event("asteroid_shot")
					asteroid.split()
		pygame.display.flip()
		clock.tick(60)
		dt = clock.tick(60) / 1000
		player.cooldown -= dt

if __name__ == "__main__":
    main()
