# type of sorting method, also output file name
SORT_TYPE = "merge"

# read input file and parse it to pull out the arrays to be sorted
def parseFile(filePath):
  with open(filePath) as f:
    raw = f.readlines()

  ret = []
  for row in raw:
    lst = row.replace("\n", "").strip().split(" ")
    if len(lst) > 1:
      ret.append(lst[1:])

  return ret


# write the sorted arrays back to SORT_TYPE.txt
def writeFile(savePath, fileContent):
  raw = ""
  for row in fileContent:
    raw += " ".join(row) + "\n"

  with open(savePath, "w+") as f:
    f.write(raw)



# path to input file
filePath = "data.txt"
# path to output file
savePath = "{}.txt".format(SORT_TYPE)


def main():
  # get contents of input file
  fileContent = parseFile(filePath)
  # write sorted data to output file
  writeFile(savePath, fileContent)



if __name__ == "__main__":
  print("{}{} Sort".format(SORT_TYPE[0].upper(), SORT_TYPE[1:]))
  main()

