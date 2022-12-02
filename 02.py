from aocd import lines  # like data.splitlines()
def part1(data):
  __import__('time').sleep(1)
  score1 = 0
  score2 = 0
  for l in lines:
      first = l[0]
      second = l[2]
      if first == "A":
          if second == "X":
              score1 += 1 + 3
              score2 += 3 + 0
          elif second == "Y":
              score1 += 2 + 6
              score2 += 1 + 3
          elif second == "Z":
              score1 += 3 + 0
              score2 += 2 + 6
      elif first == "B":
          if second == "X":
              score1 += 1 + 0
              score2 += 1 + 0
          elif second == "Y":
              score1 += 2 + 3
              score2 += 2 + 3
          elif second == "Z":
              score1 += 3 + 6
              score2 += 3 + 6
      elif first == "C":
          if second == "X":
              score1 += 1 + 6
              score2 += 2 + 0
          elif second == "Y":
              score1 += 2 + 0
              score2 += 3 + 3
          elif second == "Z":
              score1 += 3 + 3
              score2 += 1 + 6


  return(score1)

def part2(data):
  __import__('time').sleep(1)
  score1 = 0
  score2 = 0
  for l in lines:
      first = l[0]
      second = l[2]
      if first == "A":
          if second == "X":
              score1 += 1 + 3
              score2 += 3 + 0
          elif second == "Y":
              score1 += 2 + 6
              score2 += 1 + 3
          elif second == "Z":
              score1 += 3 + 0
              score2 += 2 + 6
      elif first == "B":
          if second == "X":
              score1 += 1 + 0
              score2 += 1 + 0
          elif second == "Y":
              score1 += 2 + 3
              score2 += 2 + 3
          elif second == "Z":
              score1 += 3 + 6
              score2 += 3 + 6
      elif first == "C":
          if second == "X":
              score1 += 1 + 6
              score2 += 2 + 0
          elif second == "Y":
              score1 += 2 + 0
              score2 += 3 + 3
          elif second == "Z":
              score1 += 3 + 3
              score2 += 1 + 6

  return(score2)


#print(lines)

