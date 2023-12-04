import sys

def readFileToLines(path):
  return open(path, "r").read().splitlines()

def calcPoints(matches):
  if matches == 0:
    return 0
  points = 1
  for i in range(matches - 1):
    points *= 2
  return points

def addCards(cardList: dict, cardNum: str, matches: int):
  print("Card " + cardNum)
  print(cardList)
  print(matches)


  cards = 1
  if cardNum in cardList:
    cards = cardList[cardNum] + 1
    cardList[cardNum] += 1
  else:
    cardList[cardNum] = 1

  if matches == 0:
    return cardList

  print(cards)

  for i in range(int(cardNum) + 1, int(cardNum) + matches + 1):
    if str(i) in cardList:
      print("Exists")
      print(1 * cards)
      cardList[str(i)] += (1 * cards)
    else:
      print("New")
      print(cards)
      cardList[str(i)] = 1 * cards
  
  print(cardList)
  print("-----------\n\n")
  return cardList

def main(filePath):
  lines = readFileToLines(filePath)

  allPoints = list()
  winningCards = dict()

  for line in lines:
    # 0 = card
    # 1 = winning numbers
    # 2 = numbers
    state = 0
    currNum = ""
    winNums = list()
    matches = 0
    card = ""
    for i in range(len(line)):
      char = line[i]

      if (char in ":| " and len(currNum) > 0) or i == len(line) - 1:
        if(i == len(line) - 1):
          currNum += char

        if state == 0:
          card = currNum
        elif state == 1:
          winNums.append(int(currNum))
        elif state == 2 and int(currNum) in winNums:
          matches += 1
        
        currNum = ""

      if char == ":":
        state = 1
      elif char == "|":
        state = 2
      elif char in "0123456789":
        currNum += char
    
    print(line)
    allPoints.append(calcPoints(matches))
    winningCards = addCards(winningCards, card, matches)
  
  print("Part 1:")
  print(sum(allPoints))

  print("\nPart 2:")
  print(winningCards)
  print(sum(winningCards.values()))

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Please specify the input file like 'python main.py input.txt'")
  else:
    main(sys.argv[1])