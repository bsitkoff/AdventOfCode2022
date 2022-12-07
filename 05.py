from aocd import lines  # like data.splitlines()
import numpy
#print(lines)
mygrid = []
for y in range(9):
    mygrid.append([])
for l in lines[0:8]:
  for col in range(9):
    #mygrid[row][col] = l[col*4 + 1]
    if l[col*4 + 1] != ' ':
        mygrid[col].append(l[col * 4 + 1])
print(mygrid)
rules = lines[10:len(lines)]

for r in rules:
    r = r.replace('move ','')
    r = r.replace('from ','')
    r = r.replace('to ', '')
    myr = r.split(' ')
    print(f'Used rule {myr} to move {myr[0]} items to {myr[2]} from {myr[1]} ')
    for i in range(len(myr)):
        myr[i] = int(myr[i])
    crane = []
    for h in range(myr[0]):
        crane.insert(0,mygrid[myr[1]-1].pop(0))
    for package in crane:
        mygrid[myr[2]-1].insert(0,package)
        #mygrid[myr[2]-1].insert(0,mygrid[myr[1]-1].pop(0))
    print(mygrid)
s = ''
for q in range(9):
    s+= mygrid[q][0]
print(s)


