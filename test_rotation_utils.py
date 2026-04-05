"""Rotation test
tests the adjust_rotation() function
Author: Dmitrii Dolgov
Date: 4/5/2026
    """
from rotation_utils import adjust_rotation
import pytest


def test_100():
    """tests a 100 input"""
    assert adjust_rotation(100)==100

def test_460():
    """tests a 460 input"""
    assert adjust_rotation(460)==100

def test_820():
    """tests a 820 input"""
    assert adjust_rotation(820)==100

def test_neg_100():
    """tests a -100 input"""
    assert adjust_rotation(-100)==260

def test_neg_460():
    """tests a -460 input"""
    assert adjust_rotation(-460)==260

def test_neg_820():
    """tests a -820 input"""
    assert adjust_rotation(-820)==260

def test_type():
     """tests a string input"""
     with pytest.raises(TypeError):
         adjust_rotation('abra')
