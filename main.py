import math
import matplotlib.pyplot as plt
import numpy as np

# Константы
CHARGE = -1.6e-19  # Заряд электрона (Кулоны)
MASS = 9.1e-31  # Масса электрона (кг)

# Размеры конденсатора (в метрах)
RADIUS_OUTER = 6 * 1e-2  # Внешний радиус конденсатора (м)
RADIUS_INNER = 2.5 * 1e-2  # Внутренний радиус конденсатора (м)
LENGTH = 14 * 1e-2  # Длина конденсатора (м)

# Начальная скорость электрона (м/с)
VX0 = 7.5e6  # Начальная скорость вдоль оси X (м/с)

# Параметры точности и временного шага
PRECISION = 1e-7  # Точность вычислений
TIME_STEP_POWER = 11  # Степень для расчета временного шага
TIME_STEP = 10 ** -TIME_STEP_POWER  # Временной шаг (с)
T_MAX = LENGTH / VX0  # Максимальное время полета (с)

# Логарифм отношения радиусов
LN_RATIO = math.log(RADIUS_OUTER / RADIUS_INNER)

# Функция для вычисления ускорения электрона
def calculate_acceleration(voltage, position):
    """
    Функция для вычисления ускорения электрона на основе напряжения и положения.
    Позиция - это расстояние от оси симметрии конденсатора.
    """
    return (voltage * CHARGE) / (MASS * position * LN_RATIO)

# Функция для обновления позиции
def update_position(position, velocity, acceleration, dt):
    """
    Функция для обновления положения электрона на основе скорости и ускорения.
    """
    return position + velocity * dt + 0.5 * acceleration * dt ** 2

# Функция для обновления скорости
def update_velocity(velocity, acceleration, dt):
    """
    Функция для обновления скорости электрона на основе ускорения.
    """
    return velocity + acceleration * dt

# Метод бинарного поиска для нахождения минимального напряжения
def binary_search_voltage():
    """
    Функция для нахождения минимального напряжения, при котором электрон
    не выйдет за пределы конденсатора.
    """
    lower_bound, upper_bound = 0, 1000  # Начальные границы для поиска
    while (upper_bound - lower_bound) / upper_bound > PRECISION:  # Точность поиска
        voltage_mid = (upper_bound + lower_bound) / 2  # Текущее значение напряжения
        position, velocity = (RADIUS_OUTER + RADIUS_INNER) / 2, 0  # Начальная позиция и скорость
        acceleration = calculate_acceleration(voltage_mid, position)  # Начальное ускорение
        exited = False  # Флаг выхода за пределы

        # Моделирование движения электрона
        for _ in range(int(T_MAX / TIME_STEP)):  # Проходим по времени до T_MAX
            position = update_position(position, velocity, acceleration, TIME_STEP)  # Обновляем положение
            velocity = update_velocity(velocity, acceleration, TIME_STEP)  # Обновляем скорость
            acceleration = calculate_acceleration(voltage_mid, position)  # Обновляем ускорение

            # Проверяем, не вышел ли электрон за пределы
            if position < RADIUS_INNER or position > RADIUS_OUTER:
                exited = True
                break
        
        # Если электрон вышел, уменьшаем напряжение, иначе увеличиваем
        if exited:
            upper_bound = voltage_mid
        else:
            lower_bound = voltage_mid

    return upper_bound

# Нахождение минимального напряжения
required_voltage = binary_search_voltage()

# Расчет конечной скорости электрона
final_velocity = math.sqrt(VX0 ** 2 + (calculate_acceleration(required_voltage, (RADIUS_OUTER + RADIUS_INNER) / 2) * T_MAX) ** 2)

print(f"Требуемое напряжение: {required_voltage:.10f} V")
print(f"Скорость: {final_velocity:.10f} м/с")
print(f"Время: {T_MAX:.10f} с")

# Моделирование движения электрона
positions = [(RADIUS_OUTER + RADIUS_INNER) / 2]  # Начальная позиция
velocities = [0]  # Начальная скорость
accelerations = [calculate_acceleration(required_voltage, positions[-1])]  # Начальное ускорение
times = [0]  # Начальное время

# Интеграция по времени
for step in range(1, int(T_MAX / TIME_STEP)):
    new_position = update_position(positions[-1], velocities[-1], accelerations[-1], TIME_STEP)
    new_velocity = update_velocity(velocities[-1], accelerations[-1], TIME_STEP)
    new_acceleration = calculate_acceleration(required_voltage, new_position)

    positions.append(new_position)
    velocities.append(new_velocity)
    accelerations.append(new_acceleration)
    times.append(step * TIME_STEP)

# Графики зависимости
x_positions = np.linspace(0, LENGTH, len(times))

# Построение графиков
fig, axs = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle("Анализ движения частицы")

# График зависимости y(x)
axs[0, 0].plot(x_positions, positions, color='blue')
axs[0, 0].set_title("y(x)")
axs[0, 0].set_xlabel("x, м")
axs[0, 0].set_ylabel("y, м")
axs[0, 0].grid(True)

# График зависимости v(t)
axs[0, 1].plot(times, velocities, color='green')
axs[0, 1].set_title("v(t)")
axs[0, 1].set_xlabel("t, с")
axs[0, 1].set_ylabel("v, м/с")
axs[0, 1].grid(True)

# График зависимости a(t)
axs[1, 0].plot(times, accelerations, color='red')
axs[1, 0].set_title("a(t)")
axs[1, 0].set_xlabel("t, с")
axs[1, 0].set_ylabel("a, м/с^2")
axs[1, 0].grid(True)

# График зависимости y(t)
axs[1, 1].plot(times, positions, color='purple')
axs[1, 1].set_title("y(t)")
axs[1, 1].set_xlabel("t, с")
axs[1, 1].set_ylabel("y, м")
axs[1, 1].grid(True)

plt.tight_layout()
plt.show()
