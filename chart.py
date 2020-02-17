import argparse
import turtle

parser = argparse.ArgumentParser()
parser.add_argument('--type', help='This will be option types')
parser.add_argument('--text', nargs='*', help='This will be option languages')
parser.add_argument('--color', nargs='*', help='This will be option colors')

option = parser.parse_args()

type = option.type
text = option.text
color = list(option.color)
color_defoult = ["#aaa", "#bbb", "#ccc", "#ddd", "#eee", "#fff"]
color.extend(color_defoult)

tur = turtle.Turtle()
tur.screen.setup(1200, 800)
tur2 = turtle.Turtle()

language = dict()

for item in text:
    if language.get(item):
        language[item] = language.get(item) + 1
    else:
        language[item] = 1

if type == "chart":
    i = 0
    ugol = 0
    h = 400 / (len(text))
    for key, value in language.items():
        tur.color(color[i])
        tur2.color(color[i])
        tur.begin_fill()
        tur.left(ugol)
        tur.fd(200)
        tur.left(90)
        ugol += 360 * value / len(text)
        tur.circle(200, 360 * value / len(text))
        tur.home()

        tur2.up()
        tur2.goto(-400, (380 - h * i))
        tur2.down
        tur2.write(f'{key} - {value / len(text) * 100}%')
        tur.end_fill()
        i += 1
elif type == "series":
    tur.fd(400)
    tur.home()
    tur.left(90)
    tur.fd(400)
    tur.home()

    h = 400/(len(text))
    i=0
    for key, value in language.items():
        tur.color(color[i])
        tur2.color(color[i])
        tur.begin_fill()
        tur.fd(h)
        tur.left(90)
        tur.fd(400 * value / len(text))
        tur.left(90)
        tur.fd(h)
        tur.left(90)
        tur.fd(400 * value / len(text))
        tur.left(90)
        tur.fd(h)

        tur2.up()
        tur2.goto(-400,(380-h*i))
        tur2.down
        tur2.write(f'{key} - {value / len(text) *100}%')
        tur.end_fill()

        i += 1

input()
