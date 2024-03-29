import timeit
import insertsort
import cleanup
import randomArray
import testLogger

testName = "Insert"
logName = "sort_tests.csv"

minVal = 0
maxVal = 10000
strtN = 3000
nIncr = 2000
tests = 10


tstLst = randomArray.lstOfLsts(minVal, maxVal, strtN, nIncr, tests)

results = []
i = 0
for tst in tstLst:
  n = len(tst)
  strt = timeit.default_timer()
  print("test: {}\nn: {}".format(i, n))
  insertsort.insertionSort( tst)

  end = timeit.default_timer()
  t = end - strt 
  print("t: {}\n".format(t) )

  
  result = [testName, n, t]
  results.append(result)

  i += 1

testLogger.addLogData(logName, results)

cleanup.pyc()





