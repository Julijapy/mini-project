def filter_by_state(data: list[{}], state="EXECUTED") -> list[{}]:
    new_list = []
    for i in data:
        for key, value in i.items():
            if value == state:
                new_list.append(i)

    return new_list


def sort_by_date(date: list[{}], reverse=True) -> list[{}]:
    new_date = sorted(date, key=lambda x: x["date"], reverse=reverse)
    return new_date
