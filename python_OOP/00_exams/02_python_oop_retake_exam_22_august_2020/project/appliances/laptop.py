from project.appliances.appliance import Appliance


class Laptop(Appliance):
    cost = 1.0

    def __init__(self):
        super().__init__(self.cost)