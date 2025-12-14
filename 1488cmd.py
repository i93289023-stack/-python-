
'''создание чего то на подобии cmd'''
from tkinter import *
import subprocess
import os
'''делаем функцию'''
def btn_ot():
    '''пишем условия'''
    '''берём настройку с ввода'''
    t_vvod_get = txt_vvod.get("1.0", END).strip()
    '''делаем тестовую команду которая рисует изображение при команде'''
    if t_vvod_get == "fsociety":
        lb_f = Label(tk, bg="black", fg="green", text='''    ⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡇⠀⠀⠀⣠⣤⣶⣾⣿⣿⣿⣿⣿⣿⣷⣶⣦⣄⡀⠀⠀⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡇⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡏⠙⢿⣿⠿⠟⠛⠻⣿⣿⣿⣿⣿⣿⠿⠛⠛⠿⣿⣿⠋⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣟⣉⢸⣤⣾⣿⣷⣄⠀⠙⢻⣿⠋⠀⣠⣾⣿⣷⣤⡇⣉⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣯⣴⣿⢻⣿⠟⠛⠛⢷⣶⣿⣿⣶⡾⠛⠛⠻⣿⡟⣿⣦⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣾⣛⣤⣤⣄⣤⣿⢹⣿⣿⡦⣀⣤⣤⣿⣷⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⡿⢻⣿⣿⣿⣿⡟⣵⣿⣿⣾⣿⣿⣿⣿⣿⡟⢿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⡏⠀⠸⣿⣿⠿⠟⠓⠛⢿⡿⠛⠉⠛⠿⣿⣿⠟⠀⢹⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡇⠈⢦⣤⣤⣤⣤⠤⠤⠤⣀⣀⡠⠤⠤⣤⣤⣤⣤⡾⠁⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡇⠀⠘⣿⣿⣿⣿⣶⣄⣀⡀⠀⣀⣠⣴⣿⣿⣿⣿⠇⠀⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡇⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡇⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡇⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⣿⣿⣿⣿⣿
    ⣿⣿⣿⡏⠁⣀⡀⠀⠀⠀⠀⠉⠉⠉⠉⠉⡉⠉⠉⠀⠀⡀⠀⠀⠀⠉⢹⣿⣿⣿
    ⣿⣿⣿⡇⠠⡯⠅⢴⣒⠂⡖⣶⢰⡶⠆⢲⡆⠀⣖⣶⢸⡗⠂⣶⣶⠀⢸⣿⣿⣿
    ⣿⣿⣿⡇⠀⠃⠀⠒⠚⠈⠓⠛⠘⠛⠃⠚⠓⠀⠓⠂⠈⠓⢂⣙⡿⠀⢸⣿⣿⣿
    ⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⣿⣿

    hacker active''')
        lb_f.place(x=0, y=100)
    '''делаем команду для открытия приложений'''
    if t_vvod_get == "open":
        '''делаем окно для ввода куда пользователь введёт название приложения'''
        t_open = Text(bg="black", fg="green", width=100,height=2)
        t_open.place(x=0, y=50)
        '''сщздаём функцию для ооткрытия приложений'''
        def open_pr():
            try:
                '''берём ввод пользователя'''
                t_open_get = t_open.get('1.0', END).strip()
                '''открываем приложение с вводом'''
                subprocess.Popen([t_open_get])
            except:
                '''делаем если приложение ненайдено то мы сообщаем ошибку'''
                lb_error_pl = Label(bg="black", fg="green", width=20, height=2, text="приложение ненайдено")
                lb_error_pl.place(x=0, y=100)

        '''делаем кнопку для активации'''
        btn_activ = Button(tk, fg="green", bg="black", text="⟹", command=open_pr)
        btn_activ.place(x=815, y=53)
    '''делаем команду на удаление файлов РАБОТАЕТ УДАЛЕНИЕ ТОЛЬКО НА ЛИНУКСЕ'''
    if t_vvod_get == "del":
        '''делаем окно для ввода куда пользователь введёт название приложения'''
        t_remmove = Text(bg="black", fg="green", width=100,height=2)
        t_remmove.place(x=0, y=50)
        def remov_file():
            try:
                '''берём настройки с ввода'''
                t_remmove_get = t_remmove.get('1.0', END).strip()
                '''узнаём имя пользователя'''
                ima_remove = os.getlogin()
                '''делаем путь до файла пользователя из домашней папки пользователя'''
                pyt1 = f"/home/{ima_remove}/{t_remmove_get}"
                '''удаляем файл из получившегося пути который указал пользователь'''
                os.remove(pyt1)
            except:
                '''делаем если файл ненайдено то мы сообщаем ошибку'''
                lb_error_del = Label(bg="black", fg="green", width=20, height=2, text="файл ненайдено")
                lb_error_del.place(x=0, y=200)

        btn_activ_del = Button(tk, fg="green", bg="black", text="⟹", command=remov_file)
        btn_activ_del.place(x=815, y=53)
    '''делаем команду для добавлеения файла'''
    if t_vvod_get == "create_file":
        '''делаем окно для ввода куда пользователь введёт название файла'''
        t_create = Text(bg="black", fg="green", width=100, height=2)
        t_create.place(x=0, y=50)

        def create_file():
            try:
                '''берём содержимое ввода'''
                t_create_get = t_create.get('1.0', END).strip()
                '''берём имя пользователя что бы сделать нормальный путь'''
                ima_create = os.getlogin()
                '''состовляем путь до домашней папки'''
                pyt_create = f"/home/{ima_create}/"
                '''склеиваем наш путь в один полный путь'''
                fulll_pyt = os.path.join(pyt_create, t_create_get)
                '''создаём файл уже с названием который хочет пользователь'''
                with open(fulll_pyt, "w") as f:
                    f.write(" ")
            except:
                '''делаем если пользователь хочет создать файл не в домашней папке то мы сообщаем что пока что можно
                 создать файл в домашней  папке'''
                lb_error_del = Label(bg="black", fg="green", width=20, height=2, text="пока можно сдлать файл в домашней папке")
                lb_error_del.place(x=0, y=200)

        btn_activ_del = Button(tk, fg="green", bg="black", text="⟹", command=create_file)
        btn_activ_del.place(x=815, y=53)


tk = Tk()
tk.geometry("1000x650")
'''делаем что бы окно нельзя юыло изменять в размере'''
tk.resizable(False, False)
'''делаем окно чёрным'''
tk.config(bg="black")
'''делаем название окну'''
tk.title("1488cmd")
'''делаем поле ввода'''
txt_vvod = Text(tk, bg="black", width=110, height=2, fg="green")
txt_vvod.place(x=0, y=0)
'''делаем кнопку'''
btn_otpravka = Button(tk, bg="black", fg="green", text="⟹", command=btn_ot)
btn_otpravka.place(y=2, x=900)

tk.mainloop()
