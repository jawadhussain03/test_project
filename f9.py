import csv


class CSVutils:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def get_header(self):
        r1 = open(self.csv, 'r')
        global reader1 = csv.reader(r1)
        global header1 = reader1.next()
        return header1

     def add_header(self):
         data = list(reader1)

