class UserValidationError(Exception):
    """When user credentials provided are not correct"""
    pass

class EnvironmentVariableError(Exception):
    """When environment variables are not set"""
    pass
