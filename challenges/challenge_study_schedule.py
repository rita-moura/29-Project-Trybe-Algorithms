def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    count = 0
    for period in permanence_period:
        if isinstance(period, tuple) and len(period) == 2 and all(
                isinstance(time, int) for time in period):
            start_time, end_time = period
            if start_time <= target_time <= end_time:
                count += 1
        else:
            return None

    return count
