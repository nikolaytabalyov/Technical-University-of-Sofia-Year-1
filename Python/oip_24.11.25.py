import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.io # Импортирано за пълна съвместимост, както е зададено

# 2. Дефиниране на константи и променливи
classroom_width = 7  # Ширина на учебната зала в метри
classroom_length = 5 # Дължина на учебната зала в метри

num_ap = 5           # Брой точки за достъп (AP)
population_size = 12 # Големина на популацията
generations = 10     # Брой поколения
mutation_rate = 0.1  # Скорост на мутация (10%)

# 3. Функция за изчисляване на силата на сигнала:
def calculate_signal_strength(ap_x, ap_y, point_x, point_y):
    """
    Изчислява силата на Wi-Fi сигнала в дадена точка, базирана на обратния модел на разстоянието.
    """
    distance = np.sqrt((ap_x - point_x)**2 + (ap_y - point_y)**2)
    return 1 / (distance + 1) # Обратен модел на разстоянието

# 4. Функция за визуализация на начални и крайни позиции на точките за достъп:
def visualize_initial_and_final(classroom_width, classroom_length, initial_population, final_population):
    """
    Визуализира началното и крайното разпределение на точките за достъп.
    """
    plt.figure(figsize=(10, 6))

    # Начални случайни точки
    for i, (x, y) in enumerate(initial_population):
        plt.text(x, y, str(i+1), color='black', fontsize=8, ha='center', va='center')
    plt.scatter(*zip(*initial_population), color='red', marker='o', label="Начална позиция на точките за достъп до Wi-Fi")

    # Крайно разпределение
    for i, (x, y) in enumerate(final_population):
        plt.text(x, y, str(i+1), color='black', fontsize=8, ha='center', va='center')
    plt.scatter(*zip(*final_population), color='blue', marker='o', label="Финална позиция на точките за достъп до Wi-Fi")

    plt.xlabel('Ширина на учебна зала (м)')
    plt.ylabel('Дължина на учебна зала (м)')
    plt.title('Начално и крайно разпределение на точките за достъп')
    plt.xlim(0, classroom_width)
    plt.ylim(0, classroom_length)
    plt.grid(True)
    plt.legend()
    plt.show()

# 5. Функция за динамична визуализация на промените:
def visualize_dynamic_changes(classroom_width, classroom_length, population, fitness_scores):
    """
    Динамично визуализира промените в разположението на точките за достъп и фитнес резултатите през поколенията.
    """
    for generation in range(generations):
        plt.figure(figsize=(15, 6))

        # === Лява графика: Топлинна карта и AP разпределение ===
        plt.subplot(1, 2, 1)

        # Избираме първите num_ap точки от текущата популация за визуализация на разположението
        ap_placements = population[generation][:num_ap]

        # Генериране на мрежа от точки
        x = np.linspace(0, classroom_width, 100)
        y = np.linspace(0, classroom_length, 100)
        X, Y = np.meshgrid(x, y)
        Z = np.zeros_like(X)

        # Изчисляване на общата сила на сигнала (Z) за всяка точка в стаята
        for ap_x, ap_y in ap_placements:
            Z += calculate_signal_strength(ap_x, ap_y, X, Y)

        plt.pcolormesh(X, Y, Z, shading='auto', cmap='viridis')
        plt.colorbar(label='Сила на сигнала')

        # Изобразяване на AP точките
        for i, (x_coord, y_coord) in enumerate(ap_placements):
            plt.text(x_coord, y_coord, str(i + 1), color='black', fontsize=8, ha='center', va='center')
        plt.scatter(*zip(*ap_placements), color='red', marker='o', label="Разпределение на точките за достъп")

        plt.xlabel("Ширина на учебна зала (м)")
        plt.ylabel('Дължина на учебна зала (м)')
        plt.title(f'Сила на Wi-Fi сигнала и разпределение на точките за достъп (Поколение {generation + 1})')
        plt.xlim(0, classroom_width)
        plt.ylim(0, classroom_length)
        plt.legend()

        # === Дясна графика: Фитнес резултати през поколенията ===
        plt.subplot(1, 2, 2)
        plt.plot(range(1, generation + 2), fitness_scores[:generation + 1], marker='o')
        plt.xlabel("Поколение")
        plt.ylabel('Резултат от фитнеса')
        plt.title('Резултат от фитнеса за различните поколения')

        plt.tight_layout()
        plt.show()


