# Примеры построения графиков

import tkinter as tk

# Импорт внешних файлов
import Chart1

# Функция закрытия программы
def do_close():
    window.destroy()

# Создание главного окна 
window = tk.Tk()
window.geometry("550x550")
window.title("Примеры построения графиков")

# Добавление метки заголовка
lblTitle = tk.Label(text = "Примеры построения графиков", font = ('Tahoma', 14, 'bold'), fg = '#0000FF')
lblTitle.place(x=65, y=45)

# Добавление кнопки и метки заголовка 
btnChart1 = tk.Button(window, text="График 1", font = ('Tahoma', 10, 'bold'),command=Chart1.plot_chart)
btnChart1.place(x=40, y=115, width=100, height=30)

lblChart1 = tk.Label(text = "График синуса MatPlotLib")
lblChart1.place (x= 170, y=122)

# Добавление кнопки закрытия программы
btnClose = tk.Button(window, text= "Закрыть", font = ('Helvetica', 10, 'bold'), command=do_close)
btnClose.place(x=400, y=480, width=90, height=30)

# Запуск цикла mainloop
window.mainloop()



