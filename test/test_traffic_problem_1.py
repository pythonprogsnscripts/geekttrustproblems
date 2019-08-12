'''
This is test file for unit test of traffic
problem code file
'''

import sys
import os
sys.path.append(os.path.dirname(__file__)+"/../")
import pytest
# from unittest import TestCase
from src import traffic_problem_1 as tp


@pytest.mark.parametrize('climate, speed',          \
                        [                           \
                            ('Sunny', 0.9),        \
                            ('Windy', 0.0),         \
                            ('Rainy', 1.2)
                        ])
def test_when_climate_sunny_return_all_vechicles(climate, speed):
    '''
    This is a parametrized test case, to validate speed against
    correct input
    '''
    crater_speed = tp.getvehicles(climate)
    assert crater_speed[1] == speed

@pytest.mark.parametrize('climate, expected_output',          \
    [                           \
        ('Sunny', True),        \
        ('Windy', True),        \
        ('Rainy', True),        \
        (10, False),            \
        ('@', False)
    ])
def test_validation_of_climate_input(climate, expected_output):
    '''
    This is a parametrized test case, to validate the climate
    input
    '''
    input_validation = tp.validate_input_data(climate)
    assert input_validation == expected_output, 'Validation success'

def test_vechicle_speed_less_than_orbit_speed():
    '''
    A vehicle cannot move faster than orbit speed, Below
    is the test case to check the same
    '''
    traffic_speed = 12
    vehicles = tp.getvehicles('Sunny')
    right_speed = tp.get_orbit_time(vehicles, 10, orbit_distance=18, craters_count=20)
    assert traffic_speed == right_speed[0]['max_speed']

def test_vechicle_and_orbit2_speed():
    '''
    Check the speed condition when climate is Windy
    '''
    traffic_speed = 20
    vehicles = tp.getvehicles('Windy')
    right_speed = tp.get_orbit_time(vehicles, 20, orbit_distance=20, craters_count=10)
    assert traffic_speed == right_speed[0]['max_speed']

# class CommandLineTestCase(TestCase):
#     """
#     Base TestCase class, sets up a CLI parser
#     """
#     @classmethod
#     def test_setUpClass(cls):
#         '''
#         This function test the creation of Parser
#         '''
#         cls.parser = tp.create_parser()
