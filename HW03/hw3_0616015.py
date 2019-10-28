import unittest
from Point_nD import Point

class Test(unittest.TestCase):

    # constructors
    def testConstructor_default(self):
        p1 = Point()
        self.assertEqual(str(p1), 'Point: [0, 0]')
    def testConstructor_byList(self):
        p2 = Point([1, 2, 3])
        self.assertEqual(str(p2), 'Point: [1, 2, 3]')
    def testConstructor_byTuple(self):
        p3 = Point((1, 2, 3))
        self.assertEqual(str(p3), 'Point: [1, 2, 3]')
    def testConstructor_byCopyConstructor(self):
        p2 = Point([1, 2, 3])
        p4 = Point(p2)
        self.assertEqual(str(p4), 'Point: [1, 2, 3]')
        
    # existing methods
    def testExistingMethods_moveBy(self):
        p1 = Point([1, 2, 3])
        p1.moveBy([1, 0, -1])
        self.assertEqual(str(p1), 'Point: [2, 2, 2]')
    def testExistingMethods_moveTo(self):
        p1 = Point([1, 2, 3])
        p1.moveTo([0, 0, 0])
        self.assertEqual(str(p1), 'Point: [0, 0, 0]')
    def testExistingMethods_distanceTo(self):
        p1 = Point([1, 2, 3])
        p2 = Point([4, 5, 6])
        self.assertEqual(p1.distanceTo(p2), 9)

    # error checking for existing methods
    def testError_moveBy(self):
        p1 = Point([1, 2, 3])
        # print(callable(p1.moveBy([1, 0, -1, 0])))
        # p1.moveBy([1, 0, -1, 0])
        self.assertRaises(Exception, p1.moveBy, [1, 0, -1, 0])











if __name__ == '__main__':
    unittest.main()
