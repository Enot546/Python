class Address:
    index = "000000"
    city = "name"
    street = "name"
    home_number = "00"
    apart_number = "00"
    to_address = (101000, "Москва", "Невская", 28, 10)
    from_address = (354000, "Сочи", "Ленина", 45, 13)

    def __init__(self, index, city, street, home, flat, to_address,
                 from_address):
        self.index = index
        self.city = city
        self.street = street
        self.home = home
        self.flat = flat
        to_address = to_address
        from_address = from_address

    def __str__(self):
        return (f"{self.index}, {self.street}, "
                f"{self.home},  {self.flat}")
