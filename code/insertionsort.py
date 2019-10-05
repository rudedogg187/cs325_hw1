import fileHandler


# type of sorting method, also output file name
SORT_TYPE = "insert"


# path to input file
filePath = "data.txt"

# path to output file
savePath = "{}.txt".format(SORT_TYPE)



def insertionSort(lst):

  '''PSUDOCODE FROM TEXT'''
  #for j = 2 to A.length
  #  key = A[j]
  #  // Insert A[j] into the sorted sequence A[1..j-1].
  #  i = j - 1
  #  while i > 0 and A[i] > key
  #    A[i + 1] = A[i]
  #    i = i - 1
  #  A[i + 1] = key  

  for j in range(1, len(lst)):
    key = lst[j]
    i = j - 1

    while i >= 0 and int(lst[i]) > int(key):
      lst[i + 1] = lst[i]
      i -= 1

    lst[i + 1] = key



def main():
  # get contents of input file
  fileContent = fileHandler.parseFile(filePath)

  for lst in fileContent:
    insertionSort(lst)

  # write sorted data to output file
  fileHandler.writeFile(savePath, fileContent)



if __name__ == "__main__":
  print("{}{} Sort".format(SORT_TYPE[0].upper(), SORT_TYPE[1:]))
  main()

