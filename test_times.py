from times import time_range, compute_overlap_time

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    #short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    short = time_range("2010-01-12 12:00:00", "2010-01-12 12:00:05")
    result = compute_overlap_time(large, short)
    #expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
    #            ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    expected = [("2010-01-12 12:00:00", "2010-01-12 12:00:00")]
    
    assert result == expected