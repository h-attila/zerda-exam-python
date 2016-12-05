# Write unittests for this function:

import unittest

def count_letter_in_string(string, letter):
  if type(string) != str:
    return 0
  count = 0
  for current_letter in string:
    if current_letter == letter:
      count += 1
  return count


class TestForExerciseThird(unittest.TestCase):

    def test_CheckNormalWorking(self):
        self.assertEqual(count_letter_in_string('almafa alatt alszik alma', 'a'), 8)

    def test_CheckFirstInputNotString(self):
        self.assertEqual(count_letter_in_string(12345, 'a'), 0)

    def test_CheckSecondInputNotString(self):
        self.assertEqual(count_letter_in_string('almafa alatt alszik alma', 5), 0)

    def test_CheckGivenEmptyStringInput(self):
        self.assertEqual(count_letter_in_string('', 'a'), 0)

    def test_CheckGivenSecondInputAsList(self):
        self.assertEqual(count_letter_in_string('almafa alatt alszik alma', ['a', 'b']), 0)


if __name__ == '__main__':
    unittest.main()