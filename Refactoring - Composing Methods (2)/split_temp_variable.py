# by Kami Bigdely
# Split temporary variable

class Burger:
    PATTY = 70
    PICKLE = 20
    TOMATO = 25
    LETTUCE = 15
    BUN = 95

    def __init__(self, name):
        self.name = name

    def calc_sandwich_weight(self):
        return((2*self.PATTY) + (4*self.PICKLE) + (3*self.TOMATO) + (2*self.LETTUCE) + (2*self.BUN))

    def print_weight(self):
        print(f'{self.name}: {self.calc_sandwich_weight()} g')


class SeoulKimchiBurger(Burger):
    KIMCHI = 30
    MAYO = 5
    GOLDEN_FRIED_ONION = 20

    def __init__(self, name):
        super().__init__(name)

    def calc_sandwich_weight(self):
        return(super().calc_sandwich_weight() + self.KIMCHI + self.MAYO + self.GOLDEN_FRIED_ONION)


ny_burger = Burger('NY Burger')
seoul_kimchi_burger = SeoulKimchiBurger('Seoul Kimchi Burger')

ny_burger.print_weight()
seoul_kimchi_burger.print_weight()
