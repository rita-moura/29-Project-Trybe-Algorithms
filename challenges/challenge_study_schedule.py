def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    if not permanence_period:
        return 0

    count = 0
    for period in permanence_period:
        if not isinstance(period, tuple) or len(period) != 2 or any(not isinstance(time, int) for time in period):
            return None

        start_time, end_time = period
        if start_time <= target_time <= end_time:
            count += 1

    return count
