data = {
    0:{'name':'Ilya','surname':'Aleksandrov','birthday':'01.11.2001'},
    1:{'name':'Sasha','surname':'Pavlov','birthday':'02.05.2001'},
    2:{'name':'Kolya','surname':'Petrov','birthday':'16.06.2001'},
    3:{'name':'Marina','surname':'Lanova','birthday':'24.10.2001'}
}
#Вывод даты
def day_birthday(source, index = -1):
    if index == -1:
        for i in data:
            print(f'{data[i]["surname"]} - {data[i]["birthday"]}', end=' ')
            print()
    else: print(f'{data[index]["surname"]} - {data[index]["birthday"]}', end=' ')

day_birthday(data,0)
print()

#добавление пользователей
def append_info(source):
    new_name = input('Введите Имя ')
    new_surname = input('Введите Фамилию ')
    new_birthday = input('Введите Дату рождения ')
    source[len(source)] = {'name':new_name, 'surname': new_surname, 'birthday' : new_birthday}
    return source[len(source) - 1]
print(append_info(data))

#Запись в файл
def write_file(source,path):
    file = open(path, 'w')
    sup_str = ''
    for i in range(len(source)):
        sup_str+= f'{i} {source[i]["name"]} {source[i]["surname"]} {source[i]["birthday"]}'
        file.writelines(f'{sup_str} \n')
        sup_str = ''
    file.close()

write_file(data,'base_data.txt')

#Чтение с файла
def read_file(path):
    file = open(path, 'r')
    result = {}
    sup_arr = []
    for line in file:
        sup_arr = line.split()
        result[sup_arr[0]] = {'name':sup_arr[1], 'surname': sup_arr[2], 'birthday' : sup_arr[3]}
    file.close()
    return result


print(read_file('base_data.txt'))








