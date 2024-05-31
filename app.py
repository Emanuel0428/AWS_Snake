import curses
import random

# Configuración inicial
curses.initscr()
win = curses.newwin(20, 60, 0, 0)  # Crea una nueva ventana para el juego
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

# Variables iniciales
snake = [(4, 10), (4, 9), (4, 8)]  # Posiciones iniciales de la serpiente
food = (10, 20)  # Posición inicial de la comida
win.addch(food[0], food[1], '*')
score = 0

ESC = 27  # Código ASCII para la tecla Esc
key = curses.KEY_RIGHT  # Dirección inicial de la serpiente

while key != ESC:
    win.addstr(0, 2, f'Score: {score} ')  # Muestra la puntuación
    win.timeout(150 - (len(snake)//5 + len(snake)//10 % 120))  # Aumenta la velocidad de la serpiente

    prev_key = key
    event = win.getch()
    key = key if event == -1 else event

    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prev_key

    # Calcula la nueva posición de la cabeza de la serpiente
    y = snake[0][0]
    x = snake[0][1]
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1
    snake.insert(0, (y, x))

    # Verifica si la serpiente ha comido la comida
    if snake[0] == food:
        score += 1
        food = ()
        while food == ():
            food = (random.randint(1, 18), random.randint(1, 58))
            if food in snake:
                food = ()
        win.addch(food[0], food[1], '*')
    else:
        tail = snake.pop()
        win.addch(tail[0], tail[1], ' ')

    # Verifica si la serpiente ha chocado con el borde o consigo misma
    if (snake[0][0] in [0, 19] or
        snake[0][1] in [0, 59] or
        snake[0] in snake[1:]):
        break

    win.addch(snake[0][0], snake[0][1], '#')

curses.endwin()
print(f"Final score = {score}")
