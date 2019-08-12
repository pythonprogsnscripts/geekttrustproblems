'''
This is test file for unit test of traffic
problem code file
'''

import sys
import os
sys.path.append(os.path.dirname(__file__)+"/../")
import pytest
from src import traffic_problem_1 as tp


@pytest.mark.parametrize('climate, speed',          \
                        [                           \
                            ('Sunny', -0.1),        \
                            ('Windy', 0.0),         \
                            ('Rainy', 0.2)
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
    assert input_validation == expected_output
