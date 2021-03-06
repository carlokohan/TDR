"""
    Collection of application specific custom errors
"""


class FileFormException(Exception):
    """
        Data is not rectangular (same length with first line)
    """
    pass


class InvalidDataException(Exception):
    """
        Data contains other characters besides 'X', 'O', and ' ' (space)
    """
    pass
