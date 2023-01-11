"""Python user-defined exceptions"""


class Error(Exception):
    """Base class for other exceptions"""

    pass


class DatabaseAlreadyExists(Exception):
    """Raised when the user tries to create a database that already exists

    Attributes:
        name -- name of the database that already exists
        message -- explanation of the error
    """

    def __init__(self, name: str, message: str = "A database with this name already exists"):
        self.name = name
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.name} -> {self.message}"


class DatabaseDoesNotExist(Exception):
    """Raised when the user tries to perform an action on a database that does not exist

    Attributes:
        name -- name of the database that does not exist
        message -- explanation of the error
    """

    def __init__(self, name: str, message: str = "A database with this name does not exist"):
        self.name = name
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.name} -> {self.message}"
