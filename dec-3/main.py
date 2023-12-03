import sys

def readFileToLines(path):
  return open(path, "r").read().splitlines()

def lookaroud(map, posX, posY):
  startX = max(0, posX - 1)
  startY = max(0, posY - 1)
  endX = min(len(map[0]) - 1, posX + 1)
  endY = min(len(map) - 1, posY + 1)

  for y in range(startY, endY + 1):
    for x in range(startX, endX + 1):
      if map[y][x] not in "0123456789.":
        return (map[y][x], x, y)
  
  return ("", -1, -1)

def addToGear(gears, num, x, y):
  newGears = list()
  added = False

  for gear in gears:
    if gear[0] == x and gear[1] == y:
      gear[2].append(num)
      added = True
    newGears.append((gear[0], gear[1], gear[2]))
  if not added:
    nums = list()
    nums.append(num)
    newGears.append((x, y, nums))
  return newGears

def calcGear(gear):
  if len(gear[2]) == 2:
    return gear[2][0] * gear[2][1]
  return 0

def main(inputfile):
  input = readFileToLines(inputfile)
  currNumStr = ""
  withSymbol = False
  withStar = (-1, -1)
  partNums = list()
  gears = list()
  gearRatios = list()
  
  for y in range(len(input)):
    for x in range(len(input[y])):
      char = input[y][x]
      if char in "0123456789":
        currNumStr += char
        symbol = lookaroud(input, x, y)
        withSymbol |= len(symbol[0]) != 0
        if symbol[0] == "*":
          withStar = (symbol[1], symbol[2])
      else:
        if withSymbol:
          partNums.append(int(currNumStr))
          if withStar[0] != -1 and withStar[1] != -1:
            gears = addToGear(gears, int(currNumStr), withStar[0], withStar[1])
        withStar = (-1, -1)
        currNumStr = ""
        withSymbol = False
        
    
    if withSymbol:
      partNums.append(int(currNumStr))
      if withStar[0] != -1 and withStar[1] != -1:
        gears = addToGear(gears, int(currNumStr), withStar[0], withStar[1])
    currNumStr = ""
    withSymbol = False

  for gear in gears:
    gearRatios.append(calcGear(gear))
  
  print("\nPart 1:")
  print(sum(partNums))

  print("\nPart 2:")
  print(sum(gearRatios))

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Please specify the input file like 'python main.py input.txt'")
  else:
    main(sys.argv[1])