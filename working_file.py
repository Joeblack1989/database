import os
import r_w_file

def append_info(source, path):
    new_name = input('Введите Имя ')
    new_surname = input('Введите Фамилию ')
    new_class = input('Введите номер класса ')
    if os.stat(path).st_size == 0: index = 0
    else:
        index_list = list(map(lambda el:int(el),source))
        index = int(max(index_list))+1
    source[index] = {'name':new_name, 'surname': new_surname, 'class' : new_class}
    r_w_file.write_file(source, path)
    return source

def del_info(source, path):
    index = input('Введите индекс пользователя, которого необходимо удалить: ')
    del source[index]
    r_w_file.write_file(source, path)
    return source