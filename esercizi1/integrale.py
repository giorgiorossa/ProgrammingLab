class Funzione():
    def eval (self,x): # funzione che restituisce f(x) pass 
        pass

    def calcola_integrale(self, a, b, M):
        h=(b-a)/M
        somma=0
        for i in range (0, M):
            x=a+i*h
            somma+=self.eval(x)
        integrale=h*somma
        return integrale

class F1(Funzione):
    def eval(self, x):
        return (x**3)

obj=F1()
print(obj.calcola_integrale(-1,1,1000000))
