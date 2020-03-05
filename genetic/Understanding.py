from random import choice
import time
import operator

t0 = time.perf_counter()  # считает время от самого раннего вызова perf_counter

evaluation = 0
evaluation += len(set([0, 0, 0])) * 1
print(evaluation)

gene_scores = {"bla": 3, "bol": 4, "bal": 0}   # словарь=  хромосома: ее счет фитнесс-функции
bla = {0: 3, 1: 4, 2: 0, 3: 6}
maxim = max(bla.items(), key=operator.itemgetter(1))[0]
print("max ", maxim)
sorted_genes = sorted(gene_scores, key=gene_scores.get)
print(type(sorted_genes))
best_n = sorted_genes[-1 * 1:]
print(best_n)
max_evaluation = -1 * float("Inf")
print(max_evaluation)
print(type(choice(range(4))))

colors_dict = {1: 2, 2: 1, 3: 7, 4: 5}
# получение ключа из той пары в словаре, значение у которой самое большое
print(min(colors_dict.items(), key=operator.itemgetter(1))[0])

# ------------------------------------------ #
print('/n')
sample_numbers = [0, 2, 1, 7, 7]
next_one = sorted(sample_numbers, reverse=True)[0] + 1
choice_from = list(set(sample_numbers))
choice_from.append(next_one)
print(choice_from)
sample_numbers.append(choice(choice_from))
print(sample_numbers)

no_points = 12
sample_numbers = [0]
for i in range(no_points - 1):
    next_one = sorted(sample_numbers, reverse=True)[0] + 1
    choice_from = list(set(sample_numbers))
    choice_from.append(next_one)
    sample_numbers.append(choice(choice_from))
print(sample_numbers)

print('/n')
new_arr = [0]
print(set(sample_numbers))
new_arr[0] = choice(list(set(sample_numbers)))
print(new_arr[0])
