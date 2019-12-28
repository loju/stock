#!/usr/bin/env python3
from datetime import datetime

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
    return output_dict


if __name__ == "__main__":
    start = datetime.now()
    main()
    print(f"Execution time: {datetime.now() - start}")
