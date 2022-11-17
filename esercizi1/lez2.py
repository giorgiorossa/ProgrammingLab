def sum_list(list):    
    somma=0
    for item in list:
        somma += item
    return(somma)

my_list=[3,15,-65,78]
risultato=None
if my_list==[]:
    print('{}'.format(risultato))
else:
    risultato=sum_list(my_list)
    print ('La somma è {}'.format(risultato))

    