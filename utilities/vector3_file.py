import math


class Vector3:
    def __init__(self, params=None):
        if params is None:
            params = [0.0, 0.0, 0.0]
        self.params = params

        self.x = params[0]
        self.y = params[1]
        self.z = params[2]

    def get_params(self) -> [float]:
        return self.params

    def set_params(self, params):
        self.params = params

    def set_x(self, x):
        self.params[0] = self.x

    def set_y(self, y):
        self.params[1] = self.y

    def set_z(self, z):
        self.params[2] = self.z

    def get_x(self) -> float:
        return self.params[0]

    def get_y(self) -> float:
        return self.params[1]

    def get_z(self) -> float:
        return self.params[2]

    @staticmethod
    def DistanceDouble(a, b) -> float:
        dx = a.x - b.x
        dy = a.y - b.y
        dz = a.z - b.z
        return math.sqrt(dx**2 + dy**2 + dz**2)

    @staticmethod
    def DistanceDoubleSquared(a, b) -> float:
        dx = a.x - b.x
        dy = a.y - b.y
        dz = a.z - b.z
        return dx**2 + dy**2 + dz**2

