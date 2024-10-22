from utilities.body_file import Body
from calculator_file import Calculator
from utilities.vector3_file import Vector3


class TwoBodyCalculator(Calculator):
    def __init__(self):
        self.init_params = None
        self.params = None
        self.body2 = None
        self.body1 = None
        self.g = None

    def set_G(self, g):
        self.g = g

    def get_params(self) -> [float]:
        return self.params

    def set_params(self, new_params: [float]):
        self.params = new_params
        position1 = Vector3([new_params[0], new_params[1], new_params[2]])
        velocity1 = Vector3([new_params[3], new_params[4], new_params[5]])
        position2 = Vector3([new_params[6], new_params[7], new_params[8]])
        velocity2 = Vector3([new_params[9], new_params[10], new_params[11]])

        self.body1.set_position(position1)
        self.body1.set_velocity(velocity1)

        self.body2.set_position(position2)
        self.body2.set_velocity(velocity2)

    def get_names(self) -> [str]:
        return (['x1', 'y1', 'z1',
                 'vx1', 'vy1', 'vz1',
                 'x2', 'y2', 'z2',
                 'vx2', 'vy2', 'vz2'])

    def get_init_params(self) -> [float]:
        return self.init_params

    def set_body1(self, body: Body):
        self.body1 = body

    def set_body2(self, body: Body):
        self.body2 = body

    def set_init_params(self):
        self.params = []

        self.params.append(self.body1.position.x)
        self.params.append(self.body1.position.y)
        self.params.append(self.body1.position.z)

        self.params.append(self.body1.velocity.x)
        self.params.append(self.body1.velocity.y)
        self.params.append(self.body1.velocity.z)

        self.params.append(self.body2.position.x)
        self.params.append(self.body2.position.y)
        self.params.append(self.body2.position.z)

        self.params.append(self.body2.velocity.x)
        self.params.append(self.body2.velocity.y)
        self.params.append(self.body2.velocity.z)

        self.init_params = self.params

    def get_deltas(self) -> dict:
        r = Vector3.DistanceDouble(self.body1.get_position(), self.body2.get_position())
    #    r_2 = Vector3.DistanceDoubleSquared(self.body1.position, self.body2.position)
        keys = self.get_names()
        values = self.get_params()
        p = dict(zip(keys, values))
#        deltas = ([p['vx1'], p['vy1'], p['vz1'],
#                   self.g * self.body2.mass * (p['x2'] - p['x1']) / r ** 2,
#                   self.g * self.body2.mass * (p['y2'] - p['y1']) / r ** 2,
#                   self.g * self.body2.mass * (p['z2'] - p['z1']) / r ** 2,
#                   p['vx2'], p['vy2'], p['vz2'],
#                   self.g * self.body1.mass * (p['x1'] - p['x2']) / r ** 2,
#                   self.g * self.body1.mass * (p['y1'] - p['y2']) / r ** 2,
#                   self.g * self.body1.mass * (p['z1'] - p['z2']) / r ** 2])
        deltas = ([
            self.body1.velocity.x, self.body1.velocity.y, self.body1.velocity.z,
            self.g * self.body2.mass * (self.body2.position.x - self.body1.position.x) / r**3,
            self.g * self.body2.mass * (self.body2.position.y - self.body1.position.y) / r**3,
            self.g * self.body2.mass * (self.body2.position.z - self.body1.position.z) / r**3,

            self.body2.velocity.x, self.body2.velocity.y, self.body2.velocity.z,
            self.g * self.body1.mass * (self.body1.position.x - self.body2.position.x) / r**3,
            self.g * self.body1.mass * (self.body1.position.y - self.body2.position.y) / r**3,
            self.g * self.body1.mass * (self.body1.position.z - self.body2.position.z) / r**3
        ])
        return dict(zip(keys, deltas))
