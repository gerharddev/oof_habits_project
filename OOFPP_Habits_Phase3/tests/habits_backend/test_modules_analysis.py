import habits_backend.modules.analysis as analysis

# Test data
habit = {
    "count": 0
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
