import pytest
from src.rpn.parser import RPNParser

parser = RPNParser()

def test_rpn_evaluation():
    assert parser.evaluate("3 4 +") == 7

def test_rpn_subtraction():
    assert parser.evaluate("10 5 -") == 5

def test_rpn_multiplication():
    assert parser.evaluate("6 2 *") == 12

def test_rpn_division():
    assert parser.evaluate("8 4 /") == 2

def test_rpn_invalid():
    assert parser.evaluate("3 +") is None

def test_rpn_complex_expression():
    assert parser.evaluate("5 1 2 + 4 * + 3 -") == 14
