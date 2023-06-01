def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    if not permanence_period:
        return 0

    time_list = []
    for period in permanence_period:
        if not isinstance(period, tuple) or len(period) != 2 or \
                any(not isinstance(time, int) for time in period):
            return None

        start_time, end_time = period
        time_list.extend(range(start_time, end_time + 1))

    count = time_list.count(target_time)
    return count
