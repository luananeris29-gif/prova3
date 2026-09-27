a = 15
b = 4
c = 2

res_1 = a / b - c ** b % a + a // b % 5
res_2 = not (c % a == 0) and (b * c + 2 > a or a - b * c != 7)

print(res_1)
print(res_2)