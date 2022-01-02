per_cent = {'ТБК': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
print(per_cent)
m = (per_cent.values())
print(m)
a = int(input("money:"))
print(a)
deposit = [x * (a/100) for x in m]
print(deposit)
print("Максимальная сумма, которую вы можете заработать - ", (max(deposit)))
