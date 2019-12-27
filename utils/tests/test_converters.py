class TestFromCsvToDict:
    def test_from_csv_to_dict(self):
        generator_one_symbol_data = (["dummy", "list", n ** 2] for n in range(5))
        symbol = "CDR"
        record = ConvertData(symbol=symbol, data=generator_one_symbol_data)
        assert record == {
            "CDR": [
                ["dummy", "list", 0],
                ["dummy", "list", 1],
                ["dummy", "list", 2],
                ["dummy", "list", 3],
                ["dummy", "list", 4],
            ]
        }
