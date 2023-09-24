# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.


n_num = int(input("Введите кол-во эллементов первого множества: "))
n_array = set()
for i in range(n_num):
    n_array.add(input())
m_num = int(input("Введите кол-во эллементов второго множества: "))
m_array = set()
for i in range(m_num):
    m_array.add(input())
new_array = set()
for k in n_array:
    for j in m_array:
        if k == j:
            new_array.add(k)
print(n_array)
print(m_array)
print(sorted(new_array))
