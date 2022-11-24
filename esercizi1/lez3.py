
def sum_csv(file):    
    somma=0
    for line in file:
        elements=line.split(',')
        if elements[0] != 'Date':
            valore=float(elements[1])
            somma=somma+valore
    return (somma)

my_file=open('shampoo_sales.csv', 'r')
pippo=sum_csv(my_file)
print('{}'.format(pippo))
