def filter_data(data, header, operator, value):
    res = []
    for row in data:
        cell = row.get(header)
        if cell is None:
            continue
        try:
            cell = float(cell)
            value = float(value)
        except ValueError:
            pass

        if operator == "=" and str(cell) == str(value):
            res.append(row)
        elif operator == ">" and cell > value:
            res.append(row)
        elif operator == "<" and cell < value:
            res.append(row)
        elif operator == ">=" and cell >= value:
            res.append(row)
        elif operator == "<=" and cell <= value:
            res.append(row)

    return res

def aggregate(data, column, op):
    values = []
    for row in data:
        if column not in row:
            raise ValueError(f"Колонка '{column}' не найдена в данных")
        try:
            number = float(row[column])
            values.append(number)
        except ValueError:
            raise ValueError("Нет данных для агрегации")

    if op == "avg":
        return sum(values) / len(values)
    elif op == "min":
        return min(values)
    elif op == "max":
        return max(values)
    else:
        raise ValueError(f"Операция '{op}' не поддерживается")
