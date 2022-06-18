class Stock:
    '''
    Stock class represents each stock with attributes:-
    1. symbol -> string
    2. type -> string
    3. last_dividend -> float (percentage)
    4. fixed_dividend -> float (percentage)
    5. par_value -> float (percentage)
    '''

    def __init__(self, **kwargs):

        if len(kwargs) > 0 and len(kwargs) == 5:
            self.symbol = kwargs['symbol']
            self.type = kwargs['type']
            self.last_dividend = float(kwargs['last_dividend'])
            if kwargs['fixed_dividend'] != ' ':
                self.fixed_dividend = kwargs['fixed_dividend']
            else:
                self.fixed_dividend = 0.0
            self.par_value = float(kwargs['par_value'])
        elif len(kwargs) == 0:
            self.symbol = None
            self.type = None
            self.last_dividend = 0.0
            self.fixed_dividend = 0.0
            self.par_value = 0.0
        else:
            raise IOError("Error")

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
