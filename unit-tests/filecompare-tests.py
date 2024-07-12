import unittest

import linecompare as lc


class TestFileCompare(unittest.TestCase):
  def test_clean_line_spaces_left(self):     
    lcO = lc.LineCompare()
    self.assertEqual(
      lcO.clean_line('  hello'),
      'hello'
    )
