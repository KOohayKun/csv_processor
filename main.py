from utils import read_csv_file, print_table
import argparse
from proccesor import filter_data


def read_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--where")

    return parser.parse_args()

def split_where_arg(where_str):
    for op in [">=","<=","<",">","="]:
        if op in where_str:
            header, value = where_str.split(op)
            return header.strip(), op, value.strip()

    raise ValueError("Неверный формат для --where. Используй =, <, >, <=, >=")

if __name__ == '__main__':
    args = read_args()
    data = read_csv_file("sample.csv")

    if args.where:
        header, op, value = split_where_arg(args.where)
        data = filter_data(data,header,op,value)

    print_table(data)