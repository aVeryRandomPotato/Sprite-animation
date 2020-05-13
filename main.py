import pygame
import random
import sys
import math
from pygame.locals import *
from sprite_loader import *
from cat import *
from player import *

pygame.init()

screen_info = pygame.display.Info()
size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
color = (0, 0, 0)

cat_images = []

def get_images():
  cat_sheet = SpriteSheet("runningcat.png")
  man_sheet = SpriteSheet("man.png")

  directions = ["n", "s", "e", "w"]

  for i in range(4):
    for j in range(2):
      cat_images.append(cat_sheet.get_image(j * 512, i * 256, 512, 256))
      cat_images[-1] = pygame.transform.smoothscale(cat_images[-1], (180,90))

def main():
  get_images()
  cat = Cat((-90, random.randint(50, height-50)), cat_images)

if __name__ == "__main__":
  main()