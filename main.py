import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  clock = pygame.time.Clock()
  dt = 0

  asteroids = pygame.sprite.Group()
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  Player.containers = (updatable, drawable)
  Shot.containers = (shots, updatable, drawable)
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  asteroidfield = AsteroidField()

  while(True):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
        
    updatable.update(dt)

    for asteroid in asteroids:
      collision = asteroid.check_for_collision(player)
      if collision:
        print("Game over!")
        sys.exit()
      for shot in shots:
        if asteroid.check_for_collision(shot):
          shot.kill()
          asteroid.split()

    pygame.Surface.fill(screen, (0, 0, 0))

    for obj in drawable:
      obj.draw(screen)

    pygame.display.flip()
    
    # limit the framerate to 60 FPS
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()