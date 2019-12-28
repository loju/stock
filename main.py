#!/usr/bin/env python3

from utils.converters import ConvertData
from utils.network import GetArchivedAllFiles


def main():
    all_data = GetArchivedAllFiles()
    output_dict = {}
    for _data in all_data:
        symbol = _data.get_shortcut()
        data = _data.get_csv_content()
        data_dict = ConvertData(symbol=symbol, data=data)
        output_dict.update(data_dict.convert())
    print(output_dict.keys())
    for k, v in output_dict.items():
        print(k, len(v))


if __name__ == "__main__":
    main()
