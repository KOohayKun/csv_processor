from utils import read_csv_file, print_table
import argparse
from proccesor import filter_data, aggregate


def read_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--where")
    parser.add_argument("--aggregate")
    return parser.parse_args()

def split_where_arg(where_str):
    for operator in [">=","<=","<",">","="]:
        if operator in where_str:
            column, op_value = where_str.split(operator)
            return column.strip(), operator, op_value.strip()

    raise ValueError("Неверный формат для --where. Используй =, <, >, <=, >=")

def split_aggregate_arg(aggregate_str):
    if "=" not in aggregate_str:
        raise ValueError("Неверный формат для --aggregate. Используй = ")

    column, op = aggregate_str.split("=")
    return column.strip(), op.strip()

if __name__ == '__main__':
    args = read_args()
    data = read_csv_file("sample.csv")

    if args.where:
        header, op, value = split_where_arg(args.where)
        data = filter_data(data,header,op,value)

    print_table(data)

    if args.aggregate:
        column, agg_op = split_aggregate_arg(args.aggregate)
        result = aggregate(data, column, agg_op)
        print(f"{agg_op} по колонке {column}: {result}")
    else:
        print_table(data)