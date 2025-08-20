import unittest
from main import find_missing_ranges

class TestMissingFrames(unittest.TestCase):
    def test_example_case(self):
        frames = [1, 2, 3, 5, 6, 10, 11, 16]
        expected = {
            "gaps": [[4, 4], [7, 9], [12, 15]],
            "longest_gap": [12, 15],
            "missing_count": 8
        }
        self.assertEqual(find_missing_ranges(frames), expected)

    def test_no_missing(self):
        frames = [1, 2, 3, 4, 5]
        expected = {"gaps": [], "longest_gap": [], "missing_count": 0}
        self.assertEqual(find_missing_ranges(frames), expected)

    def test_single_missing(self):
        frames = [1, 2, 4, 5]
        expected = {"gaps": [[3, 3]], "longest_gap": [3, 3], "missing_count": 1}
        self.assertEqual(find_missing_ranges(frames), expected)

if __name__ == "__main__":
    unittest.main()
