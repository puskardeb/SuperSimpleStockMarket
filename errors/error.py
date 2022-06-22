class BaseErrorClass(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class StockTypeError(BaseErrorClass):
    pass


class InvalidValueError(BaseErrorClass):
    pass


class StockNotFoundError(BaseErrorClass):
    pass