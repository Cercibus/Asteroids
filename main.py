import pygame
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, LINE_WIDTH
from logger import log_state


def main():
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	updateables = pygame.sprite.Group()
	drawables = pygame.sprite.Group()
	Player.containers = (updateables, drawables)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
	while True:
		for event in pygame.event.get():
			 if event.type == pygame.QUIT:
       				 return
		log_state()
		screen.fill("black")
		for updateable in updateables:
			updateable.update(dt)
		for drawable in drawables:
			drawable.draw(screen)
		pygame.display.flip()
		clock.tick(60)
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
