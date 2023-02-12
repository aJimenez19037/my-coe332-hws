from analyze_water import calculate_turbidity,calculate_minimum_time
import pytest

def test_calculate_turbidity():
    assert calculate_turbidity(1.025,1.104) == 64.836
    assert calculate_turbidity(1,1) == 57.296
def test_calculate_minimum_time():
    assert calculate_minimum_time(40) == 183
    assert calculate_minimum_time(1) == 0
