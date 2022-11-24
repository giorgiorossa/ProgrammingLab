
def sum_csv(file):    
    somma=0
    for line in file:
        elements=line.split(',')
        if elements[0] != 'Date':
            valore=float(elements[1])
            somma=somma+valore
    return (somma)


