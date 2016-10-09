class Pizza:
    crusts = {'thin': {'small': 10, 'medium': 20, 'large': 30},
              'thick': {'small': 20, 'medium': 30, 'large': 40}}
    toppings = {'onion': 18, 'capsicum': 15, 'tomato': 10, 'greenchilli': 12, 'mushroom': 20, 'sweetcorn': 25,
                'chicken': 50, 'egg': 40, 'extracheese': 50}

    def __init__(self, crust, size, toppings_list):
        self.crust = crust
        self.size = size
        self.toppings_list = toppings_list

    def get_bill(self):
        total_bill = self.crusts[self.crust][self.size]
        for topping in self.toppings_list:
            total_bill += self.toppings[topping]
        return total_bill
