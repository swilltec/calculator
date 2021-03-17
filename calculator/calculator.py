"""Main module."""

from functools import reduce


class Calc:

    def add(self, *args):
        return sum(args)

    def subtract(self, a, b):
        return a - b

    def multiply(self, *args):
        if not all(args):
            raise ValueError
        return reduce(lambda x, y: x*y, args)

    def divide(self, a, b):
        try:
            return a / b
        except:
            return "inf"

    def avg(self, args, ut=None):
        if not ut:
            ut = max(args)

        _arg = [x for x in args if x <= ut]
        return sum(_arg)/len(_arg)
