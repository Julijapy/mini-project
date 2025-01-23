def filter_by_state(data: list[{}], state="EXECUTED") -> list[{}]:
    new_list = []
    for i in data:
        for key, value in i.items():
            if value == state:
                new_list.append(i)

    return new_list
