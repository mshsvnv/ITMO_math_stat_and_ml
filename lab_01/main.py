import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 26, 1)

# Создаем график
plt.figure(figsize=(10, 6))

# Ограничиваем красные линии в пределах [0,25] по обеим осям
# Для линии y = x + 1: ограничиваем где y <= 25
mask_upper = (x + 1) <= 25
x_upper = x[mask_upper]
y_upper = x_upper + 1

# Для линии y = x - 1: ограничиваем где y >= 0
mask_lower = (x - 2) >= 0
x_lower = x[mask_lower]
y_lower = x_lower - 2

# Рисуем ограниченные прямые
plt.plot(x_upper, y_upper, c='r', label='y = x + 1')
plt.plot(x_lower, y_lower, c='g', label='y = x - 2')

# Закрашиваем области с ограничениями
# Область ВЫШЕ верхней прямой (y > x + 1), но только в пределах графика
plt.fill_between(x_upper, y_upper, 25, alpha=0.3, color='red', label='Зона без ожидания 2го')

# Область НИЖЕ нижней прямой (y < x - 2), но только в пределах графика
plt.fill_between(x_lower, 0, y_lower, alpha=0.3, color='g', label='Зона без ожидания 1го')

# Настраиваем оси
plt.axhline(y=0, color='k', linewidth=0.8)  # горизонтальная ось (x-ось)
plt.axvline(x=0, color='k', linewidth=0.8)  # вертикальная ось (y-ось)

# Добавляем стрелки на осях
plt.arrow(25, 0, 0.5, 0, head_width=1, head_length=0.5, fc='k', ec='k')  # стрелка на x-оси
plt.arrow(0, 25, 0, 0.5, head_width=1, head_length=0.5, fc='k', ec='k')  # стрелка на y-оси

# Подписи осей
plt.text(26, -1, 'x', fontsize=12)
plt.text(-1, 26, 'y', fontsize=12)

# Настройки графика
plt.grid(True, alpha=0.3)
plt.xlim(-2, 27)
plt.ylim(-2, 27)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.savefig('fig.svg')