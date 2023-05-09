# Примеры построения графиков

import tkinter as tk

# Импорт внешних файлов
import Chart1
import Chart2
import Chart3


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

# Добавление кнопки и метки для графика 1 
btnChart1 = tk.Button(window, text="График 1", font = ('Tahoma', 10, 'bold'),command=Chart1.plot_chart)
btnChart1.place(x=40, y=120, width=100, height=30)

lblChart1 = tk.Label(text = "График синуса MatPlotLib")
lblChart1.place (x= 170, y=125)

# Добавление кнопки и метки для графика 2 
btnChart1 = tk.Button(window, text="График 2", font = ('Tahoma', 10, 'bold'),command=Chart2.plot_chart)
btnChart1.place(x=40, y=170, width=100, height=30)

lblChart1 = tk.Label(text = "Нормальное распределение")
lblChart1.place (x= 170, y=175)

# Добавление кнопки и метки для графика 3 
btnChart1 = tk.Button(window, text="График 3", font = ('Tahoma', 10, 'bold'),command=Chart2.plot_chart2)
btnChart1.place(x=40, y=220, width=100, height=30)

lblChart1 = tk.Label(text = "Нормальное распределение 3 графика")
lblChart1.place (x= 170, y=225)

# Добавление кнопки и метки для графика 4 
btnChart1 = tk.Button(window, text="График 4", font = ('Tahoma', 10, 'bold'),command=Chart3.plot_chart)
btnChart1.place(x=40, y=270, width=100, height=30)

lblChart1 = tk.Label(text = "Гистограмма Seaborn")
lblChart1.place (x= 170, y=275)

# Добавление кнопки и метки для графика 5 
btnChart1 = tk.Button(window, text="График 5", font = ('Tahoma', 10, 'bold'),command=Chart2.plot_chart)
btnChart1.place(x=40, y=320, width=100, height=30)

lblChart1 = tk.Label(text = "Место для графика")
lblChart1.place (x= 170, y=325)

# Добавление кнопки и метки для графика 6 
btnChart1 = tk.Button(window, text="График 6", font = ('Tahoma', 10, 'bold'),command=Chart2.plot_chart)
btnChart1.place(x=40, y=370, width=100, height=30)

lblChart1 = tk.Label(text = "Место для графика")
lblChart1.place (x= 170, y=375)

# Добавление кнопки и метки для графика 7 
btnChart1 = tk.Button(window, text="График 7", font = ('Tahoma', 10, 'bold'),command=Chart2.plot_chart)
btnChart1.place(x=40, y=420, width=100, height=30)

lblChart1 = tk.Label(text = "Место для графика")
lblChart1.place (x= 170, y=425)


# Добавление кнопки закрытия программы
btnClose = tk.Button(window, text= "Закрыть", font = ('Tahoma', 10, 'bold'), command=do_close)
btnClose.place(x=400, y=480, width=90, height=30)

# Запуск цикла mainloop
window.mainloop()



