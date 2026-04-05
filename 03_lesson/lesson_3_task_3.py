from address import Address
from mailing import Mailing

to_address = Address
from_address = Address
to_address = 101000, "Москва", "Невская", 28, 10
from_address = 354000, "Сочи", "Ленина", 45, 13

sending = Mailing
sending(to_address, from_address, 3000, 81726354)

print(
    "Отправление",
    sending.track,
    "из",
    from_address,
    "в",
    to_address,
    ". Стоимость",
    sending.cost,
    "рублей.",
)
