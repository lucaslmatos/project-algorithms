def study_schedule(permanence_period, target_time):

    if target_time == None or permanence_period == None:
        return None

    array_size = len(permanence_period)
    count = 0

    for index in range(array_size):
        if None in permanence_period[index]: 
            return None
        if type(permanence_period[index][0]) != int or type(permanence_period[index][1]) != int:
            return None
        if permanence_period[index][1] >= target_time and permanence_period[index][0] <= target_time:
            count += 1
    return count
