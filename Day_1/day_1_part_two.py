with open('input.txt', encoding='utf-8') as inp:
    calories_list = inp.read()

calories = [x.split('\n') for x in calories_list.split('\n\n')]
elfs_sums = []

for cal in calories:
    elfs_sum = 0
    for elfs_cal in cal:
        if(elfs_cal != ''):
            elfs_sum += int(elfs_cal)
    elfs_sums.append(elfs_sum)

elfs_sums.sort(reverse=True)
top3_total = sum(elfs_sums[0:3])

print(f"Sum of top 3 calories is: {top3_total}")

