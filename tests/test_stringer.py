import unittest
from stringer.stringer import Stringer


class TestStringer(unittest.TestCase):

    def test_to_upper(self):
        ostr = "This is a mixed case string."
        s = Stringer()
        ustr = s.to_upper(ostr)

        self.assertEqual("THIS IS A MIXED CASE STRING", ustr)

    def test_to_lower(self):
        ostr = "This is a mixed case string."
        s = Stringer()
        lstr = s.to_upper(ostr)

        self.assertEqual("this is a mixed case string", lstr)
