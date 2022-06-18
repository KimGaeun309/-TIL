
import math 

class MyVector():
    def __init__(self, dim, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.dim = -1
        self.dist = 0
        
    def normalize(self):
        # norm을 구하고
        mag = self.getMagnitude()
        # 각 성분을 나누어주고
        self.x /= mag
        self.y /= mag
        self.z /= mag

    def getMagnitude(self):
        mag = math.sqrt(math.pow(self.x, 2)
            + math.pow(self.y, 2)
            + math.pow(self.z, 2))
        return mag

    def getState(self):
        return self.x, self.y, self.z

    def scalarMulti(self, scalar):
        vector = VectorBuilder3D().setX(self.x * scalar).setY(self.y * scalar).setZ(self.z * scalar).build()
        return vector

    def minus(self, MyVector):
        vector = VectorBuilder3D().setX(self.x - MyVector.x).setY(self.y - MyVector.y).setZ(self.z - MyVector.z).build()
        return vector


# vec = MyVector(3, 0, 0, 0)
# print(vec.getState())

# 순전히 argument들에 대한 것만.
# 목표는 결국 생성해 주는 것.
class VectorBuilder:

    def __init__(self):
        self.x = None
        self.y = None
        self.z = None
        self.dim = None

    def setDim(self, dim):
        self.dim = dim
        return self

    def setX(self, x):
        self.x = x
        return self

    def setY(self, y):
        self.y = y
        return self

    def setZ(self, z):
        self.z = z
        return self

    def build(self):
        vector = MyVector(self.dim, self.x, self.y, self.z)
        return vector


# vec = VectorBuilder().setDim(3).setX(50).setY(100).setZ(10).build()
# print(vec.getState())

# want to create 2D vector or 3D vector using presets

class VectorBuilder2D(VectorBuilder):
    def __init__(self):
        super().__init__()
        self.setZ(0)
        self.setDim(2)

class VectorBuilder3D(VectorBuilder):
    def __init__(self):
        super().__init__()
        self.setDim(3)

# vec2D = VectorBuilder2D().setX(50).setY(50).build()
# print(vec2D.getState())
# vec2D.normalize() # -> mag = 1
# print(vec2D.getState())
# print(vec2D.getMagnitude())

# vec3D = VectorBuilder3D().setX(50).setY(50).setZ(100).build()
# print(vec3D.getState())
# vec3D.normalize() # -> mag = 1
# print(vec3D.getState())
# print(vec3D.getMagnitude())


class Director:
    def vectorZeros(builder:VectorBuilder): # preset argument
        builder.setX(0)
        builder.setY(0)
        builder.setZ(0)

    def vectorOnes(builder:VectorBuilder):  # preset argument
        builder.setX(1)
        builder.setY(1)
        builder.setZ(1)


# builder3D = VectorBuilder3D()
# Director.vectorOnes(builder3D) # builder를 통과시켜줌
# vec3D.builder3D.build()
# print(vec3D.getState())


# 추가한 함수 scalarMuitl(self, scalar) 와 minus(self, MyVector) 

a = VectorBuilder3D().setX(10).setY(20).setZ(30).build()
b = a.scalarMulti(3)

c = a.minus(b)

print(a.getState())
print(b.getState())
print(c.getState())
