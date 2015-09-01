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

  while True:
    # create figure if not exists
    if not panel.figure:
      if not panel.new_figure():
        print "Game over!"
        break

    #draw panel
    clear()
    draw(panel.get_matrix_snapshot())

    print keys_text
    key = sys.stdin.read(1)
    if key == "a":
      if not panel.shift_figure(0,-1):
        print keys_text 

if __name__ == "__main__":
  main()
