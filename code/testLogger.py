import csv
import os

LOG_FILE = "test_log.csv"
cwd = os.getcwd()
dirlst = os.listdir(cwd)



def doesLogExist(logFile):
  for f in dirlst:
    if f == logFile:
      return True

  return False


def makeNewLog(logFile):
  with open(logFile, "w+") as f:
    csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(["method", "n", "t"])


def addLogData(logFile, data):
  if doesLogExist(logFile) == False:
    makeNewLog(logFile)

  with open(logFile, "a+") as f:
    csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    for row in data:
      csv_writer.writerow(row)
  
def addLogDatum(logFile, datum):
  if doesLogExist(logFile) == False:
    makeNewLog(logFile)

  addLogData(logFile, [datum])

  


def main():  
  addLogData(LOG_FILE, [["merge", 10, 8, "10-10-10"], ["sort", 88, 9, "20-20-10"]])


if __name__ == "__main__":
  main()


