#!/usr/bin/env python

"""Tests for `calculator` package."""

import pytest

from click.testing import CliRunner

from calculator.calculator import Calc
from calculator import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'calculator.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


def test_add_two_numbers():
    """Test addition of two numbers"""

    c = Calc()
    result = c.add(3, 5)
    assert result == 8


def test_add_many_numbers():
    """Test addition of multipy numbers"""

    s = range(100)
    assert Calc().add(*s) == 4950


def test_subtract_two_numbers():
    """Test the difference between two numbers"""

    res = Calc().subtract(10, 3)
    assert res == 7


def test_multiply_two_numbers():
    """Test product of two numbers"""

    res = Calc().multiply(6, 4)
    assert res == 24


def test_multiply_mul_numbers():
    """Test product of multiple numbers"""

    c = Calc()
    with pytest.raises(ValueError):
        c.multiply(3, 0)


def test_divide_two_numbers():
    """Test division of two numbers"""

    res = Calc().divide(8, 4)
    assert res == 2


def test_avg_correct_average():
    """Test average of a list"""
    c = Calc()

    res = c.avg([2, 5, 12, 98])
    assert res == 29.25


def test_avg_removes_upper_outliers():
    """Test average of a list without upper threshold"""

    c = Calc()

    res = c.avg([2, 5, 12, 98], ut=80)
    assert res == pytest.approx(6.333333)


def test_avg_removes_lower_outliers():
    """Test average of a list without lower threshold"""

    c = Calc()
    res = c.avg([2, 5, 12, 98], lt=10)
    assert res == pytest.approx(55)

