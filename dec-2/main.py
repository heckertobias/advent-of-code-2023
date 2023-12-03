import re

def paseLine(line):
  initDraw = {"red": 0, "green": 0, "blue": 0}
  gameNum = -1
  draws = list()
  draw = dict(initDraw)

  matches = re.finditer(r'\s([0-9]*):|([0-9]*)\s(red|green|blue)|(;)', line)
  for match in matches:
    groups = match.groups()

    if groups[0] != None:
      gameNum = int(groups[0])
    elif groups[1] != None and groups[2] != None:
      draw[groups[2]] = int(groups[1])
    elif groups[3] == ";":
      draws.append(draw)
      draw = dict(initDraw)
  
  draws.append(draw)
  return {"id": gameNum, "draws": draws}


def main():
  path = "./input.txt"
  lines = open(path, "r").readlines()

  maxValue = {"red": 12, "green": 13, "blue": 14}
  ids = list()
  powersOfGames = list()

  for line in lines:
    game = paseLine(line)
    print(game)
    maxRed = 0
    maxGreen = 0
    maxBlue = 0
    for draw in game["draws"]:
      maxRed = max(maxRed, draw["red"])
      maxGreen = max(maxGreen, draw["green"])
      maxBlue = max(maxBlue, draw["blue"])
    
    powersOfGames.append(maxRed * maxGreen * maxBlue)

    if maxRed > maxValue["red"] or maxGreen > maxValue["green"] or maxBlue > maxValue["blue"]:
      continue

    ids.append(game["id"])

  print("\nPart 1:")
  print(sum(ids))
  print("\nPart 2:")
  print(sum(powersOfGames))

if __name__ == "__main__":
  main()