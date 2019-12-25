import csv
class Revert(object):

    def Reup(self):
        
        new_rows = []
        
        with open('jen.csv', 'r') as csvfile:
            for row in csv.reader(csvfile):
                row = [int(val) for val in row]
                row.append(sum(row))
                new_rows.append(row)
        
        with open('file.csv', 'w') as csvfile:
            csv.writer(csvfile).writerows(new_rows)
            print (row)