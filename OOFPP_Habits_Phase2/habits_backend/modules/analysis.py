"""
This module contains the Habit analysis class.

We will use functional programming concepts.
"""


def is_tracked(habit):
    """Check if a habit is tracked. This means completed at least once."""
    return True if habit["count"] > 0 else False


def is_equal_period(habit, frequency):
    """Check if a habit is tracked. This means completed at least once."""
    return habit["repeated"].lower() == frequency.lower()


def is_streak(item1, item2, frequency):
    """Check if to items are still a valid streak. Check depending on the frequency rules."""
    import datetime

    if str.lower(frequency) == 'day':
        diff = item2 - item1
        return True if diff.days <= 1 else False


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


# def range(item1, item2):
#     return

def get_streak_by_habit_id(completed, frequency):
    """Return a date range for the longest streak for a specific habit."""
    # Sort the list by dates ascending
    sorted_tasks = sorted(completed, key=lambda d: d.completed_date)
    new_list = []   #TODO: Add 1st date and blank date
    streak_cnt = 0
    for i in range(len(sorted_tasks)-1):
        if is_streak(sorted_tasks[i].completed_date, sorted_tasks[i+1].completed_date, frequency):
            print('Streak - Extend end date')
        else:
            print(str(sorted_tasks[1].completed_date))
            print(str(sorted_tasks[i].completed_date))
            print('Streak - broken')
        # if sorted_tasks[i].completed_date and sorted_tasks[i+1].completed_date follow, count for streak
        # new_list.append(dictsorted_tasks[i].completed_date + sorted_tasks[i+1].completed_date)


    # from functools import reduce
    #
    # new_list = reduce(lambda a, b: dict([a, b]), sorted_tasks)
    # Use functional
    # Sort list by date
    # Loop over list and get streaks depending on frequency - day, week
    # Return longest streak

    return "not implemented"
