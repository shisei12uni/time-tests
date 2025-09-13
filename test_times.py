from times import time_range, compute_overlap_time
import pytest
import yaml

with open("fixture.yaml", "r") as f:
    data = yaml.safe_load(f)
    print(data)


@pytest.mark.parametrize("test_name", data)

def test_positive_cases(test_name):
    properties = list(test_name.values())[0]
    first_range = time_range(*properties["input_time_range1"])
    second_range = time_range(*properties["input_time_range2"])
    expected_overlap = [(start, stop) for start, stop in properties["expected"]]
    result = compute_overlap_time(first_range, second_range)
    assert result == expected_overlap


def test_input_validation():
    """input validation, does code raise error when start time > end time?"""
    expected_error_message = "end_time is smaller than start_time"
    with pytest.raises(ValueError, match=expected_error_message):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")