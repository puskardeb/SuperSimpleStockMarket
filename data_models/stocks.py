class Stock:
    '''
    Stock class represents each stock with attributes:-
    1. symbol -> string
    2. type -> string
    3. last_dividend -> float (percentage)
    4. fixed_dividend -> float (percentage)
    5. par_value -> float (percentage)
    '''

    COMMON = 'COMMON'
    PREFERRED = 'PREFERRED'

    def __init__(self, symbol=None, type=None, last_dividend=0, fixed_dividend=0.0, par_value=0):
        self.symbol = symbol
        self.type = type
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend / 100.0
        self.par_value = par_value

    def __str__(self):
        return "symbol={}, type={}, last_dividend={}, fixed_dividend={}, par_value={}".format(
            self.symbol, self.type, self.last_dividend,
            self.fixed_dividend, self.par_value
        )

    def set_symbol(self, symbol: str):
        self.symbol = symbol

    def get_symbol(self):
        return self.symbol

    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type

    def set_last_dividend(self, last_dividend):
        self.last_dividend = last_dividend

    def get_last_dividend(self):
        return self.last_dividend

    def set_fixed_dividend(self, fixed_dividend):
        self.fixed_dividend = fixed_dividend

    def get_fixed_dividend(self):
        return self.fixed_dividend

    def set_par_value(self, par_value):
        self.par_value = par_value

    def get_par_value(self):
        return self.par_value
