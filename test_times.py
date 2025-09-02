from times import time_range, compute_overlap_time
import pytest

@pytest.mark.parametrize("input_time_range1,input_time_range2,expected",
                         [(time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
                           time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
                           [('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
                            ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]),
                            (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
                             time_range("2020-01-12 10:30:00", "2020-01-12 10:45:00"),
                             []),
                             (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 30),
                              time_range("2010-01-12 10:30:00", "2010-01-12 11:45:00", 2, 60),
                              [('2010-01-12 10:30:00', '2010-01-12 10:59:45'),
                               ('2010-01-12 11:00:15', '2010-01-12 11:07:00'),
                               ('2010-01-12 11:08:00', '2010-01-12 11:45:00')]), 
                               (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
                                time_range("2010-01-12 12:00:00", "2010-01-12 12:10:00"),
                                [])
                                ])

def test_positive_cases(input_time_range1, input_time_range2, expected):
    result = compute_overlap_time(input_time_range1, input_time_range2)
    assert result == expected


def test_input_validation():
    """input validation, does code raise error when start time > end time?"""
    with pytest.raises(ValueError):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")