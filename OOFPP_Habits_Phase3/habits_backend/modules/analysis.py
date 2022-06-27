"""
This module contains the Habit analysis.
We used functional programming concepts in this module.
"""


def is_tracked(habit):
    """Check if a habit is tracked. This means completed at least once."""
    return True if habit["count"] > 0 else False


def is_equal_period(habit, frequency):
    """Check if a habit has the same periodicity as the frequency e.g. Daily, Weekly."""
    return habit["repeated"].lower() == frequency.lower()


def diff_days(d1, d2):
    """Calculate the number of days between two dates."""
    return (d2 - d1).days


def diff_weeks(d1, d2):
    """Calculate the number of weeks between two dates."""
    days = (d2-d1).days
    return days//7


def diff_months(d1, d2):
    """Calculate the number of months between two dates."""
    months = (d2.year - d1.year) * 12 + d2.month - d1.month
    return months


def is_streak(d1, d2, frequency):
    """Check if to items are still a valid streak. Check depending on the frequency rules."""

    if str.lower(frequency) == 'day':
        return True if diff_days(d1, d2) <= 1 else False
    elif str.lower(frequency) == 'week':
        return True if diff_weeks(d1, d2) <= 1 else False
    elif str.lower(frequency) == 'month':
        return True if diff_months(d1, d2) <= 1 else False


def custom_filter(function, iterable, frequency):
    """Custom filter function to filter habits with the same frequency."""
    from functools import reduce

    return reduce(
        lambda items, value: items + [value] if function(value, frequency) else items,
        iterable,
        []
    )


def get_equal_periodicity(habits, frequency):
    """Return a list of habits with the same periodicity."""
    return list(custom_filter(is_equal_period, habits, frequency))


def get_tracked_habits(habits):
    """Return a list of tracked habits."""
    return list(filter(is_tracked, habits))


def get_streak_by_habit_id(completed, frequency):
    """Return a date range for the longest streak for a specific habit."""
    # Sort the list by dates ascending
    sorted_tasks = sorted(completed, key=lambda d: d.completed_date)

    # The streak is 1 till we find consecutive days
    streak = dict({"start": sorted_tasks[0].completed_date, "end": sorted_tasks[0].completed_date, "cnt": 1})
    streak_current = dict({"start": sorted_tasks[0].completed_date, "end": sorted_tasks[0].completed_date, "cnt": 1})

    for i in range(len(sorted_tasks)-1):
        if is_streak(sorted_tasks[i].completed_date, sorted_tasks[i+1].completed_date, frequency):
            streak_current['end'] = sorted_tasks[i+1].completed_date
            streak_current['cnt'] += 1
            # Check if the current streak is longer than the previous longest streak
            if streak_current['cnt'] > streak['cnt']:
                streak = streak_current.copy()
        else:
            # Streak was broken reset count and start with next streak
            streak_current['start'] = sorted_tasks[i+1].completed_date
            streak_current['cnt'] = 1

    return streak
