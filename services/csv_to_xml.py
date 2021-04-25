import csv
import datetime

csvFile = input()
now = datetime.datetime.now()
xmlFile = 'myXML_' + now.strftime("%y-%m-%d") + '.xml'

csvData = csv.reader(open(csvFile), delimiter = ';')
xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0" encoding="utf-8" standalone="yes"?>' + "\n")
xmlData.write('<' + csvFile + '>' + "\n")

iteration = 0
rowNum = 0
for row in csvData:
    if rowNum == 0:
        tags = row
        for i in range(len(tags)):
            tags[i] = tags[i].replace(' ', '')
    else:
        iteration += 1
        xmlData.write(' <Data' + str(iteration) + '>' + "\n")
        for i in range(len(tags)):
            row[i] = row[i].replace('&', '&amp;')
            row[i] = row[i].replace(';', ';'+"\n")
            row[i] = row[i].replace(' ', '_')
            xmlData.write(' <' + str(tags[i]) + '>' + str(row[i]) + '</' + str(tags[i]) + '>' + '\n')
        xmlData.write('</Data' + str(iteration) + '>' + "\n")

    rowNum += 1

xmlData.write('<' + csvFile + '>' + "\n")
xmlData.close()