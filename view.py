
from additional import data_proc as dp, msg

def get_request():
    frst_choice = int(input ('Выберите действие: \n'
                    '1 - внести изменения в список\n'
                    '2 - вывести данные\n'))
    # for key, value in msg.items:
    #     print(f'{key} - {value}')
        # print(f'{msg[frst_choice]}.keys() - {msg[frst_choice][i]}.values()\n')

    for f, k in msg[frst_choice].items():
        print(f'\t{f} - {k} ')


    sec_choice = int(input())  
    # sec_choice = int(input(msg[frst_choice]))
    # func = data_proc[frst_choice][sec_choice]
    return dp[frst_choice][sec_choice]

# print(get_request())

get_request()
f_add = 'add'
f_del = 'del'
f_all = 'all'
f_class = 'class'
f_id = 'id'

