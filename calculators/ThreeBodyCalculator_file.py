from utilities.body_file import Body
from calculator_file import Calculator
from utilities.vector3_file import Vector3


class ThreeBodyCalculator(Calculator):
    def __init__(self):
        self.g = None
        self.init_params = None
        self.params = None
        self.body1 = None
        self.body2 = None
        self.body3 = None

    def set_G(self, g):
        self.g = g

    def set_body1(self, body: Body):
        self.body1 = body

    def set_body2(self, body: Body):
        self.body2 = body

    def set_body3(self, body: Body):
        self.body3 = body

    def get_names(self) -> [str]:
        names = []
        for i in range(3):
            for letter in ['x', 'y', 'z', 'vx', 'vy', 'vz']:
                names.append(letter + str(i + 1))  # e.g. x1, y1 ... vz3
        return names

    def set_init_params(self):
        self.params = []
        for body in [self.body1, self.body2, self.body3]:
            self.params.append(body.position.x)
            self.params.append(body.position.y)
            self.params.append(body.position.z)

            self.params.append(body.velocity.x)
            self.params.append(body.velocity.y)
            self.params.append(body.velocity.z)

        self.init_params = self.params

    def get_init_params(self) -> [float]:
        return self.init_params

    def get_params(self) -> [float]:
        return self.params

    def set_params(self, new_params: [float]):
        self.params = new_params
        i = 0
        for body in [self.body1, self.body2, self.body3]:
            body.set_position(Vector3([new_params[i], new_params[i + 1], new_params[i + 2]]))
            body.set_velocity(Vector3([new_params[i + 3], new_params[i + 4], new_params[i + 5]]))
            i = i + 6

    def get_deltas(self) -> dict:
        r12 = Vector3.DistanceDouble(self.body1.get_position(), self.body2.get_position())
        r13 = Vector3.DistanceDouble(self.body1.get_position(), self.body3.get_position())
        r23 = Vector3.DistanceDouble(self.body2.get_position(), self.body3.get_position())

        keys = self.get_names()

        deltas = ([
            self.body1.velocity.x, self.body1.velocity.y, self.body1.velocity.z,
            self.g * self.body2.mass * (self.body2.position.x - self.body1.position.x) / r12 ** 3 +
            self.g * self.body3.mass * (self.body3.position.x - self.body1.position.x) / r13 ** 3,
            self.g * self.body2.mass * (self.body2.position.y - self.body1.position.y) / r12 ** 3 +
            self.g * self.body3.mass * (self.body3.position.y - self.body1.position.y) / r13 ** 3,
            self.g * self.body2.mass * (self.body2.position.z - self.body1.position.z) / r12 ** 3 +
            self.g * self.body3.mass * (self.body3.position.z - self.body1.position.z) / r13 ** 3,

            self.body2.velocity.x, self.body2.velocity.y, self.body2.velocity.z,
            self.g * self.body1.mass * (self.body1.position.x - self.body2.position.x) / r12 ** 3 +
            self.g * self.body3.mass * (self.body3.position.x - self.body2.position.x) / r23 ** 3,
            self.g * self.body1.mass * (self.body1.position.y - self.body2.position.y) / r12 ** 3 +
            self.g * self.body3.mass * (self.body3.position.y - self.body2.position.y) / r23 ** 3,
            self.g * self.body1.mass * (self.body1.position.z - self.body2.position.z) / r12 ** 3 +
            self.g * self.body3.mass * (self.body3.position.z - self.body2.position.z) / r23 ** 3,

            self.body3.velocity.x, self.body3.velocity.y, self.body3.velocity.z,
            self.g * self.body1.mass * (self.body1.position.x - self.body3.position.x) / r13 ** 3 +
            self.g * self.body2.mass * (self.body2.position.x - self.body3.position.x) / r23 ** 3,
            self.g * self.body1.mass * (self.body1.position.y - self.body3.position.y) / r13 ** 3 +
            self.g * self.body2.mass * (self.body2.position.y - self.body3.position.y) / r23 ** 3,
            self.g * self.body1.mass * (self.body1.position.z - self.body3.position.z) / r13 ** 3 +
            self.g * self.body2.mass * (self.body2.position.z - self.body3.position.z) / r23 ** 3
        ])
        return dict(zip(keys, deltas))
