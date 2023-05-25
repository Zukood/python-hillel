class Human:
    default_name = "John"
    default_age = 30

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.money = 0
        self.house = None

    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Money: {self.money}")
        print(f"House: {self.house}")

    @staticmethod
    def default_info():
        print(f"Default Name: {Human.default_name}")
        print(f"Default Age: {Human.default_age}")

    def make_deal(self, house, price):
        self.money -= price
        self.house = house

    def earn_money(self):
        self.money += 1000

    def buy_house(self, house, discount=0):
        final_price = house.final_price(discount)
        if self.money >= final_price:
            self.make_deal(house, final_price)
            print("Purchase successful!")
        else:
            print("Insufficient funds for the purchase!")

class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price - discount

class SmallHouse(House):
    def __init__(self):
        super().__init__(40, 50000)

Human.default_info()  # Викличте довідковий метод default_info() для класу Human

human = Human()  # Створіть об'єкт класу Human
human.info()  # Виведіть довідкову інформацію про створений об'єкт (викличте метод info()).

small_house = SmallHouse()  # Створіть об'єкт класу SmallHouse

human.buy_house(small_house)  # Спробуйте купити створений будинок, переконайтеся в отриманні попередження.

human.earn_money()  # Виправте фінансове становище об'єкта - викличте метод earn_money()

human.buy_house(small_house)  # Знову спробуйте купити будинок

human.info()  # Подивіться, як змінилося стан об'єкта класу Human
