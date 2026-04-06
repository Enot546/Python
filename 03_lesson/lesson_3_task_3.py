from address import Address
from mailing import Mailing

to_address = Address(101000, "Москва", "Невская", 28, 10)
from_address = Address(354000, "Сочи", "Ленина", 45, 13)
mailing = Mailing(to_address, from_address, 3000, '81726354')

print(mailing)
