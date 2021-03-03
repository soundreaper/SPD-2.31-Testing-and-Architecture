import unittest
from unittest.mock import patch
import pytest
import math

from exercise3 import read_input, calculate_stat, print_stat


@pytest.fixture(scope="function")
def grades():
    return [100, 88, 96, 75, 65]


@pytest.fixture
def mean():
    return 84.8


@pytest.fixture
def sd():
    return 13.075167302944921


@pytest.fixture
def expected_printout():
    return "****** Grade Statistics ******\nThe grades's mean is: 84.8\nThe population standard deviation of grades is:  13.075\n****** END ******\n"


class TestInput(unittest.TestCase):

    @patch('builtins.input', side_effect=[100, 88, 96, 75, 65])
    def test_read_input(self, grades):
        result = read_input()
        self.assertEqual(result, [100, 88, 96, 75, 65])


def test_calculate_stat(grades, mean, sd):
    m, s = calculate_stat(grades)
    assert math.isclose(m, mean, abs_tol=0.0001)
    assert math.isclose(s, sd, abs_tol=0.01)


def test_print_stat(capsys, mean, sd, expected_printout):
    print_stat(mean, sd)
    captured = capsys.readouterr()
    assert captured.out == expected_printout
