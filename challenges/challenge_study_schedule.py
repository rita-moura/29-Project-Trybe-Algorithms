def is_valid_period(period):
    return isinstance(period, tuple) and len(period) == 2 and all(
            isinstance(time, int) for time in period)


def count_valid_periods(permanence_period, target_time):
    count = 0
    for period in permanence_period:
        if is_valid_period(period):
            start_time, end_time = period
            if start_time <= target_time <= end_time:
                count += 1
        else:
            return None
    return count


def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    if not permanence_period:
        return 0

    return count_valid_periods(permanence_period, target_time)
