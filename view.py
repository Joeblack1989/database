# import os

import additional as ad

# from database import path_txt as pt, data as dt

def get_request():
    frst_choice = int(input ('Выберите действие: \n'
                    '\t1 - внести изменения в список\n'
                    '\t2 - вывести данные\n'))
    for f, k in ad.msg[frst_choice].items():
        print(f'\t{f} - {k} ')
    sec_choice = int(input())  
    return ad.data_proc[frst_choice][sec_choice]

# func = get_request()

print(get_request())