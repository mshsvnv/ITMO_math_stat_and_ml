import numpy as np
import matplotlib.pyplot as plt

# БЛОК 1: Первый график (прямые и закрашенные области)
x = np.arange(0, 26, 1)

plt.figure(figsize=(10, 6))

# Ограничиваем красные линии в пределах [0,25] по обеим осям
mask_upper = (x + 1) <= 25
x_upper = x[mask_upper]
y_upper = x_upper + 1

mask_lower = (x - 2) >= 0
x_lower = x[mask_lower]
y_lower = x_lower - 2

# Рисуем ограниченные прямые
plt.plot(x_upper, y_upper, c='r', label='y = x + 1')
plt.plot(x_lower, y_lower, c='g', label='y = x - 2')

# Закрашиваем области с ограничениями
plt.fill_between(x_upper, y_upper, 25, alpha=0.3, color='red', label='Зона без ожидания 2го')
plt.fill_between(x_lower, 0, y_lower, alpha=0.3, color='g', label='Зона без ожидания 1го')

# Настраиваем оси
plt.axhline(y=0, color='k', linewidth=0.8)  # горизонтальная ось (x-ось)
plt.axvline(x=0, color='k', linewidth=0.8)  # вертикальная ось (y-ось)

# Добавляем аккуратные стрелки с помощью annotate
plt.annotate("", xy=(25, 0), xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", linewidth=1, color='k'))  # стрелка на x-оси
plt.annotate("", xy=(0, 25), xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", linewidth=1, color='k'))  # стрелка на y-оси

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
plt.savefig('fig_01.svg')

# Очищаем фигуру для второго графика
plt.clf()  # или plt.close()

# БЛОК 2: Второй график (cos(x))
x = np.arange(-np.pi, np.pi, step=0.01)
y = np.cos(x)

plt.figure(figsize=(10, 6))  # Создаем новую фигуру
plt.plot(x, y, label = 'η1 = cos(ξ)')

# Настраиваем оси
plt.axhline(y=0, color='k', linewidth=0.8)
plt.axvline(x=0, color='k', linewidth=0.8)

# Добавляем аккуратные стрелки с помощью annotate
plt.annotate("", xy=(np.pi, 0), xytext=(-np.pi, 0),
            arrowprops=dict(arrowstyle="->", linewidth=1, color='k'))  # стрелка на x-оси
plt.annotate("", xy=(0, 1), xytext=(0, -1),
            arrowprops=dict(arrowstyle="->", linewidth=1, color='k'))  # стрелка на y-оси

# Подписи осей
plt.text(np.pi + 0.2, -0.2, 'ξ', fontsize=12)
plt.text(-0.25, 1.2, 'η1', fontsize=12)

# Настройки графика
plt.grid(True, alpha=0.3)
plt.legend()

# Сохраняем второй график отдельно
plt.savefig('fig_02.svg')

# Очищаем фигуру для второго графика
plt.clf()  # или plt.close()

# БЛОК 2: Второй график (cos(x))
x = np.arange(-np.pi, np.pi, step=0.01)
y = np.sin(x)

plt.figure(figsize=(10, 6))  # Создаем новую фигуру
plt.plot(x, y, label = 'η2 = sin(ξ)')

# Настраиваем оси
plt.axhline(y=0, color='k', linewidth=0.8)
plt.axvline(x=0, color='k', linewidth=0.8)

# Добавляем аккуратные стрелки с помощью annotate
plt.annotate("", xy=(np.pi, 0), xytext=(-np.pi, 0),
            arrowprops=dict(arrowstyle="->", linewidth=1, color='k'))  # стрелка на x-оси
plt.annotate("", xy=(0, 1), xytext=(0, -1),
            arrowprops=dict(arrowstyle="->", linewidth=1, color='k'))  # стрелка на y-оси

# Подписи осей
plt.text(np.pi + 0.2, -0.2, 'ξ', fontsize=12)
plt.text(-0.25, 1.2, 'η2', fontsize=12)

# Настройки графика
plt.grid(True, alpha=0.3)
plt.legend()

# Сохраняем второй график отдельно
plt.savefig('fig_03.svg')

plt.clf()

# БЛОК 3: График с осями ξ и t, прямые t = ξ и t = ξ - 1, t >= 0

plt.figure(figsize=(10, 6))  # Создаем новую фигуру

# Генерируем значения для оси ξ (аналог x)
xi = np.arange(0, 6, 0.1)  # диапазон от 0 до 6 с шагом 0.1 (чтобы t = ξ-1 >= 0)

# Вычисляем значения для прямых t = ξ и t = ξ - 1
t1 = xi  # t = ξ
t2 = xi - 1  # t = ξ - 1

# Фильтруем значения, чтобы соблюсти условие t >= 0 для второй прямой
mask = t2 >= 0
xi_filtered = xi[mask]
t2_filtered = t2[mask]

# Рисуем прямые
plt.plot(xi, t1, c='b', label='t = ξ')
plt.plot(xi_filtered, t2_filtered, c='orange', label='t = ξ - 1')

# Закрашиваем область между прямыми (где t1 > t2)
plt.fill_between(xi_filtered, t2_filtered, t1[mask], alpha=0.3, color='lightblue')

# Настраиваем оси
plt.axhline(y=0, color='k', linewidth=0.8)  # горизонтальная ось (t-ось)
plt.axvline(x=0, color='k', linewidth=0.8)  # вертикальная ось (ξ-ось)

# Добавляем аккуратные стрелки с помощью annotate
plt.annotate("", xy=(6, 0), xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", linewidth=1, color='k'))  # стрелка на оси ξ
plt.annotate("", xy=(0, 5), xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", linewidth=1, color='k'))  # стрелка на оси t

# Подписи осей
plt.text(6.2, -0.25, 'ξ', fontsize=12)
plt.text(-0.25, 5.2, 't', fontsize=12)

# Настройки графика
plt.grid(True, alpha=0.3)
plt.xlim(-0.5, 6.5)
plt.ylim(-0.5, 5.5)
plt.legend()

# Сохраняем график
plt.savefig('fig_04.svg')
