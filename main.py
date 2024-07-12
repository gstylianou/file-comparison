# import numpy as np
import sys

sys.path.insert(0, 'src')

from rich import print

from src import FileCompare, FileReader


def main():
  fr1 = FileReader('test-file1.txt')
  file1 = fr1.read()
  fr2 = FileReader('test-file2.txt')
  file2 = fr2.read()
  fc = FileCompare(file1, file2)
  fc.compare()
  print(file1)
  for i in range(len(file1)):
    print(file1[i])
  for i in range(len(file2)):
    print(file2[i])


main()

#todo
# diff when file1 has more lines than file2
# test other linecompare file
