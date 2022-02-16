def output_all(source):
    for i in source:
        print(f'{i} {source[i]["name"]} {source[i]["surname"]} {source[i]["class"]}', end='')
        print()