import random

MIN_VAL = 0
MAX_VAL = 10000

START_N = 5
N_INCR = 5

TESTS = 10

def lstOfLsts(minVal, maxVal, strtN, nIncr, tests):
  lstLst = []
  lgth = strtN
  for test in range(0, tests):
    lst = []
    for i in range(0, lgth):
      rand = random.randrange(minVal, maxVal)
    
      lst.append(rand)

    lgth += nIncr
    lstLst.append(lst)
  return lstLst



def main():
  lstLst = lstOfLsts(MIN_VAL, MAX_VAL, START_N, N_INCR, TESTS)
  for lst in lstLst:
    print(lst)
    print('\n')


if __name__ == "__main__":
  main()



