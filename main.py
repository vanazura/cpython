# Beating Heart 
# defaut input
import random
from math import sin, cos, pi, log 

CANVAS_WIDTH = 980 # frame_width
CANVAS_HEIGHT = 720 # frame_height
CANVAS_CENTER_X = CANVAS_WIDTH / 2 # frame_center_x
CANVAS_CENTER_Y = CANVAS_HEIGHT / 2 # center_y 
IMAGE_ENLARGE = 11  # ratio 
# color List 
HEART_COLOR_LIST = [ "#d974ff", "#be77fa", "#a478f3", "#8b78ea", "#7377e0", "#4871c6", "#5c74d3", "#fa6ea9", "#dc6db1", "#ec2c2ce91e41", "#8b44", "#593", "#2bd3ec", "#00be93", "#2bec62"]


def heart_function(t, shrink_ratio: float = IMAGE_ENLARGE):
  """
  create a heart 
  :param shrink_ratio: ratio
  :param t: parameter
  :return: x, y 
  """
  # basic function, size 
  x = 16 * (sin(t) ** 3)
  y = -(13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t))
  
  # zoom
  x *= shrink_ratio 
  y *= shrink_ratio
  
  return x, y
# def draw_heart