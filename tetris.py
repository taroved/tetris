import random
import copy


"""
*20x20*
*     *
*******
"""
class Panel:

  figure = None
  fugure_x = None
  figure_y = None

  matrix = None

  X_SIZE = 20
  Y_SIZE = 20
 
  def __init__(self):
    # create matrix
    self.matrix = [[0 for col in range(self.X_SIZE)] for row in range(self.Y_SIZE)]
 
  def new_figure(self):
    self.figure = Figure()
    d = self.figure.get_dimensions()

    x_interval = [-d["min_x"], self.X_SIZE-1 - d["max_x"]]
    # try random x position for start
    xpos = random.randint(x_interval[0], x_interval[1])
    if (self.validate_figure(self.figure, xpos, 1)):
      pass
    else: # move from left to right border
      shift = 1
      xpos = x_interval[0]
      # search empty space for new figure
      while not self.validate_figure(self.figure, xpos, 1):
        xpos += shift
        if xpos > x_interval[1]:
          break
    
    if self.validate_figure(self.figure, xpos, 1):
      self.figure_x = xpos
      self.figure_y = 1
      return True
    else:
      return False

  def validate_figure(self, figure, x, y):
    for i in figure.get_coordinates():
      if 0 <= i[0]+x < self.X_SIZE and i[1]+y < self.Y_SIZE and self.matrix[i[1]+y][i[0]+x]==0:
        pass
      else:
        return False
    return True

  def rotate_figure(self, clockwise):
    #import pdb
    #pdb.set_trace()
    f = copy.deepcopy(self.figure)
    f.rotate(clockwise)
    if self.validate_figure(f, self.figure_x, self.figure_y):
      self.figure.rotate(clockwise)
      return True
    else:
      return False

  def shift_figure(self, shift_x, shift_y):
    f = copy.deepcopy(self.figure)
    if self.validate_figure(f, self.figure_x+shift_x, self.figure_y+shift_y):
      self.figure_x += shift_x
      self.figure_y += shift_y 
      return True
    else:
      return False

  def shift_figure_down(self):
    return self.shift_figure(0, 1)

  def figure_end(self):
    for i in self.figure.get_coordinates():
      x = i[0]+self.figure_x
      y = i[1]+self.figure_y
      if 0 <= x < self.X_SIZE and 0 <= y < self.Y_SIZE:
        self.matrix[y][x] = 1
    self.figure = None

  def get_matrix_snapshot(self):
    m = copy.deepcopy(self.matrix)
    if self.figure:
      for i in self.figure.get_coordinates():
        x = i[0]+self.figure_x
        y = i[1]+self.figure_y
        if 0 <= x < self.X_SIZE and 0 <= y < self.Y_SIZE:
          m[y][x] = 1
    return m

class Figure:
  
  possible_figures = [
    #We can calculate rotations but hardcode is simple
    # |
    #**** states
    [
      [[-1,0], [0,0], [1,0], [2,0]],
      [[0,-1], [0,0], [0,1], [0,2]]
    ],
    #*
    #*<
    #*
    #** states
    [
      [[0,-1], [0,0], [0,1], [0,2], [1,2]],
      [[-2,1], [-2,0], [-1,0], [0,0], [1,0]],
      [[-1,-2], [0,-2], [0,-1], [0,0], [0,1]],
      [[-1,0], [0,0], [1,0], [2,0], [2,-1]]
    ],
    # *
    # *<
    # *
    #** states
    [
      [[0,-1], [0,0], [0,1], [0,2], [-1,2]],
      [[-2,-1], [-2,0], [-1,0], [0,0], [1,0]],
      [[1,-2], [0,-2], [0,-1], [0,0], [0,1]],
      [[-1,0], [0,0], [1,0], [2,0], [2,1]]
    ],
    #|*
    #**
    #*  states
    [
      [[0,1], [0,0], [1,0], [1,-1]],
      [[-1,0], [0,0], [0,1], [1,1]]
    ],
    #|
    #**
    #** states
    [
      [[0,0], [1,0], [1,1], [0,1]]
    ]
  ]

  SWUARE_NUM = 4

  fig_num = None
  fig_state = None

  def __init__(self):
    """Create random figure with random position"""
    self.fig_num = random.randint(0, len(self.possible_figures)-1)
    self.fig_state = random.randint(0, len(self.possible_figures[self.fig_num])-1)

  def is_rotatable(self):
    return self.fig_num != self.SWUARE_NUM

  def rotate(self, clockwise):
    if self.is_rotatable():
      positions = self.possible_figures[self.fig_num]
      if clockwise:
        self.fig_state = (self.fig_state + 1) % len(positions)
      else:
        self.fig_state = len(positions)-1 if self.fig_state == 0 else self.fig_state-1
 
  def get_dimensions(self):
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0

    position = self.possible_figures[self.fig_num][self.fig_state]

    for i in position:
       if min_x > i[0]:
         min_x = i[0]
       if min_y > i[1]:
         min_y = i[1]
       if max < i[0]:
         max_x = i[0]
       if max_y < i[1]:
         max_y = i[1]

    return {"min_x":min_x, "min_y":min_y, "max_x":max_x, "max_y":max_y}

  def get_coordinates(self):
    return self.possible_figures[self.fig_num][self.fig_state]     
  
  def __str__(self):
    return "<Figure (fig_num: %s fig_state: %s)>" % (self.fig_num, self.fig_state) 

    


