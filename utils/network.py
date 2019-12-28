import codecs
import csv
import typing


from io import BytesIO
from urllib.request import urlopen


class GetIOFile:
    def __init__(self, url: typing.AnyStr):
        self.url = url

    def get_content(self) -> BytesIO:
        with urlopen(self.url) as content:
            print(content, type(content))
            return BytesIO(content.read())


class GetCsvFile:
    def __init__(self, content: BytesIO):
        self.content = content

    def get_content(self) -> typing.Iterator:
        return csv.reader(codecs.iterdecode(self.content, "utf-8"))


class GetArchivedFile:
    def __init__(self, shortcut: typing.AnyStr):
        self.shortcut = shortcut

    def _get_url(self) -> typing.AnyStr:
        return f"https://stooq.com/q/d/l/?s={self.shortcut.lower()}&i=d"

    def get_shortcut(self):
        return self.shortcut

    def get_io_content(self) -> BytesIO:
        _io_file = GetIOFile(url=self._get_url())
        return _io_file.get_content()

    def get_csv_content(self) -> typing.Iterator:
        _csv_file = GetCsvFile(content=self.get_io_content())
        return _csv_file.get_content()


class GetArchivedAllFiles:
    symbols = [
        "ALR",
        "CCC",
        "CDR",
        "CPS",
        "DNP",
        "JSW",
        "KGH",
        "LTS",
        "LPP",
        "MBK",
        "OPL",
        "PEO",
        "PGE",
        "PGN",
        "PKN",
        "PKO",
        "PLY",
        "PZU",
        "SPL",
        "TPE",
    ]

    def __iter__(self) -> typing.Generator:
        return (GetArchivedFile(shortcut=symbol) for symbol in self.symbols)
