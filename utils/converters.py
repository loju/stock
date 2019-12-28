import typing


class ConvertData:
    def __init__(
        self,
        symbol: typing.AnyStr,
        data: typing.Generator,
    ):
        self.symbol = symbol
        self.data = data
        self.output_dict = {}

    def convert(self):
        _dct = {self.symbol: [record for record in self.data]}
        return _dct

