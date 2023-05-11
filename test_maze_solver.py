import unittest
from io import StringIO
from unittest.mock import patch
import sys
import import_helper
import maze_solver
from maze import myMaze as obstacles
import robot

class MyTests(unittest.TestCase):

    @patch("sys.stdin", StringIO('HAL\nmazerun\noff\n'))
    def test_find_edge(self):
        sys.stdout = StringIO()
        obstacles.obstacleList
        robot.robot_start()

        output = sys.stdout.getvalue()
        self.assertTrue(output.find('starting maze run..') > -1)
        self.assertTrue(output.find('I am at the top edge') > -1)

    def test_compress_instruction(self):
        instruction = ["left","left","right","left", "bottom", "bottom", "top"]
        result = maze_solver.compress_instruction(instruction, [])
        self.assertEqual(result,[('left', 10), ('right', 5), ('left', 5), ('bottom', 10)])

    def test_append_handler(self):
        result = maze_solver.append_handler(10, 3, "top", "bottom")
        self.assertEqual(result,"bottom")
        result = maze_solver.append_handler(0, 3, "right", "left")
        self.assertEqual(result,"right")

    def test_make_instr(self):
        path = [(0,0),(0,5),(5,0)]
        result = maze_solver.make_instructions(path, [])
        self.assertEqual(result, [('top', 5), ('right', 5)])

    def test_backRoute(self):
        solution = {(0,10): (0,10), (0,5): (0,10), (0,0): (0,5)}
        result = maze_solver.backRoute(solution, 0, 10, 0, 0)
        self.assertEqual(result, [('top', 10)])
    
    def test_do_x_y(self):
        result = maze_solver.do_x_y(0, 0, "top", 20)
        self.assertEqual(result, (0,20))

