import numpy as np
import matplotlib.pyplot as plt

x = np.arange(2, 5, 0.001)
y = 2 * np.exp(-2 * (x - 2))

plt.figure(figsize = (10, 6))

plt.plot(x, y, c = 'r', label = 'y = 2e^(-2(x - 2))')

# Вертикальная линия x = 2
plt.axvline(x = 2, color = 'blue', linestyle = '--', linewidth = 1.5, 
            label = 'x = 2 (мода)')

# Настраиваем оси
plt.axhline(y = 0, color = 'k', linewidth = 0.8)
plt.axvline(x = 0, color = 'k', linewidth = 0.8)

# Добавляем аккуратные стрелки с помощью annotate
plt.annotate("", xy=(5, 0), xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", linewidth=1, color='k')) 
plt.annotate("", xy=(0, 3), xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", linewidth=1, color='k')) 

# Подписи осей
plt.text(4.75, -0.25, 'x', fontsize=12)
plt.text(-0.25, 2.75, 'y', fontsize=12)

# Настройки графика
plt.grid(True, alpha=0.3)
plt.xlim(-1, 5)
plt.ylim(-1, 3)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('data/fig_01.svg')