# By Kami Bigdely
# Remove assignment to method parameter.

class Distance:
    def __init__(self, distance, unit):
        self.distance = distance
        self.unit = unit

    def get_unit(self):
        return self.unit

    def get_distance(self):
        return self.distance

    def convert_unit(self):
        if self.unit == 'km':
            return self.distance

        elif self.unit == 'ly':
            self.distance = self.distance * 9.461e12
            self.unit = 'km'
            return self.distance

        else:
            print("Unknown Units!")
            return

    def calc_speed(self, time):
        return self.distance/time


class Mass:
    def __init__(self, mass, unit):
        self.mass = mass
        self.unit = unit

    def convert_unit(self):
        if self.unit == 'kg':
            return self.mass

        elif self.unit == 'solar-mass':
            self.mass = self.mass * 1.98892e30
            self.unit = 'kg'
            return self.mass

        else:
            print("Unknown Units!")
            return


def calculate_kinetic_energy(mass, distance, time):
    mass.convert_unit()
    distance.convert_unit()
    speed = distance.calc_speed(time)

    kinetic_energy = 0.5 * mass.mass * (speed ** 2)
    return kinetic_energy


mass = Mass(2, "solar-mass")
distance = Distance(2, 'ly')
print(calculate_kinetic_energy(mass, distance, 3600e20))
