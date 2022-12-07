with open('input.txt', encoding='utf-8') as inp:
    calories_list = inp.read()

calories = [x.split('\n') for x in calories_list.split('\n\n')]
most_calories = [0, 0]
elf_number = 0

for cal in calories:
    elfs_sum = 0
    for elfs_cal in cal:
        if(elfs_cal != ''):
            elfs_sum += int(elfs_cal)
    if elfs_sum > most_calories[1]:
        most_calories[0] = elf_number
        most_calories[1] = elfs_sum
    elf_number += 1

print(f"Elf number {most_calories[0]} carried the most calories - {most_calories[1]}")
