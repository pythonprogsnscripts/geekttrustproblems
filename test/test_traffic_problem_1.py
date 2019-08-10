import sys
import os
sys.path.append(os.path.dirname(__file__)+"/../")
from src import traffic_problem_1 as tp
import pytest

@pytest.mark.parametrize('climate, speed',          \
                        [                           \
                            ('Sunny', -0.1),        \
                            ('Windy', 0.0),         \
                            ('Rainy', 0.2)
                        ])
def test_when_climate_sunny_return_all_vechicles(climate, speed):
    crater_speed = tp.getvehicles(climate)
    assert crater_speed[1] == speed