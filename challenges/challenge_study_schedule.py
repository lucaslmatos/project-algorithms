def study_schedule(permanence_period, target_time):

    if target_time is None or permanence_period is None:
        return None

    array_size = len(permanence_period)
    count = 0

    for index in range(array_size):
        arg_one = permanence_period[index][0]
        arg_two = permanence_period[index][1]
        if (None in permanence_period[index] or
                type(arg_one) != int or
                type(arg_two) != int):
            return None
        if arg_two >= target_time and arg_one <= target_time:
            count += 1
    return count
