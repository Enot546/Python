from smartphone import Smartphone

catalog = [
    Smartphone("Huawei", "Enjoy 90", "+79854655847"),
    Smartphone("Red Magic", "10 Air", "+79456364546"),
    Smartphone("Acer", "Liquid Z6", "+794585648153"),
    Smartphone("Nokia", "3310", "+79457637635"),
    Smartphone("POCO", "F8 Ultra", "+79148218402")
]

for phone in catalog:
    print(f"{phone.marka} - {phone.model}. {phone.number}")
