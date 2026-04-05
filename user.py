class User:
    age = 0

    def __init__(self, name):
        print("Я создался")
        self.username = name

    def sayName(self):
        print("меня зовут", self.username)

    def sayAge(self):
        print(self.age)

    def setAge(self, newAge):
        self.age = newAge
