from aocd import lines  # like data.splitlines()
from aocd import numbers  # uses regex pattern -?\d+ to extract integers from data

c = 0
row = []
elf_data = []
for l in lines:
    if l != '':
        row.append(int(l))
    else:
        elf_data.append(row)
        c += 1
        row = []
elf_sums = []
for rows in elf_data:
    elf_sum = 0
    for elem in rows:
        elf_sum += elem
    elf_sums.append(elf_sum)
print(max(elf_sums))
more_snacks = 0
for q in range(3):
    m = max(elf_sums)
    more_snacks += m
    elf_sums.remove(m)

print(more_snacks)
