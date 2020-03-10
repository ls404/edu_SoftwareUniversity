mine_yield = int(input())
days_counter = 0
total_materials = 0

while mine_yield >= 100:
    days_counter += 1
    total_materials += mine_yield
    if total_materials >= 26:
        total_materials -= 26
    else:
        total_materials -= total_materials
    mine_yield -= 10


if total_materials >= 26:
    total_materials -= 26
else:
    total_materials -= total_materials

print(days_counter)
print(total_materials)