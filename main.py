"""
Практическая работа №0
Выполнил Удалов Егор, гр. КИ21-16/1б
Визуализация фрактала (обнаженное обдуваемое ветром дерево Пифагора) с использованием Turtle
"""

import typing
import turtle as pointer
from conf import get_config


def tree(size: typing.Any, levels: int, angle: int) -> None:
    """
    :param size размер шага
    :param levels количество уровней
    :param angle угол наклона
    """
    if levels == 0:
        pointer.color("green")
        pointer.dot(size)
        return

    pointer.pencolor(0, 254 // levels, 0)

    pointer.forward(size)
    pointer.right(angle)

    tree(size * 0.8, levels - 1, angle)

    pointer.pencolor(0, 254 // levels, 0)

    pointer.left(angle * 2)

    tree(size * 0.8, levels - 1, angle)

    pointer.pencolor(0, 254 // levels, 0)

    pointer.right(angle)

    pointer.backward(size)


def main():
    """
    Точка входа, подключаем конфиг из conf.py, запускаем ф-ю tree
    """
    Config = get_config()

    pointer.speed(Config.speed)
    pointer.colormode(Config.colormode)
    pointer.width(Config.width)

    pointer.left(90)

    tree(Config.size,
         Config.levels,
         Config.angle)

    pointer.mainloop()


if __name__ == '__main__':
    main()
