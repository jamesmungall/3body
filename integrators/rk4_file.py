import calculator_file


class RK4:

    def __init__(self):
        self.dt = None
        self.calculator: calculator_file.Calculator = calculator_file.Calculator()
        self.verbose = True

    def set_calculator(self, input_calculator: calculator_file.Calculator):
        self.calculator = input_calculator

    def set_dt(self, dt):
        self.dt = dt

    def set_verbose(self, verbose):
        self.verbose = verbose

    def next_iteration(self):

        dt = self.dt
# k1
        deltas = self.calculator.get_deltas()

        k1 = list(deltas.values())
        params_0 = self.calculator.get_params()
        params_1 = []
        for i in range(len(params_0)):
            params_1.append(params_0[i] + k1[i] * dt / 2)

        if self.verbose:
            print('k1 ', k1, ', y1', params_1)

# k2
        self.calculator.set_params(params_1)
        deltas = self.calculator.get_deltas()

        k2 = list(deltas.values())

        params_2 = []
        for i in range(len(params_0)):
            params_2.append(params_0[i] + k2[i] * dt / 2)

        if self.verbose:
            print('k2 ', k2, ', y2', params_2)

# k3
        self.calculator.set_params(params_2)
        deltas = self.calculator.get_deltas()

        k3 = list(deltas.values())

        params_3 = []
        for i in range(len(params_0)):
            params_3.append(params_0[i] + k3[i] * dt)

        if self.verbose:
            print('k3 ', k3, ', y3', params_3)

# k4
        self.calculator.set_params(params_3)
        deltas = self.calculator.get_deltas()

        k4 = list(deltas.values())

        if self.verbose:
            print('k4 ', k4)
# m
        m = []
        for i in range(len(params_0)):
            m.append(1 / 6. * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]))
# final
        final_params = []
        for i in range(len(params_0)):
            final_params.append(params_0[i] + m[i] * dt)

        if self.verbose:
            print('m ', m, ' final params ', final_params)

        return final_params

    def next_dictionary(self) -> dict[str, float]:
        result_as_list = self.next_iteration()
        names = self.calculator.get_names()
        result_as_dictionary = {}
        for i in range(len(names)):
            result_as_dictionary.update({names[i]: result_as_list[i]})

        return result_as_dictionary
