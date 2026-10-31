from tkinter import *

win_1 = Tk()
win_1.title("Высчитыватель баллов")
win_1.geometry("450x225")
win_1.iconbitmap('Icon.ico')
win_1.resizable(10, 10)


global text_10, text_11, text_12, text_13, text_14, text_15
text_10 = Label(text="Отлично")
text_11 = Label(text="Хорошо")
text_12 = Label(text="Удовлетворительно")
text_13 = Label(text="Плохо")
text_14 = Label(text="Очень плохо")
text_15 = Label(text="Нулевая оценка")

def text_1_destroy():
    try:
        text_1.destroy()
    except NameError:
        pass

def text_2_destroy():
    try:
        text_2.destroy
    except NameError:
        pass

def text_3_destroy():
    try:
        text_3.destroy()
    except NameError:
        pass

def text_4_destroy():
    try:
        text_4.destroy()
    except NameError:
        pass

def text_5_destroy():
    try:
        text_5.destroy()
    except NameError:
        pass
def text_6_destroy():
    global text_6
    try:
        text_6.destroy()
    except NameError:
        pass

def text_7_destroy():
    global text_7
    try:
        text_7.destroy()
    except NameError:
        pass

def text_8_destroy():
    global text_8
    try:
        text_8.destroy()
    except NameError:
        pass

def text_9_destroy():
    global text_9
    try:
        text_9.destroy()
    except NameError:
        pass

def text_10_destroy():
    try:
        text_10.destroy()
    except NameError:
        pass

def text_11_destroy():
    try:
        text_11.destroy()
    except NameError:
        pass

def text_12_destroy():
    try:
        text_12.destroy()
    except NameError:
        pass

def text_13_destroy():
    try:
        text_13.destroy()
    except NameError:
        pass

def text_14_destroy():
    try:
        text_14.destroy()
    except NameError:
        pass

def text_15_destroy():
    try:
        text_15.destroy()
    except NameError:
        pass

def text_16_destroy():
    try:
        text_16.destroy()
    except NameError:
        pass

def text_17_destroy():
    try:
        text_17.destroy()
    except NameError:
        pass

def text_18_destroy():
    try:
        text_18.destroy()
    except NameError:
        pass

def text_19_destroy():
    try:
        text_19.destroy()
    except NameError:
        pass

def text_20_destroy():
    try:
        text_20.destroy()
    except NameError:
        pass

def button_1_destroy():
    try:
        button_1.destroy()
    except NameError:
        pass

def button_2_destroy():
    try:
        button_2.destroy()
    except NameError:
        pass

def button_3_destroy():
    try:
        button_3.destroy()
    except NameError:
        pass

def button_4_destroy():
    try:
        button_4.destroy()
    except NameError:
        pass

def button_5_destroy():
    try:
        button_5.destroy()
    except NameError:
        pass

def button_6_destroy():
    try:
        button_6.destroy()
    except NameError:
        pass

def button_10_destroy():
    try:
        button_10.destroy()
    except NameError:
        pass

def button_11_destroy():
    try:
        button_11.destroy()
    except NameError:
        pass

def entry_1_destroy():
    try:
        entry_1.destroy()
    except NameError:
        pass

def entry_2_destroy():
    try:
        entry_2.destroy()
    except NameError:
        pass
    

def button_4_command():
    win_2 = Tk()
    win_2.title("О приложении")
    win_2.geometry("450x300")
    win_2.iconbitmap('Icon.ico')
    win_2.resizable(False, False)

    global text_16, text_17, text_18

    canvas_1 = Canvas(master=win_2, width=450, height=80, bg="#f0f0f0")
    canvas_1.pack()

    canvas_1.create_rectangle(10, 10, 440, 70, fill="#f0f0f0", outline="#000000", width=4)

    canvas_1.create_text(225, 40, text="Высчитыватель баллов", font="Impact 20", fill="#000000")

    text_16 = Label(master=win_2, text="Это приложение создано для перевода оценок в пятибалльную шкалу.")
    text_16.place(x=10, y=90)

    text_17 = Label(master=win_2, text="Оно разработано на Python с использованием библиотеки Tkinter.")
    text_17.place(x=10, y=110)

    text_18 = Label(master=win_2, text="Автор: \/@$!L¡Y")
    text_18.place(x=10, y=130)

    global button_5

    button_5 = Button(master=win_2, text="Закрыть", command=win_2.destroy)
    button_5.place(x=10, y=160)

