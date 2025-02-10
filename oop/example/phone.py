from item import Item


class Phone(Item):

    def __init__(self, name, price, quantity, broken_phone):
        super().__init__(name, price, quantity)

        print(quantity)

        self.broken_phone = broken_phone
        self.quantity = quantity - broken_phone

        assert (
            broken_phone >= 0
        ), f"Broken Phone {broken_phone} must be greater or equal to 0"
