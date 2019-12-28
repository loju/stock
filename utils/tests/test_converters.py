from ..converters import ConvertData


class TestFromCsvToDict:
    def test_from_csv_to_dict(self):
        generator_one_symbol_data = (["dummy", "list", n ** 2] for n in range(5))
        symbol = "CDR"
        _record = ConvertData(symbol=symbol, data=generator_one_symbol_data)
        record = _record.convert()

        assert record == {
            "CDR": [
                ["dummy", "list", 0],
                ["dummy", "list", 1],
                ["dummy", "list", 4],
                ["dummy", "list", 9],
                ["dummy", "list", 16],
            ]
        }

