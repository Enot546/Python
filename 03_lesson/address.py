class Address:
    index = "000000"
    city = "name"
    street = "name"
    home = "00"
    flat = "00"

    def __init__(self, index, city, street, home, flat):
        self.index = index
        self.city = city
        self.street = street
        self.home = home
        self.flat = flat

    def __str__(self):
        return (f"{self.index}, {self.street}, "
                f"{self.home},  {self.flat}")


to_address = Address(101000, "Москва", "Невская", 28, 10)
from_address = Address(354000, "Сочи", "Ленина", 45, 13)
