import csv

o = "fullcsv.csv"
files = ['mnist_train.csv','mnist_test.csv']

with open(o, 'w', newline='') as csvfile:
    i = 0
    writer = csv.writer(csvfile, delimiter=',')
    while i < len(files):
        readCSV = csv.reader(open(files[i]), delimiter=',')
        for row in readCSV:
            writer.writerow(row)

        i+=1


print("done")
