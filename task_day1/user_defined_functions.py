
'''What are User-Defined Exceptions?

They are custom exception classes you create to signal specific error conditions or events in your code.
They allow you to tailor exception handling to your application's needs and provide more informative error messages.
Creating User-Defined Exceptions:


Python
class InvalidAgeError(ValueError):
    def __init__(self, age):
        super().__init__(f"Invalid age: {age}. Age must be positive.")


'''


class MyCustomError(Exception):
    """Base class for custom exceptions in this module."""
    pass

class InvalidInputError(MyCustomError):
    """Raised when invalid input is provided."""
    pass

class FileFormatError(MyCustomError):
    """Raised when a file format is incorrect."""
    pass
class InvalidAgeError(ValueError):
    def __init__(self, age):
        super().__init__(f"Invalid age: {age}. Age must be positive.")
