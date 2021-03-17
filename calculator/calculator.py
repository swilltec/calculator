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

    def avg(self, args, ut=None, lt=None):

        _args = args[:]

        if ut:
            _args = [x for x in _args if x <= ut]

        if lt:
           _args = [x for x in _args if x >= lt]

        if not len(_args):
            return 0
            
        return sum(_args)/len(_args)
