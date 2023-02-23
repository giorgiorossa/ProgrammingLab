class ExamException(Exception):
    pass

class CSVTimeSeriesFile():

    def __init__(self, name):
        if not isinstance(name, str):
            raise ExamException('Errore, il nome non è di tipo stringa')
        self.name = name

    def get_data(self):
        try:
            open_file = open(self.name, 'r')
        except:
            raise ExamException('Errore, il file non è leggibile')

        n_lista=0
        anno_scorso=None
        mese_scorso=None
        lista_dati=[]
        for line in open_file:
            try:
                if n_lista != 0:
                    elements = line.split(',')
                    elements[1] = int(elements[1])
                    lista_line = []
                    lista_line.append(elements[0])
                    lista_line.append(elements[1]) 
                    lista_dati.append(lista_line)
                n_lista+=1
        
            except:
                pass
        # print(lista_dati)
        count=0
        for line in lista_dati:
            anno_mese=line[0].split('-')
            anno=anno_mese[0]
            mese=anno_mese[1]
            mese=int(mese)
            anno=int(anno)    
            # print(mese,mese_scorso)
            if count>0:
                    if anno<anno_scorso:
                            raise ExamException('Timestamp fuori ordine')
                    else:
                        if anno==anno_scorso:
                            # print(anno)
                            if mese<mese_scorso or mese==mese_scorso:
                                # print(mese,mese_scorso)
                                raise ExamException('Timestamp fuori ordine')
            mese_scorso=mese
            anno_scorso=anno
            count+=1
            
        if len(lista_dati) == 0:
            raise ExamException('Errore, la lista valori è vuota')

        
        
        return lista_dati


years=[1959, 1960]


def detect_similar_monthly_variations(time_series, years):
    try:
        mese=None
        passeggeri=None
        mese_scorso=None
        passeggeri_mese_scorso=None
        monthly_variation=None
        monthly_variation_2=None
        lista_monthly_variations=[]
        lista_monthly_variations_2=[]
        n_line=0
        m_line=0
        differenza_mesi=None
        lista_coppie_simili=[]
        years[0]=int(years[0])
        years[1]=int(years[1])
        if years[1]==years[0]+1:
        
            for line in time_series:
                
                line[1]=int(line[1])
                elements=line[0].split('-')
                elements[0]=int(elements[0])
                elements[1]=int(elements[1])
                if elements[0]==years[0]:
                    mese=elements[1]
                    passeggeri=line[1]
                    if m_line>0:
                        differenza_mesi=mese-mese_scorso
                        if differenza_mesi>1:
                            for i in range(0,(differenza_mesi)):
                                lista_monthly_variations.append(None)
                        else:
                            monthly_variation=passeggeri-passeggeri_mese_scorso
                            lista_monthly_variations.append(monthly_variation)
                    mese_scorso=mese
                    passeggeri_mese_scorso=passeggeri
                    m_line+=1
                
            
            for line in time_series:
                line[1]=int(line[1])
                elements=line[0].split('-')
                elements[0]=int(elements[0])
                elements[1]=int(elements[1])
                if elements[0]==years[1]:
                    mese=elements[1]
                    passeggeri=line[1]
                    if n_line>0:
                        differenza_mesi=mese-mese_scorso
                        if differenza_mesi>1:
                            for i in range(0,(differenza_mesi)):
                                lista_monthly_variations_2.append(None)
                        else:
                            monthly_variation_2=passeggeri-passeggeri_mese_scorso
                            lista_monthly_variations_2.append(monthly_variation_2)
                    mese_scorso=mese
                    passeggeri_mese_scorso=passeggeri
                    n_line+=1
            for i in range(0, len(lista_monthly_variations)):
                if lista_monthly_variations[i]==None or lista_monthly_variations_2[i]==None:
                    lista_coppie_simili.append(False)
                else:
                    if lista_monthly_variations[i]-lista_monthly_variations_2[i]<-2 or lista_monthly_variations[i]-lista_monthly_variations_2[i]>2:
                        lista_coppie_simili.append(True)
                    else:
                        lista_coppie_simili.append(False)
        else:
            raise Exception('Anni non consecutivi')
          
        
        
        return lista_coppie_simili                            

    except:
        raise Exception('Errore')
    



time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
print(detect_similar_monthly_variations(time_series, years))