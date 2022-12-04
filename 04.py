from aocd import lines  # like data.splitlines()
def pairs_contain(elfa1,elfa2,elfb1,elfb2):
    arange = range(elfa1,elfa2+1)
    brange = range(elfb1,elfb2+1)
    if (elfb1 in arange and elfb2 in arange) or (elfa1 in brange and elfa2 in brange):
        return True
    else:
        return False
def any_overlap(elfa1,elfa2,elfb1,elfb2):
    doublework = False
    arange = range(elfa1,elfa2+1)
    brange = range(elfb1,elfb2+1)
    for a in arange:
        if a in brange:
            doublework = True
    for b in brange:
        if b in arange:
            doublework = True
    return(doublework)

double_count = 0
parttwo_count = 0
#print(lines)
for l in lines:
    ll = l.split("-")
    middle = ll[1].split(',')
    a1 = int(ll[0])
    a2 = int(middle[0])
    b1 = int(middle[1])
    b2 = int(ll[2])
    overlap = pairs_contain(a1,a2,b1,b2)
    parttwooverlap = any_overlap(a1,a2,b1,b2)
    print(f'in group {l},elves clean sections {a1} through {a2} and {b1} through {b2}.  Overlap is {overlap}.')
    if overlap:
        double_count+=1
    if parttwooverlap:
        parttwo_count += 1
print(double_count)
print(parttwo_count)