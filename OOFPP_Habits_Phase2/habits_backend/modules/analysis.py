"""
This module contains the Habit analysis class.

We will use functional programming concepts.
"""


def is_tracked(habit):
    """Check if a habit is tracked. This means completed at least once."""
    return True if habit["count"] > 0 else False


def get_tracked_habits(habits):
    """Return a list of tracked habits."""
    return list(filter(is_tracked, habits))
