import sys
import os

sys.path.append(os.path.dirname(__file__)+"/../")
from src.main import create_parser
from unittest import TestCase

class CommandLineTestCase(TestCase):
    """
    Base TestCase class, sets up a CLI parser
    """
    @classmethod
    def setUpClass(cls):
        parser = create_parser()
        cls.parser = parser