from rich.text import Text
import linecompare as lc

class FileCompare:

  def __init__(self, file1, file2):
    self.file1 = file1
    self.file2 = file2

  # def split_line_at_three(self, line,startIndex,length):
  #   lineLeft = line[:startIndex]
  #   lineMid = line[startIndex:startIndex + length]
  #   lineRight = line[startIndex + length:]
  #   return lineLeft, lineMid, lineRight

  # def color_diff_for_line(self, line, startIndex, length, color): 
  #   lineLeft, lineMid,lineRight = self.split_line_at_three(line,startIndex, length)    
  #   line = ''.join([
  #       lineLeft, '[bold ',color,']', lineMid, '[/bold ',color,']',
  #       lineRight
  #   ])
  #   return line

  # def clean_line(self, line):
  #   line = ' '.join(line.split())
  #   line = line.replace('\n', '')
  #   return line
    
    
  # def lineCompare(self, lineNo, line1, line2):
  #   line1 = self.clean_line(line1)
  #   line2 = self.clean_line(line2)
    
  #   if line1 == line2:
  #     return line1, line2
  #   line1Ans=line1
  #   line2Ans=line2
    
  #   minLength = min(len(line1), len(line2))
  #   maxLength = max(len(line1), len(line2))
  #   diff = ''
  #   startIndex = -1
  #   for i in range(minLength):
  #     if line1[i] != line2[i]:
  #       diff = ''.join([diff, line2[i]])
  #       if startIndex==-1: 
  #         startIndex = i
  #     elif len(diff) > 0:
  #       print("diff in line " + str(lineNo) + " chars:" + diff)
  #       line1Ans= self.color_diff_for_line(line1,startIndex, len(diff),'magenta')
  #       line2Ans= self.color_diff_for_line(line2,startIndex, len(diff),'magenta')        
  #       diff = ''

  #   if minLength < maxLength and maxLength == len(line1):      
  #     line1Ans= self.color_diff_for_line(line1,minLength, maxLength,'magenta')      
  #   elif minLength < maxLength and maxLength == len(line2):        
  #     line2Ans= self.color_diff_for_line(line2,minLength,maxLength,'magenta') 

  #   return line1Ans, line2Ans

  def compare(self):
    minLength = min(len(self.file1), len(self.file2))
    lcO= lc.LineCompare()
    for i in range(minLength):
      self.file1[i], self.file2[i] = lcO.lineCompare(i, self.file1[i],
                                                      self.file2[i])

 
      
    # line1 = Text(line1,style="on red")
    # line2 = Text(line2,style="on blue")

  