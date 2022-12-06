from aocd import lines  # like data.splitlines()
import numpy
print(lines)
mygrid = numpy.full((8,9),'')
row = 0
for l in lines[0:8]:
    myline = l.split(' ')
    linelen = len(l)
    print(f'Line {myline} is {linelen}')
    for col in range(9):
        s = myline[col].strip('[]')
        mygrid[row][col] = s
    print(f'Grid line is {mygrid[row][:]}')

    row += 1
print(mygrid)


