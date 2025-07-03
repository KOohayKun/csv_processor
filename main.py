from utils import read_csv_file, print_table
import argparse


if __name__ == '__main__':
    data = read_csv_file("sample.csv")
    print_table(data)

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
