import csv
from io import StringIO
text = "name,score\nAlice,95\nBob,88\n"
for row in csv.DictReader(StringIO(text)): print(row)