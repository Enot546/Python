class Address:
    index = "000000"
    city = "name"
    street = "name"
    home_number = "00"
    apart_number = "00"

    def __init__(self, index, city, street, home, flat):
        self.index = index
        self.city = city
        self.street = street
        self.home = home
        self.flat = flat

    def __str__(self):
        return (f"{self.index}, {self.street}, дом "
                f"{self.home} - квартира {self.flat}")

    def to_address(self):
        print(self.to_address)


to_address = (101000, "Москва", "Невская", 28, 10)
from_address = (354000, "Сочи", "Ленина", 45, 13)
