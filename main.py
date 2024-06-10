from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *
import time
import webbrowser
# Импорт библеотек для светомузыки епта

desk = GetDC(0)
x = GetSystemMetrics(0) # Получаем ширину экрана
y = GetSystemMetrics(1) # Уже высоту

for i in range (10000): # Сколько циклов
    brush = CreateSolidBrush(RGB( # Конфигурируем цвет
                      
        randrange(255), # Красный
        1, # Зелёнка
        randrange(82), # Синий
        ))
    webbrowser.open("https://github.com/D3sp1r4t/")
    webbrowser.open_new_tab("https://d3sp1r4t.itch.io/")
    webbrowser.open_new_tab("https://www.youtube.com/@deraid.7")
    SelectObject(desk, brush) # Выбираем цвет которым будем рисовать
    PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), PATINVERT) # Начинаем свето-музыку а именно инвертируем цвета экрана в разных его частях
    DeleteObject(brush) # Освобождает ОЗУ. Нужная херь.
    time.sleep(0.001) # Задержка цикла
DeleteDC(desk) # Эта херь сделана для воизбежания утечек ОЗУ