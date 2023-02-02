class ExamException(Exception):
    pass



class MovingAverage():

    def __init__(self, lunghezza):
        self.lunghezza=lunghezza
        
    def compute(self,data):    
        if not isinstance(self.lunghezza, int):
            raise ExamException('Valore della finestra non valido')
        if len(data)<self.lunghezza:
            raise ExamException('Lista troppo corta')
        try:
            lista_mediata=[]
            for i in range (self.lunghezza-1,len(data)):
                sum_elem=0
                for j in range(i-(self.lunghezza-1),i+1):
                    if not isinstance(data[j], int) and not isinstance(data[j],float):
                        raise ExamException('Valori non validi')
                    sum_elem+=data[j]
                media_mob_parziale=sum_elem/self.lunghezza
                lista_mediata.append(media_mob_parziale)
            return lista_mediata

        except:
            raise ExamException('Errore')
    
moving_average=MovingAverage(2)
result=moving_average.compute([2,4,'k',16])
print(result)