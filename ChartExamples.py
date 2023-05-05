# Примеры построения графиков

import tkinter as tk

# Функция закрытия программы
def do_close():
    window.destroy()

# Создание главного окна 
window = tk.Tk()
window.geometry("550x550")
window.title("Примеры построения графиков")

# Добавление кнопки закрытия программы
btnClose = tk.Button(window, text= "Закрыть", font = ('Helvetica', 10, 'bold'), command=do_close)
btnClose.place(x=400, y=480, width=90, height=30)

# Запуск цикла mainloop
window.mainloop()



