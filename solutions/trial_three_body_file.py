from integrators import rk4_file
from utilities.body_file import Body
from calculators.ThreeBodyCalculator_file import ThreeBodyCalculator
from utilities.vector3_file import Vector3

import pandas as pd


class TrialThreeBody:

    def __init__(self):
        self.m3 = 1.0
        self.m2 = 1.0
        self.m1 = 1.0
        self.calculator = ThreeBodyCalculator()
        self.calculator.set_G(1)

        self.X1 = 0.716248295713
        self.Y1 = 0.384288553041
        self.X2 = 0.086172594591
        self.Y2 = 1.342795868577
        self.X3 = 0.538777980808
        self.Y3 = 0.481049882656

        self.VX1 = 1.245268230896
        self.VY1 = 2.444311951777
        self.VX2 = -0.675224323690
        self.VY2 = -0.962879613630
        self.VX3 = -0.570043907206
        self.VY3 = -1.481432338147

        self.n_iterations = 100
        self.dt = 0.1

    def set_G(self, g):
        self.calculator.set_G(g)

    def _initialize(self):
        first_body = Body()
        first_body.set_name('b1')
        position = Vector3([self.X1, self.Y1, 0.0])
        velocity = Vector3([self.VX1, self.VY1, 0.0])
        first_body.set_position(position)
        first_body.set_velocity(velocity)
        first_body.set_mass(self.m1)

        second_body = Body()
        second_body.set_name('b2')
        position = Vector3([self.X2, self.Y2, 0.0])
        velocity = Vector3([self.VX2, self.VY2, 0.0])
        second_body.set_position(position)
        second_body.set_velocity(velocity)
        second_body.set_mass(self.m2)

        third_body = Body()
        third_body.set_name('b3')
        position = Vector3([self.X3, self.Y3, 0.0])
        velocity = Vector3([self.VX3, self.VY3, 0.0])
        third_body.set_position(position)
        third_body.set_velocity(velocity)
        third_body.set_mass(self.m3)

        self.calculator.set_body1(first_body)
        self.calculator.set_body2(second_body)
        self.calculator.set_body3(third_body)
        self.calculator.set_init_params()

    def _integrate(self):
        integrator = rk4_file.RK4()
        integrator.set_dt(self.dt)
        integrator.set_calculator(self.calculator)
        integrator.set_verbose(False)

        results = [self.calculator.get_init_params()]

        n_iterations = self.n_iterations
        for i in range(n_iterations):
            results.append(integrator.next_iteration())

        results_df = pd.DataFrame(results, columns=self.calculator.get_names())
        results_df['time'] = range(n_iterations + 1)

        self.final_df = results_df

    def get_df(self):
        self._initialize()
        self._integrate()
        return self.final_df

    def set_m1(self, m):
        self.m1 = m

    def set_m2(self, m):
        self.m2 = m

    def set_m3(self, m):
        self.m3 = m
