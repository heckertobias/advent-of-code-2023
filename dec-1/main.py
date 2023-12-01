import regex as re

def trans(number):
  if number == "one":
    return "1"
  elif number == "two":
    return "2"
  elif number == "three":
    return "3"
  elif number == "four":
    return "4"
  elif number == "five":
    return "5"
  elif number == "six":
    return "6"
  elif number == "seven":
    return "7"
  elif number == "eight":
    return "8"
  elif number == "nine":
    return "9"
  else:
    return number

def main():
  path = "./input.txt"
  nums = list()

  with open(path, "r") as file:
    for line in file.readlines():
      print("\nReading Line:")
      print(line)

      digits = re.findall("[0-9]|one|two|three|four|five|six|seven|eight|nine", line, overlapped=True)
      print("Digits found:")
      print(digits)

      if len(digits) >= 2:
        nums.append(int(trans(digits[0]) + trans(digits[-1])))
      elif len(digits) == 1:
        nums.append(int(trans(digits[0]) + trans(digits[0])))
      else:
        nums.append(0)
      
      print("Num added to sum:")
      print(nums[-1])
  
  print("Final sum:")
  print(sum(nums))

if __name__ == "__main__":
  main()