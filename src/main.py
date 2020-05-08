from lines import Lines
import pygame
import pygame.freetype
import sys
import importlib
import time

algorithm = importlib.import_module(f".{sys.argv[1]}", "algorithms")

pygame.init()
pygame.display.set_caption("PySort")

size = width, height = 1280, 720

screen = pygame.display.set_mode(size)
font = pygame.freetype.SysFont("Arial", 24)

lines = Lines(height, width)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    algorithm.sort_one(lines)
    time.sleep(0.005)

    screen.fill((0, 0, 0))
    for (i, val) in enumerate(lines.values):
        pygame.draw.line(screen, (255, 255, 255), (i, height), (i, height - val))
    font.render_to(screen, (10, 10), f"Sorted {lines.already_sorted + 1}/{len(lines.values)} lines", (255, 255, 255))
    pygame.display.flip()
