atoms = int(input())
final_atoms = int(input())
half_life_period = 0
while atoms > final_atoms:
    atoms /= 2
    half_life_period += 1
print(half_life_period * 12)
