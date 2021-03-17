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

    def avg(self, args, ut=None, lt = None):
        if not ut:
            ut = max(args)

        if not lt:
            lt = min(args)

        _arg = [x for x in args if x <= ut and x >= lt]
        return sum(_arg)/len(_arg)
