import fileHandler


# type of sorting method, also output file name
SORT_TYPE = "merge"


# path to input file
filePath = "data.txt"
# path to output file
savePath = "{}.txt".format(SORT_TYPE)



def mergeSort(lst, p, r):
  q = (p + r) / 2

  a = lst[p: q]
  b = lst[q: r]
  print (a)
  print (b)


def merge(lst, p, q, r):
  return p


def main():
  # get contents of input file
  fileContent = fileHandler.parseFile(filePath)

  for lst in fileContent[0:1]:
    mergeSort(lst, 0, len(lst))


  # write sorted data to output file
  #fileHandler.writeFile(savePath, fileContent)



if __name__ == "__main__":
  print("{}{} Sort".format(SORT_TYPE[0].upper(), SORT_TYPE[1:]))
  main()

