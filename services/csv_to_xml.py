import csv
import datetime

csvFile = input()
now = datetime.datetime.now()
xmlFile = 'myXML_' + now.strftime("%y-%m-%d") + '.xml'

csvData = csv.reader(open(csvFile))
xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0" encoding="utf-8" standalone="yes"?>' + "\n")
xmlData.write('<myTVA_data>' + "\n")

rowNum = 0
for row in csvData:
    if rowNum == 0:
        tags = row
        for i in range(len(tags)):
            tags[i] = tags[i].replace(' ', '')
    else:
        xmlData.write(' <Class>' + "\n")
        for i in range(len(tags)):
            row[i] = row[i].replace('&', '&amp;')
            row[i] = row[i].replace(';', ';'+"\n")
            row[i] = row[i].replace(' ', '_')
            row[i] = row[i].replace(',', '_')
            xmlData.write(' <' + str(tags[i]) + '>' + str(row[i]) + '</' + str(tags[i]) + '>' + '\n')
        xmlData.write('<Class>' + "\n")

    rowNum += 1

xmlData.write('</myTVA_data>' + "\n")
xmlData.close()