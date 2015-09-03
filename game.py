import os
import sys

import tetris

def clear():
  """Create console"""
  os.system('cls' if os.name == 'nt' else 'clear')

def draw(matrix):
  for row in matrix:
    sys.stdout.write('*')
    for col in row:
      sys.stdout.write('*' if col else ' ')
    print '*'
  print '**********************'
  

def main():
  panel = tetris.Panel()
  
  keys_text = 'Enter your move ("a" - move left, "d" - move right, "w" - rotate counter clockwise, "s" rotate clockwise):'

  redraw = True
  while True:
    # create figure if not exists
    if not panel.figure:
      if not panel.new_figure():
        print "Game over!"
        break

    #draw panel
    if redraw:
      clear()
      draw(panel.get_matrix_snapshot())

    print keys_text
    key = sys.stdin.readline()[0]

    if key == "a":  # move left
      if not panel.shift_figure_x(-1):
        redraw = False 
      else:
        if not panel.shift_figure_down():
          panel.figure_end()
        redraw = True
    elif key == "d":  # move right
      if not panel.shift_figure_x(1):
        redraw = False
      else:
        if not panel.shift_figure_down():
          panel.figure_end()
        redraw = True
    elif key == "w":  # rotate counter clockwise
      if not panel.rotate_figure(False):
        redraw = False
      else:
        if not panel.shift_figure_down():
          panel.figure_end()
        redraw = True
    elif key == "s":  # rotate clockwise
      if not panel.rotate_figure(True):
        redraw = False
      else:
        if not panel.shift_figure_down():
          panel.figure_end()
        redraw = True
    else:
      redraw = False
      

if __name__ == "__main__":
  main()
