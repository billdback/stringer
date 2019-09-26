

class Stringer:
    """
    Simple class that will convert strings to upper and lower and write the results.
    """

    def __init__(self):
        """Creates a new stringer."""
        pass

    @staticmethod
    def to_upper(s):
        """
        Converts the string to upper case.
        :param s: The string to convert.
        :type s: str
        :return: The string in upper case.
        """
        return s.upper()

    @staticmethod
    def to_lower(s):
        """
        Converts the string to lower case.
        :param s: The string to convert.
        :type s: str
        :return: The string in lower case.
        """
        return s.lower()
