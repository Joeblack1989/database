data = {
    0:{'name':'Ilya','surname':'Aleksandrov','birthday':'01.11.2001'},
    1:{'name':'Sasha','surname':'Pavlov','birthday':'02.05.2001'},
    2:{'name':'Kolya','surname':'Petrov','birthday':'16.06.2001'},
    3:{'name':'Marina','surname':'Lanova','birthday':'24.10.2001'}
}

def day_birthday(source, index = -1):
    if index == -1:
        for i in data:
            print(f'{data[i]["surname"]} - {data[i]["birthday"]}', end=' ')
            print()
    else: print(f'{data[index]["surname"]} - {data[index]["birthday"]}', end=' ')

day_birthday(data,0)
print()
def append_info(source):
    new_name = input('Введите Имя ')
    new_surname = input('Введите Фамилию ')
    new_birthday = input('Введите Дату рождения ')
    source[len(source)] = {'name':new_name, 'surname': new_surname, 'birthday' : new_birthday}
    return source[len(source) - 1]

#print(append_info(data))






