import unittest

from plane import Plane

class TestPlane(unittest.TestCase):


    def setUp(self):
        self.plane = Plane()

    def test_0_defaults(self):
        """Plane initially flying"""
        self.assertTrue(self.plane.isFlying)

    def test_1_land_changes_isFlying_to_false(self):
        self.plane.land()
        self.assertFalse(self.plane.isFlying)

    def test_2_takeoff_changes_isflying_to_true(self):
        self.plane.land()
        self.plane.take_off()
        self.assertTrue(self.plane.isFlying)

if __name__ == '__main__':
        unittest.main()