def button_1_command():

    text_1_destroy()
    text_2_destroy()
    text_3_destroy()
    button_1_destroy()
    text_4_destroy()
    text_5_destroy()
    text_6_destroy()
    text_7_destroy()
    text_8_destroy()
    text_9_destroy()
    text_10_destroy()
    text_11_destroy()
    text_12_destroy()
    text_13_destroy()
    text_14_destroy()
    text_15_destroy()
    # text_16_destroy()
    # text_17_destroy()
    # text_18_destroy()
    text_19_destroy()
    text_20_destroy()
    button_2_destroy()
    button_3_destroy()
    button_4_destroy()
    # button_5_destroy()
    button_6_destroy()
    button_10_destroy()
    button_11_destroy()
    entry_1_destroy()
    entry_2_destroy()

    def button_2_command():
        text_4_destroy()
        text_5_destroy()

        button_2_destroy()

        if entry_1.get() == "" or entry_2.get() == "":
            
            entry_1_destroy()
            entry_2_destroy()

            global text_19

            text_19 = Label(text="Ошибка! Параметры не заданы.")
            text_19.place(x=10, y=10)

            global button_10

            button_10 = Button(text="Повторить попытку", command=button_1_command)
            button_10.place(x=10, y=30)
        
        else:
            
            try:
                poluchil = float(entry_1.get())
                vsego = float(entry_2.get())

                entry_1_destroy()
                entry_2_destroy()
        
                if vsego < poluchil or vsego == 0:

                    global text_6

                    text_6 = Label(text="Ошибка! Параметры заданы неверно.")
                    text_6.place(x=10, y=10)

                    global button_6

                    button_6 = Button(text="Повторить попытку", command=button_1_command)
                    button_6.place(x=10, y=30)
                else:
                    otvet = int(round(poluchil * 5 / vsego))

                    global text_7
            
                    text_7 = Label(text="Готово! У вас:")
                    text_7.place(x=10, y=10)

                    global text_8

                    text_8 = Label(text=otvet, font="Arial 20", bg="#000000", fg="#f0f0f0")
                    text_8.place(x=10, y=40)

                    global text_9

                    text_9 = Label(text="из 5 баллов")
                    text_9.place(x=10, y=85)

                    if otvet == 5:
                        text_result = Label(text="Отлично")
                    elif otvet == 4:
                        text_result = Label(text="Хорошо")
                    elif otvet == 3:
                        text_result = Label(text="Удовлетворительно")
                    elif otvet == 2:
                        text_result = Label(text="Плохо")
                    elif otvet == 1:
                        text_result = Label(text="Очень плохо")
                    elif otvet == 0:
                        text_result = Label(text="Нулевая оценка")
                    else:
                        text_result = Label(text="Оценка не определена.")
                        text_result.place(x=10, y=100)

                    def button_7_command():
                        text_result.destroy()
                        button_7.destroy()
                        button_8.destroy()
                        button_9.destroy()
                        button_1_command()

                    button_7 = Button(text="Ещё раз", command=button_7_command)
                    button_7.place(x=10, y=130)

                    button_8 = Button(text="Выход", command=win_1.destroy)
                    button_8.place(x=175, y=130)

                    button_9 = Button(text="О приложении", command=button_4_command)
                    button_9.place(x=70, y=130)
            except ValueError:
                pass

                entry_1_destroy()
                entry_2_destroy()

                global text_20

                text_20 = Label(text="Ошибка! Введены некорректные данные.")
                text_20.place(x=10, y=10)

                global button_11

                button_11 = Button(text="Повторить попытку", command=button_1_command)
                button_11.place(x=10, y=30)

            


            
    global text_4

    text_4 = Label(text="Сколько баллов вы получили?")
    text_4.place(x=10, y=10)

    global entry_1

    entry_1 = Entry()
    entry_1.place(x=200, y=10)

    global text_5

    text_5 = Label(text="Сколько баллов всего?")
    text_5.place(x=10, y=40)

    global entry_2

    entry_2 = Entry()
    entry_2.place(x=200, y=40)

    global button_2

    button_2 = Button(text="Ввод", command=button_2_command)
    button_2.place(x=10, y=70)

text_1 = Label(text="Привет! Я Гоша, который переводит ваши оценки в пятибалльную шкалу.")
text_1.place(x=10, y=10)

def text_2_destroy():
    text_2.destroy()

text_2 = Label(text="Всё просто! Вы пишите свою оценку, а я её обработаю.")
text_2.place(x=10, y=30)

text_3 = Label(text="Давайте начнём!")
text_3.place(x=10, y=50)

def button_1_destroy():
    button_1.destroy()

button_1 = Button(text="Начать", command=button_1_command)
button_1.place(x=10, y=70)

button_3 = Button(text="Выход", command=win_1.destroy)
button_3.place(x=175, y=70)

button_4 = Button(text="О приложении", command=button_4_command)
button_4.place(x=70, y=70)






win_1.mainloop()

