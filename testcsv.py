import csv

with open('test.csv') as file:
    dulieu = list(csv.reader(file))

print(dulieu)
# print (len(dulieu) - 1, len(dulieu[0]))
 
