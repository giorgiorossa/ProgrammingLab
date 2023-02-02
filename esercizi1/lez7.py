from math import sqrt
class Funzione():
    def eval(self, x): # funzione che restituisce f(x)
        pass
    
    def calcola_integrale(self, a, b, M):
        h=(b-a)/M
        sum=0
        for i in range (0, M):
            x=a+(i*h)
            sum+=self.eval(x)
        integrale=h*sum
        return integrale

    def valore(self, x):
        return self.eval(x)
    
    def valore_assoluto(self, x):
        if x<0:
            x=-x
        return self.eval(x)

    def radice(self, x):
        x=sqrt(x)
        return self.eval(x)
            
class Funz(Funzione):
    def eval(self, x):
        return (x*((3**x)/((x**3)-4))) 
        #return (e**(2*x))
        #return (x/(1+x**2))
               

obj=Funz()
print(obj.calcola_integrale(-1, 4, 1000))
print(obj.valore(5))
print(obj.valore_assoluto(-5))
print(obj.radice(5))


