from operator import add, sub, mul, gt, eq, and_
from functools import reduce

class Point:
    # __init__ function is the constructor
    def __init__(self, ref=[0, 0]):
        try:
            self.coords = list(ref)
        except TypeError:
            self.coords = ref.coords
        self.dim = len(self.coords)

    @staticmethod
    def errMsg( _type):
        if _type == 'dim':
            print("\033[1;91mValueError:\033[0m The coordinate and point dimensionalities should be consistent.")
        if _type == 'plist':
            print("\033[1;91mRuntimeError:\033[0m The pList should not be empty.")
        return

    #move the point by x,y
    def moveBy(self, move=[0, 0]):
        try:
            if self.dim != len(move):
                raise ValueError
            self.coords = list(map(add, self.coords, move))
        except ValueError:
            self.errMsg('dim')

    #move the point to x,y
    def moveTo(self, move=[0, 0]):
        try:
            if self.dim != len(move):
                raise ValueError
            self.coords = move
        except ValueError:
            self.errMsg('dim')

    #calculate Hamming distance between two points
    def distanceTo(self, p2):
        try:
            if self.dim != len(p2.coords):
                raise ValueError
            def getDistance(a, b):
                return abs(a - b)
            return reduce(add, list(map(getDistance, self.coords, p2.coords)))
        except ValueError:
            self.errMsg('dim')

    # __str__ generates string representation of objects
    def __str__(self):
        return str(self.coords)

    # magic functions
    def __getitem__(self, key):
        return self.coords[key]

    def __setitem__(self, key, value):
        self.coords[key] = value

    def __len__(self):
        return self.dim

    # operator
    def __add__(self, p2):
        try:
            if self.dim != len(p2.coords):
                raise ValueError
            return Point(list(map(add, self.coords, p2.coords)))
        except ValueError:
            self.errMsg('dim')
        return

    def __sub__(self, p2):
        try:
            if self.dim != len(p2.coords):
                raise ValueError
            return Point(list(map(sub, self.coords, p2.coords)))
        except ValueError:
            self.errMsg('dim')
        return

    def __gt__(self, p2):
        try:
            if self.dim != len(p2.coords):
                raise ValueError
            return reduce(and_, list(map(gt, self.coords, p2.coords)))
        except ValueError:
            self.errMsg('dim')
        return

    def __mul__(self, scalar):
        return Point(list(map(lambda x: x * scalar, self.coords)))

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __eq__(self, p2):
        try:
            if self.dim != len(p2.coords):
                raise ValueError
            return reduce(and_, list(map(eq, self.coords, p2.coords)))
        except ValueError:
            self.errMsg('dim')
        return

    @classmethod
    def centroid(cls, pList=[]):
        try:
            if len(pList) == 0:
                raise RuntimeError
            dim = len(pList[0])
            for p in pList:
                if len(p) != dim:
                    raise ValueError
            n = len(pList)
            cls = reduce(add, pList)
            cls = cls * (1 / n)
            return cls
        except RuntimeError:
            cls.errMsg('plist')
        except ValueError:
            cls.errMsg('dim')

p0=Point([336,580,496,16,199])
print(p0)
p1=Point((57,278,823,925,912))
print(p1)
p2=Point(p0)
print(p2)
p3=Point(p1)
print(p3)
p4=Point(p1)
print(p4)
p5=Point([498,743,647,896,745])
print(p5)
p6=Point(p5)
print(p6)
p7=Point(p0)
print(p7)
p8=Point((732,102,181,68,34))
print(p8)
p9=Point((84,233,935,494,864))
print(p9)
p9.moveBy([849,254,603,729,172])
print(p9)
p3.distanceTo(p1)
print(p3)
p2.distanceTo(p6)
print(p2)
p0.distanceTo(p3)
print(p0)
p2.moveBy([165,444,678,585,479])
print(p2)
p1.distanceTo(p0)
print(p1)
p7.moveBy([105,287,56,306,893])
print(p7)
p7.moveTo([353,760,792,789,133])
print(p7)
p4.moveBy([107,107,359,604,624])
print(p4)
p4.moveTo([282,694,583,347,41])
print(p4)
p7[0]=89
print(p7)
p2[4]=48
print(p2)
print(p2[4])
p4[2]=437
print(p4)
p6[2]=66
print(p6)
p3[1]=300
print(p3)
p8[1]=251
print(p8)
p5[3]=96
print(p5)
print(p7[0])
print(p3[0])
print(p1==p9)
print(p4==p1)
print(20.8*p8)
print(p4>p7)
print(2.4*p9)
print(p5==p7)
print(p0+p8)
print(p6>p0)
print(p9==p8)
print(21.6*p9)
p8=p1.centroid([p9,p3,p2,p1,p0,p9,p5,p2,p4,p6])
print(p8)
p1=Point.centroid([p3,p6,p7,p4,p6,p9,p4,p2,p7,p2])
print(p1)
p4=p8.centroid([p3,p5,p5,p1,p1,p8,p2,p4,p0,p3])
print(p4)
p6=Point.centroid([p0,p1,p5,p6,p2,p5,p9,p8,p2,p3])
print(p6)
p4=Point.centroid([p8,p8,p9,p2,p2,p1,p2,p7,p6,p7])
print(p4)
p0=Point.centroid([p8,p2,p6,p8,p7,p2,p2,p7,p3,p7])
print(p0)
p5=Point.centroid([p2,p5,p5,p6,p0,p1,p8,p0,p0,p9])
print(p5)
p5=p0.centroid([p7,p2,p9,p7,p2,p0,p5,p7,p6,p5])
print(p5)
p4=Point.centroid([p7,p4,p4,p5,p9,p2,p9,p6,p7,p6])
print(p4)
p7=Point.centroid([p6,p9,p1,p5,p4,p5,p7,p4,p9,p8])
print(p7)
p10=Point([463,914,239,338,761,855,865,727])
p11=Point.centroid([p10,p1,p2,p1,p5,p1,p9,p2,p9,p6])
print(33.6*p10)
p11=Point.centroid([p10,p8,p1,p8,p3,p5,p7,p3,p8,p5])
p11=Point.centroid([p10,p4,p9,p4,p6,p2,p1,p9,p2,p4])
p11=Point.centroid([p10,p6,p0,p2,p9,p5,p4,p1,p5,p7])
p10.distanceTo(p9)
print(p10)
p10.moveTo([579,17,577,491,144])
print(p10)
p10.distanceTo(p5)
print(p10)
p10.moveTo([99,906,340,353,837])
print(p10)
p11=Point.centroid([p10,p3,p6,p8,p2,p9,p7,p6,p5,p3])

