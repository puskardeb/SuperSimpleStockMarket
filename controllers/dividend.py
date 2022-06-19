from services.dividend_service import DividendService


class DividendController:

    @staticmethod
    def calculate(stock, price):
        try:
            if price < 0:
                print("Price cannot be a negative value.")
                return -1
            return DividendService.calculate(stock, price)
        except KeyError:
            print("Stock '{}' not present in stock list".format(stock))
            return -1
        except ZeroDivisionError:
            print("Price is 0. Enter a positive value for price")
            return -1
