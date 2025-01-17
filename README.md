# Modeling-2

# Анализ движения электрона в цилиндрическом конденсаторе

## Описание

Этот проект посвящён исследованию движения электрона в электрическом поле цилиндрического конденсатора. Основное внимание уделено моделированию траектории движения электрона под действием электрической силы. Для расчётов используются классические физические формулы, а результаты могут быть визуализированы графически.

Проект поддерживает настройку параметров, таких как напряжение, радиусы цилиндра и свойства электрона.

## Используемые формулы

### Второй закон Ньютона:
F = ma

### Закон Кулона:
F = (q₁ · q₂) / (4πε₀r²)

### Расчёты:
- E = F / q₀
- dF = (λdx) / (4πε₀r²)
- E = ∫[−∞,∞] (λ / (4πε₀r²)) dx = λ / (2πε₀r)
- a = F / m = (E · q) / m
- U = −∫ E dr
- U = −∫[r,R] (λ / (2πε₀r)) dr = −(λ / (2πε₀)) ln(R / r)
- λ = (2πε₀U) / ln(R / r)
- E = λ / (2πε₀r) = U / (r · ln(R / r))

### Итоговые формулы
Напряженность электрического поля:
<p align="center">
  E = λ / (2πε₀r)
</p>

Потенциальная энергия:
<p align="center">
  U = −∫ E dr
</p>

Ускорение частицы в электрическом поле:
<p align="center">
  a = (Ue) / (mr * ln(R / r))
</p>

где:  
- U — напряжение (Вольт),  
- e — заряд электрона (-1.6 × 10<sup>-19</sup> Кулон),  
- m — масса электрона (9.1 × 10<sup>-31</sup> кг),  
- r — текущее расстояние до оси симметрии (м),  
- R - радиус цилиндра (м).

## Как использовать

1. Настройте параметры системы в коде, включая напряжение, радиусы цилиндра и шаг времени.
2. Запустите симуляцию, чтобы рассчитать траекторию движения электрона.
3. Визуализируйте результаты с помощью графиков (например, с использованием `matplotlib`).

## Требования

- Python 3.x
- Библиотеки:
  - numpy
  - matplotlib
 
