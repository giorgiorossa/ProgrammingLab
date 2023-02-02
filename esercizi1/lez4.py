
class CSVfile ():
    def __init__(self, file_name):
        self.name=file_name
    def get_data(self):
        my_file=open(self.name, 'r')
        lista=[]
        c=0
        for line in my_file:
            line=line[:-1]
            if c!=0:
                elements=line.split(',')
                elements[-1]=float(elements[-1])
                lista.append(elements)
                #lista.append(elements[1])
                #del elements[0]
            c+=1
        my_file.close()
        return(lista)

        



obj=CSVfile('shampoo_sales.csv')
print(obj.name)
l=obj.get_data()
print(l)
