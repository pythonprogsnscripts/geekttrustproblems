'''
This is test file for main program
Though it is not easy to test the argprase function,
have tried to test the main file
'''
import sys
import os

sys.path.append(os.path.dirname(__file__)+"/../")
from unittest import TestCase
from src.traffic_problem_1 import create_parser

class CommandLineTestCase(TestCase):
    """
    Base TestCase class, sets up a CLI parser
    """
    @classmethod
    def setUpClass(cls):
        '''
        This function test the creation of Parser
        '''
        parser = create_parser()
        cls.parser = parser
