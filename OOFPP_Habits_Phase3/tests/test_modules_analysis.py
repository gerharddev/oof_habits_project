import datetime
import habits_backend.modules.analysis as analysis

# Test data
habit = {
    "count": 0,
    "repeated": "Daily"
}


def test_is_tracked_true():
    """Test that is_tracked return true if the count is greater than 0."""
    habit["count"] = 1
    value = analysis.is_tracked(habit)
    assert value is True


def test_is_tracked_false():
    """Test that is_tracked return false if the count is 0."""
    habit["count"] = 0
    value = analysis.is_tracked(habit)
    assert value is False


def test_is_equal_period_true():
    """Test if a habit has the same periodicity as the frequency."""
    habit["repeated"] = "Daily"
    frequency = "DAILY"
    value = analysis.is_equal_period(habit, frequency)
    assert value is True


def test_is_equal_period_false():
    """Test if a habit has the different periodicity as the frequency."""
    habit["repeated"] = "weekly"
    frequency = "daily"
    value = analysis.is_equal_period(habit, frequency)
    assert value is False


# Day tests
def test_diff_days_less_than_one_day():
    """Test if the difference between two dates is one day."""
    date1 = datetime.datetime(2022, 4, 29, 14, 17, 45)
    date2 = datetime.datetime(2022, 4, 29, 23, 17, 45)
    value = analysis.diff_days(date1, date2)
    assert value == 0


def test_diff_days_one_day_exact():
    """Test if the difference between two dates is one day."""
    date1 = datetime.datetime(2022, 4, 29, 14, 17, 45)
    date2 = datetime.datetime(2022, 4, 30, 14, 17, 45)
    value = analysis.diff_days(date1, date2)
    assert value == 1


def test_diff_days_one_day_25_hours():
    """
    Test if the difference between two dates is one day.
    Should still return 1. Only the days is taken into consideration for the test.
    """
    date1 = datetime.datetime(2022, 4, 29, 14, 17, 45)
    date2 = datetime.datetime(2022, 4, 30, 15, 17, 45)
    value = analysis.diff_days(date1, date2)
    assert value == 1


def test_diff_days_two_days():
    """
    Test if the difference between two dates is two day.
    Should still return 2. Only the days is taken into consideration for the test.
    """
    date1 = datetime.datetime(2022, 4, 29, 14, 17, 45)
    date2 = datetime.datetime(2022, 5, 1, 15, 17, 45)
    value = analysis.diff_days(date1, date2)
    assert value == 2


def test_diff_days_one_day_year():
    """
    Test if the difference between two dates is 366 days.
    """
    date1 = datetime.datetime(2022, 4, 29, 14, 17, 45)
    date2 = datetime.datetime(2023, 4, 30, 15, 17, 45)
    value = analysis.diff_days(date1, date2)
    assert value == 366


# Week tests
def test_diff_weeks_less_than_one_week():
    """Test if the difference between two dates less than one week is valid."""
    date1 = datetime.datetime(2022, 5, 1, 14, 17, 45)
    date2 = datetime.datetime(2022, 5, 7, 14, 17, 45)
    value = analysis.diff_weeks(date1, date2)
    assert value == 0


def test_diff_weeks_one_week_exact():
    """Test if the difference between two dates is one week."""
    date1 = datetime.datetime(2022, 5, 1, 14, 17, 45)
    date2 = datetime.datetime(2022, 5, 8, 14, 17, 45)
    value = analysis.diff_weeks(date1, date2)
    assert value == 0


def test_diff_weeks_greater_than_one_week():
    """Test if the difference between two dates is greater than one week."""
    date1 = datetime.datetime(2022, 5, 1, 14, 17, 45)
    date2 = datetime.datetime(2022, 5, 9, 15, 17, 45)
    value = analysis.diff_weeks(date1, date2)
    assert value == 2


# Month Tests
def test_diff_months_less_than_one_week():
    """Test if the difference between two dates less than one month is valid."""
    date1 = datetime.datetime(2022, 5, 1, 14, 17, 45)
    date2 = datetime.datetime(2022, 5, 31, 14, 17, 45)
    value = analysis.diff_months(date1, date2)
    assert value == 0


def test_diff_months_one_month_exact():
    """Test if the difference between two dates is one month."""
    date1 = datetime.datetime(2022, 5, 1, 14, 17, 45)
    date2 = datetime.datetime(2022, 6, 1, 14, 17, 45)
    value = analysis.diff_months(date1, date2)
    assert value == 1


def test_diff_months_one_month_not_exact():
    """Test if the difference between two dates is greater than one month."""
    date1 = datetime.datetime(2022, 5, 1, 14, 17, 45)
    date2 = datetime.datetime(2022, 6, 9, 15, 17, 45)
    value = analysis.diff_months(date1, date2)
    assert value == 1


def test_diff_months_greater_than_one_month():
    """Test if the difference between two dates is greater than one month."""
    date1 = datetime.datetime(2022, 5, 1, 14, 17, 45)
    date2 = datetime.datetime(2022, 7, 9, 15, 17, 45)
    value = analysis.diff_months(date1, date2)
    assert value == 2
