# ================================================ #
# Author: Darshan Gadkari
# Date: Dec 6, 2019
# Bink's Coding Test
# ================================================ #

# imports
import pytest
from solution import Solution
import pandas as pd
from datetime import datetime

# create a fixture that can be used by all the test cases
@pytest.fixture(name='solution')
def get_solution_object():
    return Solution()

# test to assert the number of records of requirements 1 output
def test_requirement_1_shape_0(solution):
    assert solution.requirement_1().shape[0] == 5

# test to assert the number of columns of requirements 1 output
def test_requirement_1_shape_1(solution):
    assert solution.requirement_1().shape[1] == 11

# test to assert the number of records of requirements 2 output
def test_requirement_2_shape_0(solution):
    assert solution.requirement_2()[0].shape[0] == 4

# test to assert the number of columns of requirements 2 output
def test_requirement_2_shape_1(solution):
    assert solution.requirement_2()[0].shape[1] == 11

# test to assert the outout of requirements 2 total rent
def test_requirement_2_total_rent(solution):
    assert solution.requirement_2()[1] == 46500.00

# test to assert the outout of requirements 3 is a string (json as a string)
def test_requirement_3_shape_output_is_a_string(solution):
    assert isinstance(solution.requirement_3()[0], str)

# test to assert the number of keys of requirements 3 output dict
def test_requirement_3_dict_number_of_keys(solution):
    assert len(solution.requirement_3()[1].keys()) == 15

# test to assert the number of items of requirements 3 output dict
def test_requirement_3_dict_number_of_items(solution):
    assert len(solution.requirement_3()[1].items()) == 15

# test to assert the number of records of requirements 4 output
def test_requirement_4_shape_0(solution):
    assert solution.requirement_4().shape[0] == 5

# test to assert the number of columns of requirements 4 output
def test_requirement_4_shape_1(solution):
    assert solution.requirement_4().shape[1] == 11

# test the left bound of the date range of requirements 4
def test_requirement_4_before_date_range(solution):
    req_4_before_date_range = solution.requirement_4().copy()
    req_4_before_date_range['Lease Start Date'] = pd.to_datetime(req_4_before_date_range['Lease Start Date'])
    assert req_4_before_date_range[req_4_before_date_range['Lease Start Date'] < datetime(1999, 6, 1, 0, 0)].shape[0] == 0
    assert req_4_before_date_range[req_4_before_date_range['Lease Start Date'] < datetime(1999, 6, 1, 0, 0)].shape[1] == 11

# test the right bound of the date range of requirements 4
def test_requirement_4_after_date_range(solution):
    req_4_after_date_range = solution.requirement_4().copy()
    req_4_after_date_range['Lease Start Date'] = pd.to_datetime(req_4_after_date_range['Lease Start Date'])
    assert req_4_after_date_range[req_4_after_date_range['Lease Start Date'] >= datetime(2007, 9, 1, 0, 0)].shape[0] == 0
    assert req_4_after_date_range[req_4_after_date_range['Lease Start Date'] >= datetime(2007, 9, 1, 0, 0)].shape[1] == 11

# test the date range of requirements 4
def test_requirement_4_within_date_range(solution):
    req_4_within_date_range = solution.requirement_4().copy()
    req_4_within_date_range['Lease Start Date'] = pd.to_datetime(req_4_within_date_range['Lease Start Date'])
    assert req_4_within_date_range[(req_4_within_date_range['Lease Start Date'] >= datetime(1999, 6, 1, 0, 0)) & \
    (req_4_within_date_range['Lease Start Date'] < datetime(2007, 9, 1, 0, 0))].shape[0] == 5
    assert req_4_within_date_range[(req_4_within_date_range['Lease Start Date'] >= datetime(1999, 6, 1, 0, 0)) & \
    (req_4_within_date_range['Lease Start Date'] < datetime(2007, 9, 1, 0, 0))].shape[1] == 11

