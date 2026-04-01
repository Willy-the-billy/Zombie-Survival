from pathlib import Path

import pygame


ASSET_ROOT = Path(__file__).resolve().parents[1]
BACKGROUND_PATH = ASSET_ROOT / "background-1.png.png"
WINDOW_TITLE = "Catfish"
FPS = 60


def load_scaled_background(size):
	background = pygame.image.load(BACKGROUND_PATH).convert()
	return pygame.transform.scale(background, size)


def main():
	pygame.init()
	pygame.display.set_caption(WINDOW_TITLE)

	screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
	clock = pygame.time.Clock()
	background = load_scaled_background(screen.get_size())

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				running = False

		screen.blit(background, (0, 0))
		pygame.display.flip()
		clock.tick(FPS)

	pygame.quit()


if __name__ == "__main__":
	main()
