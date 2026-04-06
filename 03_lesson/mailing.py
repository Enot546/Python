from address import Address


class Mailing:
    to_address = Address
    from_address = Address
    cost = 3000
    rack = '81726354'

    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return (f'Отправление, {self.track}, из, '
                f'{self.from_address}, в, {self.to_address}, . Стоимость, '
                f'{self.cost}, рублей.')


to_address = Address(101000, "Москва", "Невская", 28, 10)
from_address = Address(354000, "Сочи", "Ленина", 45, 13)


print(to_address)
