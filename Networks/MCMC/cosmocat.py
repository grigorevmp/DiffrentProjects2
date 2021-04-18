import numpy

"""
Дано
"""

N = 9
MTTCA = 81
MTTBR = 4

alpha = 1 / MTTCA
beta = 1 / MTTBR
MTTPL = MTTCA / N

markov_chain = [[]]  # <- Тут будет цепь (Матрица переходов)

print()
print("Состояние 0:")
print("Остаться в состоянии 0:", 1 - N * alpha)
markov_chain[0].append(1 - N * alpha)
print("Перейти в состояние 1:", N * alpha)
markov_chain[0].append(N * alpha)
print("Перейти в состояние 2:", 0)
markov_chain[0].append(0)
print()
markov_chain.append([])
print("Состояние 1:")
print("Вернуться в состоянии 0:", beta)
markov_chain[1].append(beta)
print("Остаться в состояние 1:", 1 - beta - ((N - 1) * alpha))
markov_chain[1].append(1 - beta - (N - 1) * alpha)
print("Перейти в состояние 2:", (N - 1) * alpha)
markov_chain[1].append((N - 1) * alpha)
print()
markov_chain.append([])
print("Состояние 2:")
print("Вернуться в состоянии 0:", 0)
markov_chain[2].append(0)
print("Вернуться в состояние 1:", 0)
markov_chain[2].append(0)
print("Остаться в состояние 2:", 1)
markov_chain[2].append(1)

print()
print("Матрица переходов:", markov_chain)
print()

######################################

"""
Промоделируем цепь, сохраняя количество шагов до перехода во второе состояние
numpy.random.choice вернёт состояние в соответствии с вероятностью - будет задано строчкой матрицы переходов
"""


def next_state(state):
    return numpy.random.choice(numpy.arange(0, 3), p=markov_chain[state])


current_state = 0

living_times = []
iter_n = 0
while iter_n != 5000000:
    iter_n += 1
    current_state = 0
    time = 0
    while current_state != 2:
        current_state = next_state(current_state)
        time += 1
    living_times.append(time)
    if iter_n == 2500000:
        print("Don't kill me... 50% left")

print("MTTPL:", sum(living_times) / len(living_times))
print("Ideal MTTPL:", (MTTCA ** 2 + (2 * N - 1) * MTTCA * MTTBR) / (N * (N - 1) * MTTBR))  # см second.txt

######################################

# Добавим переход из 2го сотояния в 1ое

markov_chain[2][0] = markov_chain[1][0]
markov_chain[2][2] = 1 - markov_chain[2][0]

######################################

"""
Промоделируем цепь, сохраняя количество шагов и количество шагов во втором состоянии (downtime) 
Общее число - downtime = uptime
"""

iter_n = 0
current_state = 0
all_time = 0
downtime = 0

while iter_n != 10000000:
    iter_n += 1
    all_time += 1
    current_state = next_state(current_state)
    if current_state == 2:
        downtime += 1
    if iter_n == 3000000:
        print("Don't kill me... 70% left")
    if iter_n == 5000000:
        print("Don't kill me... 50% left")
    if iter_n == 7000000:
        print("Don't kill me... 30% left")

print("IA:", (all_time - downtime) / all_time)
