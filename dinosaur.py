import csv
dino={}
with open("dino1.csv") as dino1:
  csv_reader=csv.reader(dino1,delimiter=",")
  for row in csv_reader:
      # print(row)
      dino[row[0]]=""
      dino[row[0]]=[row[1],row[2]]

with open("dino2.csv") as dino2:
  csv_reader=csv.reader(dino2,delimiter=",")
  for row in csv_reader:
      # print(row)
      if row[0] in dino:
          dino[row[0]].append(row[1])
          dino[row[0]].append(row[2])
      else:
          dino[row[0]]=""
          dino[row[0]]=[row[1],row[2]]
for i,v in dino.items():
    if len(v)>2:
        print(f'{i} : {v}')
