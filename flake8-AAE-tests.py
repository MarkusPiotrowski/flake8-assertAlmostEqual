"""A module as test dummy for flake8-assertAlmostEqual."""

import unittest


class TestSelfAssertEqualDetection(unittest.TestCase):
    """Dummy for flake8-assertAlmostEqual."""

    def setUp(self):
        """Set up."""
        self.my_result = 5.0473

    def test_detection(self):
        """Detect flake8-assertAlmostEqual violoations."""
        # Simple one-liners:
        self.assertAlmostEqual(5.05, round(self.my_result, 2))
        self.assertEqual(round(self.my_result, 3), 5.047)
        # Comments (shouldn't be detected):
        # self.assertAlmostEqual(5.05, round(self.my_result, 2))
        # self.assertEqual(round(self.my_result, 3), 5.047)
        # Two-liners:
        self.assertAlmostEqual(5.05,
                               round(self.my_result, 2))
        self.assertEqual(
            round(self.my_result, 3), 5.047)
        # NOQAs:
        # This shouldn't be detected as AAE100, but has a trailing whitespace!
        self.assertAlmostEqual(5.05, round(self.my_result, 2))  # noqa: AAE100
        # This should be detected, because it's AAE110:
        self.assertEqual(round(self.my_result, 3), 5.047)  # noqa: AAE100


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
