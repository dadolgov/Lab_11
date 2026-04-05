"""Rotation test
tests the adjust_rotation() function
Author: Dmitrii Dolgov
Date: 4/5/2026
    """
from rotation_utils import adjust_rotation

"""Input: 100 -> Expected Output: 100
Input: 460 -> Expected Output: 100
Input: 820 -> Expected Output: 100
Input: -100 -> Expected Output: 260
Input: -460 -> Expected Output: 260
Input: -820 -> Expected Output: 260
Non-Numeric Input: You must write a test 
that uses pytest.raises(TypeError) to verify the function correctly raises a 
TypeError when given a string (e.g., "abc").
    """


def test_100():
    assert adjust_rotation(100)==100

def test_460():
    assert adjust_rotation(460)==100

def test_820():
    assert adjust_rotation(820)==100

def test_neg_100():
    assert adjust_rotation(-100)==260

def test_neg_460():
    assert adjust_rotation(-460)==260

def test_neg_820():
    assert adjust_rotation(-820)==260