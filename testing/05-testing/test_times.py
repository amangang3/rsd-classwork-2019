import times
    
def test_given_input():
    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = (times.overlap_time(large, short))
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected    

#test_given_input() #this runs the function 


def test_class_time():
    time_range_1 = ("2019-10-31 10:00:00", "2019-10-31 13:00:00")
    time_range_2 = ("2019-10-31 10:05:00", "2019-10-31 12:55:00", 3, 600) #small time is in the big time 
    # large = times.time_range(time_range_1) #why doesn't this work 
    # short = times.time_range(time_range_2)
    large = times.time_range("2019-10-31 10:00:00", "2019-10-31 13:00:00")
    short = times.time_range("2019-10-31 10:05:00", "2019-10-31 12:55:00", 3, 600)
    result = (times.overlap_time(large, short))
    expected = short
    assert result == expected    

test_class_time()


