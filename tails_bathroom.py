"""
 Расчет плитки для ванной, запас  + 10%
 Размеры в см:
             ширина х длина х высота
 дверь =     65 х х 205
 ванна =     70 х 170 х 55(+- 5)
 помещения = 175 х 155 х 245
"""

s_door = 205 * 65
s_full_bathroom = 2 * (175 + 155) * 245
s_bathroom = s_full_bathroom - s_door


s_tails = 20 * 44 
size_tail = input("Введите  размеры плитки (длина х ширина):")
print(size_tail)
l_tail, w_tail =map(int, size_tail.split('x'))
print(f"{l_tail + w_tail}")

if l_tail >= 0 and w_tail > 0:
    s_tails = l_tail * w_tail
    print(f"Площадь плитки {s_tails} см")

count_tail = round(s_bathroom / s_tails)
count_tail_backup = count_tail + (count_tail * 0.1)

print("Площадь ванны: {0} кв.см / ({1} кв.м)".format(s_bathroom, (round(s_bathroom / 100**2))))
print(f"Количество плиток {count_tail} шт.")
print(f"Количество плиток c запасом 10% {round(count_tail_backup)} шт.")







