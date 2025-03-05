# -- Pygame Game Template -- #

import pygame
import sys
import config # Import the config module 
import random
import shapes
def init_game (): 
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen


def handle_events ():
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          return False
       elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
             return False
    return True
   



def draw_text(screen, text, font, text_col, x, y):
   
   txt_img = font.render(text, True, text_col)
   screen.blit(txt_img, (x, y))








def main():
   screen = init_game()
   clock = pygame.time.Clock() # Initialize the clock here
   txt_font1 = pygame.font.SysFont("Ariel", random.randint(10, 100))
   shapes_list = []
   
   running = True
   while running:
      running = handle_events()
      screen.fill(config.WHITE) # Use color from config

      #makes a random number to represent the various shapes
      shape_type = random.randrange(3)
      font = pygame.font.SysFont(None, shape_type)
      pygame.render
      #Create a new shape and add it to the list 
      if shape_type == 0:
         # Circle: (type, color, position, radius)
         new_shapes = {
               'type':'circle',
               'color':(random.randrange(255), random.randrange(255), random.randrange(255)),
               'position':(random.randrange(config.WINDOW_WIDTH), random.randrange(config.WINDOW_HEIGHT)),
               'radius': 50
         }
      elif shape_type == 1:
         # rectangle: (type, color, position, width, height)
         new_shapes = {
               'type':'rectangle',
               'color':(random.randrange(255), random.randrange(255), random.randrange(255)),
               'position':(random.randrange(config.WINDOW_WIDTH) - 100, random.randrange(config.WINDOW_HEIGHT) - 100),
               'width': 100,
               'height':100
         }
      elif shape_type == 2:
            # line: (type,color, start_pos, end_pos, width)
            new_shapes = {
                'type': 'line',
               'color': (random.randrange(255), random.randrange(255), random.randrange(255)),
               'start_pos': (random.randrange(config.WINDOW_WIDTH), random.randrange(config.WINDOW_HEIGHT)),
               'end_pos': (random.randrange(config.WINDOW_WIDTH), random.randrange(config.WINDOW_HEIGHT)),
               'width': 10
            }
      # add the new shapes to the list
      shapes_list.append(new_shapes)
              
      # draw all shapes from the list using the appropriate function from the shapes module\
      for shape in shapes_list: 
         if shape['type'] == 'circle':
            shapes.draw_circle(screen, shape)
         elif shape['type'] == 'rectangle':
            shapes.draw_rect(screen, shape)
         elif shape['type'] == 'line': 
            shapes.draw_line(screen, shape)
      draw_text(screen, "Hello World", txt_font1, (0,0,0), (config.WINDOW_WIDTH), (config.WINDOW_HEIGHT))

        # Randomize text size each time it is drawn
      txt_font1 = pygame.font.SysFont("Arial", random.randint(10, 100))

        # Draw random sized text at the bottom of the screen
      draw_text(screen, "Hello World", txt_font1, (0, 0, 0), config.WINDOW_WIDTH // 2 - 50, config.WINDOW_HEIGHT - 50)

      pygame.display.flip()

      # -- Limit the frame rate to the specified frames per second (FPS) -- #
      clock.tick(config.FPS) # Use the clock to control the frame rate

   pygame.quit()
   sys.exit()

if __name__ == "__main__":
   main()