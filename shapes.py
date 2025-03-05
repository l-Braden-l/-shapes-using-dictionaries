import pygame 

def draw_circle(screen, shape):
   pygame.draw.circle(screen, shape["color"], shape["position"], shape["radius"])

def draw_rect(screen, shape):
   pygame.draw.rect(screen, shape["color"], (shape["position"][0], shape["position"][1], shape["width"], shape["height"]))

def draw_line(screen, shape):
   pygame.draw.line(screen, shape["color"], shape["start_pos"], shape["end_pos"], shape["width"])
