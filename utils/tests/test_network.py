from io import BytesIO
from unittest.mock import patch

from ..network import GetIOFile, GetCsvFile, GetArchivedFile, GetArchivedAllFiles


class TestGetFile:
    @patch.object(GetIOFile, "get_content")
    def test_get_content(self, get_content):
        _io_content = GetIOFile(url="https://fake.url")
        _io_content.get_content()
        assert get_content.called


class TestGetCsvFile:
    def test_get_content(self):
        _csv_content = GetCsvFile(content=BytesIO(b"first,second,third"))
        content = _csv_content.get_content()
        assert content.__next__() == ["first", "second", "third"]


class TestGetArchivedFile:
    def test_url_template(self):
        arch_file = GetArchivedFile(shortcut="CDR")
        assert arch_file._get_url() == "https://stooq.com/q/d/l/?s=cdr&i=d"

    @patch.object(GetIOFile, "get_content")
    def test_get_io_content(self, get_content):
        arch_file = GetArchivedFile(shortcut="CDR")
        arch_file.get_io_content()
        assert get_content.called is True

    @patch.object(GetCsvFile, "get_content")
    def test_get_csv_content(self, get_content):
        arch_file = GetArchivedFile(shortcut="CDR")
        arch_file.get_csv_content()
        assert get_content.called is True


class TestGetArchivedAllFiles:
    def test__iter__(self):
        get_all = GetArchivedAllFiles()
        assert hasattr(get_all, "__init__") is True
