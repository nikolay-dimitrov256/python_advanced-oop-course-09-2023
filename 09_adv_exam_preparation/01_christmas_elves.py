from collections import deque

elves_energies_queue = deque(int(num) for num in input().split())
materials_stack = [int(num) for num in input().split()]

total_toys = 0
energy_spent = 0
counter = 0

while elves_energies_queue and materials_stack:
    toys_created = 0
    elf_energy = elves_energies_queue.popleft()

    if elf_energy < 5:
        continue

    counter += 1
    material = materials_stack.pop()
    needed_energy = material

    if counter % 3 == 0:
        needed_energy *= 2

    if elf_energy >= needed_energy:
        toys_created = 1 if needed_energy == material else 2
        elf_energy -= needed_energy
        energy_spent += needed_energy
        elf_energy += 1
    else:
        materials_stack.append(material)
        elf_energy *= 2

    if counter % 5 == 0 and toys_created > 0:
        toys_created = 0
        elf_energy -= 1

    total_toys += toys_created
    elves_energies_queue.append(elf_energy)

print(f'Toys: {total_toys}')
print(f'Energy: {energy_spent}')
if elves_energies_queue:
    print('Elves left: ', end='')
    print(*elves_energies_queue, sep=', ')
if materials_stack:
    print('Boxes left: ', end='')
    print(*materials_stack, sep=', ')
