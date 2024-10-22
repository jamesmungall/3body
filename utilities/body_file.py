from utilities.vector3_file import Vector3


class Body:
    def __init__(self):
        self.mass = None
        self.velocity = None
        self.position = None
        self.name = None

    def set_name(self, name):
        self.name = name

    def set_position(self, position: Vector3):
        self.position = position

    def get_position(self) -> Vector3:
        return self.position

    def set_velocity(self, velocity: Vector3):
        self.velocity = velocity

    def get_velocity(self) -> Vector3:
        return self.velocity

    def set_mass(self, mass):
        self.mass = mass
