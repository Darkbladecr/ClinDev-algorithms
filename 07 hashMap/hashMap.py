"""Create a hashmap."""


class HashMap:
    """A Map class with set, get and delete methods."""

    def __init__(self):
        """Initialize data."""
        self.data = dict()

    def set(self, key, value):
        """Store the value against the key."""
        self.data[str(key)] = value

    def get(self, key):
        """Get the value against the key (if any)."""
        return self.data[str(key)]

    def delete(self, key):
        """Remove the key/value pair."""
        del self.data[str(key)]

    def has(self, key):
        """Return true if value stored against the key."""
        return key in self.data
