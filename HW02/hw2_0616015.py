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
        # try:
            if self.dim != len(move):
                raise ValueError
            self.coords = list(map(add, self.coords, move))
        # except ValueError:
        #     self.errMsg('dim')

    #move the point to x,y
    def moveTo(self, move=[0, 0]):
        # try:
            if self.dim != len(move):
                raise ValueError
            self.coords = move
        # except ValueError:
        #     self.errMsg('dim')

    #calculate Hamming distance between two points
    def distanceTo(self, p2):
        # try:
            if self.dim != len(p2.coords):
                raise ValueError
            def getDistance(a, b):
                return abs(a - b)
            return reduce(add, list(map(getDistance, self.coords, p2.coords)))
        # except ValueError:
        #     self.errMsg('dim')

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
        # try:
            if self.dim != len(p2.coords):
                raise ValueError
            return Point(list(map(add, self.coords, p2.coords)))
        # except ValueError:
        #     self.errMsg('dim')
        # return

    def __sub__(self, p2):
        # try:
            if self.dim != len(p2.coords):
                raise ValueError
            return Point(list(map(sub, self.coords, p2.coords)))
        # except ValueError:
        #     self.errMsg('dim')
        # return

    def __gt__(self, p2):
        # try:
            if self.dim != len(p2.coords):
                raise ValueError
            return reduce(and_, list(map(gt, self.coords, p2.coords)))
        # except ValueError:
        #     self.errMsg('dim')
        # return

    def __mul__(self, scalar):
        return Point(list(map(lambda x: x * scalar, self.coords)))

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __eq__(self, p2):
        # try:
            if self.dim != len(p2.coords):
                raise ValueError
            return reduce(and_, list(map(eq, self.coords, p2.coords)))
        # except ValueError:
        #     self.errMsg('dim')
        # return

    @classmethod
    def centroid(cls, pList=[]):
        # try:
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
        # except RuntimeError:
        #     cls.errMsg('plist')
        # except ValueError:
        #     cls.errMsg('dim')

