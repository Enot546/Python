from user import User
from card import Card

djo = User("Djo")

djo.sayAge()
djo.setAge(33)
djo.sayAge()

card = Card("9875 7834 6547 3456", "11/28", "Djo F")
card.pay(1000)
