import codecs
import csv

from io import BytesIO
from urllib.request import urlopen


class GetFile:
    def __init__(self, url):
        self.url = url

    def as_io(self):
        with urlopen(self.url) as content:
            return BytesIO(content.read())

    def as_csv(self):
        return csv.reader(codecs.iterdecode(self.as_io(), "utf-8"))


class GetArchivedFile:
    def __init__(self, shortcut):
        self.shortcut = shortcut
        self.url_template = f"https://stooq.com/q/d/l/?s={self.shortcut}&i=d"
        self.content = GetFile(url=self.url_template)

    def get_content(self):
        return self.content.as_csv()
