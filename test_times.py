from times import time_range, compute_overlap_time

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
                ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]    
    assert result == expected

def test_input_dont_overlap():
    """testing no overlap between inputs"""
    time2010 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    time2020 = time_range("2020-01-12 10:30:00", "2020-01-12 10:45:00")
    result = compute_overlap_time(time2010, time2020)
    expected = []
    assert result == expected

def test_input_both_with_several_interval():
    time1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 30)
    time2 = time_range("2010-01-12 10:30:00", "2010-01-12 11:45:00", 2, 60)
    result = compute_overlap_time(time1, time2)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:59:45'),
                ('2010-01-12 11:08:00', '2010-01-12 11:45:00')]
    assert result == expected

def test_input_ends_at_start():
    time1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    time2 = time_range("2010-01-12 12:00:00", "2010-01-12 12:10:00")
    result = compute_overlap_time(time1, time2)
    expected = []
    assert result == expected