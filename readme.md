Программа реализует алгоритм построения диаграм с помощью python библиотек:
- Turtle
- Argparse

Правила ввода
Для вызова программы необходимо ввести в командной строке:
python chart.py --type chart --text py cpp php php cpp cpp cpp py php py py js html cpp js --color red blue

--type - может принимать только одно значение либо **chart** (круговая диаграмма)
    либо **series** (столбики)
    
--text - принимает множество значений выборки исследования

--color - цвета заливки диаграммы. Если меньше чем количество уникальных значений выборки
    то заполняется дефолтными цветами