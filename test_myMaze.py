import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import maze.myMaze as obstacles
import world.text.world as world
# import random

class MyTestCase(unittest.TestCase):

    def test_obstacle_list(self):
        list_size = obstacles.obstacleList
        output = obstacles.get_obstacles()
        if len(output) in range(1,len(list_size)+1):
            self.assertEquals(len(list_size),len(output))

    def test_position_blocked(self):
      x = world.x
      y = world.y
      blocked_position = obstacles.get_obstacles()
      for i in blocked_position:
        obstacle = i
        if [x,y] == obstacle[0:]:
          self.assertTrue([x,y], obstacles[0:])

    def test_path_blocked(self):
        x = world.x
        y = world.y
        blocked_path = obstacles.get_obstacles()
        for i in blocked_path:
            if x in range (i[0], i[0] + 4) and y in range(i[1], i[1] + 4):
                self.assertTrue([x,y], [i[0],i[1]])