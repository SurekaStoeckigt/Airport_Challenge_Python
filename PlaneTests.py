import unittest

from plane import *

class TestPlane(unittest.TestCase):


    def setUp(self):
        self.plane = Plane()

    # def test_0_defaults(self):
    #     """Plane initially flying"""
    #     self.assertTrue(self.plane.isFlying)

    # def test_1_land_changes_isFlying_to_false(self):
    #     """Plane changes status when landed"""
    #     self.plane.land()
    #     self.assertFalse(self.plane.isFlying)

    # def test_2_takeoff_changes_isflying_to_true(self):
    #     """Plane changes status twice when landed and taking off"""
    #     self.plane.land()
    #     self.plane.take_off()
    #     self.assertTrue(self.plane.isFlying)

    # def test_3_raise_exception_if_trying_to_takeoff_while_flying(self):
    #     self.plane.land()
    #     self.plane.take_off()
    #     with self.assertRaisesRegexp(Exception, 'Plane cannot takeoff while flying'):
    #         self.plane.take_off()

    def test_2_set_request(self):
        self.plane.setRequestToLand()
        self.assertTrue(self.plane.requestedToLand)

if __name__ == '__main__':
        unittest.main()
