import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from app import hello_world, add_numbers


def test_hello_world():
    assert hello_world() == "Hello, World!"


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
