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