# 6. Инициализация на популацията
# Всеки индивид е позицията (x, y) на ЕДНО AP.
# Създаваме population_size * num_ap на брой позиции за индивиди.
initial_population = [(random.uniform(0, classroom_width), random.uniform(0, classroom_length)) for _ in range(population_size * num_ap)]
population = [initial_population.copy()]

# Променливи за проследяване
best_solution = None
best_fitness = float(-np.inf)
all_fitness_scores = []

# 7. Главен оптимизационен цикъл Генетичен алгоритъм:
for generation in range(generations):

    # Оценка на фитнеса на всеки индивид
    fitness_scores = []

    # Фитнесът на всяка позиция (ap_x, ap_y) се изчислява като сума от силата на сигнала
    # от тази точка до всяка дискретна точка (point_x, point_y) в стаята.
    for ap_x, ap_y in population[generation]:
        coverage = 0
        # Обхождане на всички дискретни точки в стаята (в метри)
        for point_x in range(classroom_width):
            for point_y in range(classroom_length):
                coverage += calculate_signal_strength(ap_x, ap_y, point_x, point_y)
        fitness_scores.append(coverage)

    # Актуализиране на най-доброто решение
    max_fitness_index = np.argmax(fitness_scores)
    current_max_fitness = fitness_scores[max_fitness_index]

    if current_max_fitness > best_fitness:
        best_solution = population[generation][max_fitness_index]
        best_fitness = current_max_fitness

    # Запазване на максималния фитнес резултат за текущото поколение
    all_fitness_scores.append(current_max_fitness)

    # Избор на родители
    selected_parents = random.choices(population[generation], weights=fitness_scores, k=len(population[generation]))

    # Създаване на потомство чрез кръстосване
    offspring = []

    for i in range(len(population[generation])):
        parent1, parent2 = random.sample(selected_parents, 2)

        # Кръстосване: Интермедиерен/Униформен кросоувър между координатите
        crossover_x = random.uniform(parent1[0], parent2[0])
        crossover_y = random.uniform(parent1[1], parent2[1])

        offspring.append((crossover_x, crossover_y))

    # Прилагане на мутация
    for i in range(len(offspring)):
        if random.random() < mutation_rate:
            # Мутация: Случайна нова позиция в рамките на залата
            offspring[i] = (random.uniform(0, classroom_width), random.uniform(0, classroom_length))

    # Замяна на старото население с ново поколение
    population.append(offspring)

    print(f"Поколение {generation + 1}/{generations}: Най-добър фитнес = {current_max_fitness:.4f}")

# === 8. Извеждане на резултатите в конзолата ===
print("\n=== Крайни Резултати ===")
print(f"Най-добро разпределение на точките за достъп: {best_solution}")
print(f"Най-добро покритие: {best_fitness}")

# === 9. Визуализации ===

# Началното и крайното разпределение на точките за достъп
# Използваме първите num_ap индивида от съответните популации
ap_initial_positions = initial_population[:num_ap]
ap_final_positions = population[-1][:num_ap]

visualize_initial_and_final(classroom_width, classroom_length, ap_initial_positions, ap_final_positions)

# Динамичните промени в разпределението и резултатите от фитнес през различните поколения
visualize_dynamic_changes(classroom_width, classroom_length, population, all_fitness_scores)

# Траекторията на популацията
trajectory_scores = []
for generation in range(generations + 1):
    # Изчисляване на средното разстояние от всеки индивид до най-доброто решение
    distances = [np.linalg.norm(np.array(point) - np.array(best_solution)) for point in population[generation]]
    trajectory_scores.append(np.mean(distances))

plt.figure(figsize=(10, 6))
plt.plot(range(generations + 1), trajectory_scores, marker='o')
plt.xlabel('Поколение')
plt.ylabel('Средно разстояние до най-доброто решение')
plt.title('Траектория на популацията')
plt.grid(True)
plt.show()

# Графика на сходство
plt.figure()
plt.plot(range(1, generations + 1), all_fitness_scores, marker='o')
plt.xlabel("Поколение")
plt.ylabel('Най-добър фитнес резултат')
plt.title('Графика на сходство')
plt.grid(True)
plt.show()