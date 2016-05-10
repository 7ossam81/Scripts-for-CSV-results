# this script remove any row that has a "#NULL!"
import csv
with open('quiebras-spain-2005-clean.csv', 'r') as inp, open('first_edit6.csv', 'w',newline='\n') as out:
      writer = csv.writer(out)
      for row in csv.reader(inp):
          #if "#NULL!" not in row:
          if not any('#NULL!' in x for x in row):
              writer.writerow(row)

