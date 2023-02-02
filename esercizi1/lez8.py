
class Model():
    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')

    def predict(self,data):
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):

    def predict(self, data):
        prev_value = None
        # for i, item in enumerate(data):
        #      Logica per la predizione
        #     if i>0:
        #         diff=item-data[i-1]
        #         sum_diff=0
        #         sum_diff+=diff
                
        # prediction = sum_diff/i-1
        # return prediction
        sum_inc=0
        for i in range (len(data)-3, len(data)):
            incremento=data[i]-data[i-1]
            sum_inc+=incremento
        incr_medio=sum_inc/3
        prev_value=data[-1]+incr_medio
        return prev_value

class FitIncrementModel(IncrementModel):
    def fit(self,data):
        prev_value=None
        sum_inc=0
        for i in range(1, len(data)):
            incremento=data[i]-data[i-1]
            sum_inc+=incremento
        incr_medio=sum_inc/(len(data)-1)
        pred_IncrMod=self.predict(data)-data[-1]
        media=(incr_medio+pred_IncrMod)/2
        prev_value=media+data[-1]
        return prev_value
lista=[12,20,24,34,40,45,48,50,58,60]
obj=FitIncrementModel()
print(obj.predict(lista))
print(obj.fit(lista))


        