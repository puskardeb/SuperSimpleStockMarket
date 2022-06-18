import datetime


class Trade:
    def __init__(self, type=None, quantity=0, price=0, timestamp=datetime.datetime.now()):
        self.type = type
        self.quantity = quantity
        self.price = price
        self.timestamp = timestamp

    def __str__(self):
        return "type={}, quantity={}, price={}, timestamp={}".format(
            self.type, self.quantity, self.price, self.timestamp)

    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type

    def set_quantity(self, quantity):
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp

    def get_timestamp(self):
        return self.timestamp