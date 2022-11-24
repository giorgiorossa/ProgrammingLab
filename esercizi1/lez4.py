my_file=open('shampoo_sales.csv', 'r')

class CSVFile ():
    for line in my_file:
        elements = line.split(',')
        if elements[0] != 'Date\n':
            date=elements[0]
            value=elements[1]
    def get_data(self, date, value):
        def __init__(self, date, value):
            self.date = date
            self.value = value
        def __str__(self):
            return("{}, {}".format(self.date, self.value))
        