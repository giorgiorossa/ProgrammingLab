class Studente:
# attributo uguale per tutti
    ruolo = "Studente UNITS"
# costruttore, per ogni studente,
# che permette di creare un oggetto
# della classe, con opportuni valori per
# eventuali variabili di istanza dell'oggetto Studente
    def __init__(self, nome, cognome):
        self.nome = nome                
        self.cognome = cognome
    def bonjour(self):
        print(self.ruolo, ":", self.nome,         self.cognome)
obj_Giulio = Studente("Giulio", "Caravagna")
obj_Giulio.bonjour()
# accedo al campo nome (come nelle struct in C)
print("Campo nome di Giulio", obj_Giulio.nome)
obj_Giulio.nome = "Giuliano" # cambio nome
print("Campo nome di Giulio", obj_Giulio.nome)
obj_Giulio.ruolo = "Bidello" # cambio ruolo
obj_Giulio.bonjour()