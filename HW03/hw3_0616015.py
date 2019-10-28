import unittest
from Point_nD import Point

class Test(unittest.TestCase):

    # constructors
    def testConstructor(self):
        p1 = Point()
        self.assertEqual(str(p1), 'Point: [0, 0]')
        p2 = Point([1, 2, 3])
        self.assertEqual(str(p2), 'Point: [1, 2, 3]')
        p3 = Point((1, 2, 3))
        self.assertEqual(str(p3), 'Point: [1, 2, 3]')
        p4 = Point(p2)
        self.assertEqual(str(p4), 'Point: [1, 2, 3]')

    def testConstructorError(self):
        self.assertRaises(Exception, Point, [])
        
    # existing methods
    def testExistingMethods(self):
        p1 = Point([1, 2, 3])
        p1.moveBy([1, 0, -1])
        self.assertEqual(str(p1), 'Point: [2, 2, 2]')
        p1 = Point([1, 2, 3])
        p1.moveTo([0, 0, 0])
        self.assertEqual(str(p1), 'Point: [0, 0, 0]')
        p1 = Point([1, 2, 3])
        p2 = Point([4, 5, 6])
        self.assertEqual(p1.distanceTo(p2), 9)

    # error checking for existing methods
    def testExistingMethodsError(self):
        p1 = Point([1, 2, 3])
        p2 = Point([1, 2, 3, 4])
        self.assertRaises(Exception, p1.moveBy, [1, 0, -1, 0])
        # self.assertRaises(Exception, p1.moveTo, [1, 0, -1, 0])
        # self.assertRaises(Exception, p1.distanceTo, p2)

    # indexing
    def testIndexing(self):
        p1 = Point([1, 2, 3])
        self.assertEqual(p1[0], 1)
        self.assertEqual(p1[1], 2)
        self.assertEqual(p1[2], 3)
        p1[1] = 0
        self.assertEqual(p1[0], 1)
        self.assertEqual(p1[1], 0)
        self.assertEqual(p1[2], 3)

    # len
    def testLen(self):
        p1 = Point([1, 2, 3])
        self.assertEqual(len(p1), 3)

    # operators
    def testOperators(self):
        p1 = Point([1, 2, 3])
        p2 = Point([4, 5, 6])
        p3 = Point(p1)
        # add
        pa = Point([5, 7, 9])
        self.assertEqual(p1 + p2, pa)
        # sub
        pa = Point([-3, -3, -3])
        self.assertEqual(p1 - p2, pa)
        # greater then
        self.assertTrue(p2 > p1)
        self.assertFalse(p1 > p2)
        self.assertFalse(p1 > p3)
        # mul
        p4 = p1 * 10;
        self.assertEqual(str(p4), 'Point: [10, 20, 30]')
        # equal
        self.assertFalse(p1 == p2)
        self.assertTrue(p1 == p3)

    def testOperatorsError(self):
        p1 = Point([1, 2, 3])
        p2 = Point([4, 5, 6, 7])
        self.assertRaises(Exception, p1.__add__, p2)
        self.assertRaises(Exception, p1.__sub__, p2)
        self.assertRaises(Exception, p1.__gt__, p2)
        self.assertRaises(Exception, p1.__eq__, p2)

    def testClassMethods(self):
        p1 = Point([1, 2, 3])
        p2 = Point([1, 3, 5])
        p3 = Point([4, 7, 10])
        pa = Point([(1+1+4)/3, (2+3+7)/3, (3+5+10)/3])
        self.assertTrue(p1.centroid([p1, p2, p3]) == pa)
        self.assertTrue(Point.centroid([p1, p2, p3]) == pa)

    def testClassMethodsError(self):
        p1 = Point([1, 2, 3])
        p2 = Point([1, 3, 5])
        p3 = Point([4, 7, 10, 3])
        self.assertRaises(Exception, p1.centroid, [])
        self.assertRaises(Exception, p1.centroid, [p1, p2, p3])
        self.assertRaises(Exception, Point.centroid, [])
        self.assertRaises(Exception, Point.centroid, [p1, p2, p3])


if __name__ == '__main__':
    unittest.main()
