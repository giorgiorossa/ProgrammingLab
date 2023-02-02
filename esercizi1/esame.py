class ExamException(Exception):
    pass


class CSVTimeSeriesFile():

    def __init__(self, name):
        if not isinstance(name, str):
            raise ExamException('Errore, il nome non è di tipo stringa')
        self.name = name

    def get_data(self):
        try:
            open_file = open('data.csv', 'r')
        except:
            raise ExamException('Errore, il file non è leggibile')

        
            n_lista = 0
            lista_dati = []
            elements_0_precedente = None
            for line in open_file:
                try:
                    if n_lista != 0:
                        elements = line.split(',')
                        elements[0] = int(float(elements[0]))
                        elements[1] = float(elements[1])
                        lista_line = []
                        lista_line.append(elements[0])
                        lista_line.append(elements[1])
                        lista_dati.append(lista_line)
                        if n_lista > 1:
                            if elements[0] <= elements_0_precedente:
                                raise ExamException('Timestamp fuori ordine')
                        elements_0_precedente = elements[0]
                    n_lista += 1
                except:
                    pass
        if len(lista_dati) == 0:
            raise ExamException('Errore, la lista valori è vuota')

        return lista_dati


def compute_daily_max_difference(time_series):
    try:
        lista_escursioni = []
        yesterday_start_epoch = None
        temp_max = None
        temp_min = None
        escursione = None
        for line in time_series:
            day_start_epoch = line[0] - (line[0] % 86400)

            if day_start_epoch != yesterday_start_epoch:
                temp_max = line[1]
                temp_min = line[1]
                lista_escursioni.append(None)
            else:
                if line[1] > temp_max:
                    temp_max = line[1]
                if line[1] < temp_min:
                    temp_min = line[1]
                lista_escursioni.pop(-1)
                escursione = temp_max - temp_min
                lista_escursioni.append(escursione)

            yesterday_start_epoch = day_start_epoch

        return lista_escursioni
    except:
        raise ExamException('Errore')


time_series_file = CSVTimeSeriesFile('data.csv')
time_series = time_series_file.get_data()
print(compute_daily_max_difference(time_series))