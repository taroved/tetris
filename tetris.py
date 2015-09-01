

"""
*20x20*
*     *
*******
"""
class Panel:

  figure = None
  matrix = None

  X_SIZE = 20
  Y_SIZE = 20
 
  def __init__(self):
    # create matrix
    matrix = [[0 for col in range(self.X_SIZE)] for row in range(self.Y_SIZE)]
 
  def add_figure(self, figure):
      

  def validate_figure(self):
    

  def key_press(self, key):
    if  


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


  def is_rotatable(self):
    return self.fig_num == self.SWUARE_NUM




