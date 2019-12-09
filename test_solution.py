import pytest
from solution import Solution
import pandas as pd
from datetime import datetime

@pytest.fixture(name='solution')
def get_solution_object():
    return Solution()

def test_requirement_1_shape_0(solution):
    assert solution.requirement_1().shape[0] == 5

def test_requirement_1_shape_1(solution):
    assert solution.requirement_1().shape[1] == 11

def test_requirement_2_shape_0(solution):
    assert solution.requirement_2()[0].shape[0] == 4

def test_requirement_2_shape_1(solution):
    assert solution.requirement_2()[0].shape[1] == 11

def test_requirement_2_total_rent(solution):
    assert solution.requirement_2()[1] == 46500.00

def test_requirement_3_shape_output_is_a_string(solution):
    assert isinstance(solution.requirement_3()[0], str)

def test_requirement_3_dict_number_of_keys(solution):
    assert len(solution.requirement_3()[1].keys()) == 15

def test_requirement_3_dict_number_of_items(solution):
    assert len(solution.requirement_3()[1].items()) == 15

def test_requirement_4_shape_0(solution):
    assert solution.requirement_4().shape[0] == 5

def test_requirement_4_shape_1(solution):
    assert solution.requirement_4().shape[1] == 11

def test_requirement_4_before_date_range(solution):
    req_4_before_date_range = solution.requirement_4().copy()
    req_4_before_date_range['Lease Start Date'] = pd.to_datetime(req_4_before_date_range['Lease Start Date'])
    assert req_4_before_date_range[req_4_before_date_range['Lease Start Date'] < datetime(1999, 6, 1, 0, 0)].shape[0] == 0
    assert req_4_before_date_range[req_4_before_date_range['Lease Start Date'] < datetime(1999, 6, 1, 0, 0)].shape[1] == 11

def test_requirement_4_after_date_range(solution):
    req_4_after_date_range = solution.requirement_4().copy()
    req_4_after_date_range['Lease Start Date'] = pd.to_datetime(req_4_after_date_range['Lease Start Date'])
    assert req_4_after_date_range[req_4_after_date_range['Lease Start Date'] >= datetime(2007, 9, 1, 0, 0)].shape[0] == 0
    assert req_4_after_date_range[req_4_after_date_range['Lease Start Date'] >= datetime(2007, 9, 1, 0, 0)].shape[1] == 11

def test_requirement_4_within_date_range(solution):
    req_4_within_date_range = solution.requirement_4().copy()
    req_4_within_date_range['Lease Start Date'] = pd.to_datetime(req_4_within_date_range['Lease Start Date'])
    assert req_4_within_date_range[(req_4_within_date_range['Lease Start Date'] >= datetime(1999, 6, 1, 0, 0)) & \
    (req_4_within_date_range['Lease Start Date'] < datetime(2007, 9, 1, 0, 0))].shape[0] == 5
    assert req_4_within_date_range[(req_4_within_date_range['Lease Start Date'] >= datetime(1999, 6, 1, 0, 0)) & \
    (req_4_within_date_range['Lease Start Date'] < datetime(2007, 9, 1, 0, 0))].shape[1] == 11

