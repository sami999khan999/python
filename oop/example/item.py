class Item:
    discount = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity: 0):
        assert price >= 0, "Price must be greater then or equal to 0!"
        assert quantity >= 0, "Quantity must be greater then or equal to 0!"

        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_discount(self):
        return self.price * self.discount

    def calculate_price(self):
        return self.quantity * self.price

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', '{self.quantity}, {self.price}')"

    @classmethod
    def create_instences(cls, products):
        for product in products:
            Item(product["name"], product["price"], product["quantity"])
        #     print(cls.all)
        # print(cls.discount)

    @staticmethod
    def is_int(num):
        if isinstance(num, int):
            return True
        elif isinstance(num, float):
            return False
        else:
            return False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
