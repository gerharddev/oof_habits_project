from sqlalchemy import Integer,String

class Frequency():
    """Frequency Model."""

    __tablename__ = 'frequency'

    id = Integer(primary_key=True)
    name = String(maxlength=50)
    description = String(maxlength=255)
    # TODO: frequency date

    def __init__(self, name, description):
        """Initialize the frequency model."""
        self.name = name
        self.description = description