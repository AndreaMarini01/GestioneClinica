import os
import pickle


class CartellaClinica:


    def __init__(self, id):
        self.id=id
        self.patologie=[]

    def setPatologie(self, patologia):
        self.patologie.append(patologia)

    def setId(self,id):
        self.id=id

    def getId(self):
        return self.id

    def stampaCartella(self):
        with open ('dati/CC/cartella'+str(self.id)+'.pickle' , 'wb+') as f:
            pickle.dump(self.patologie,f,pickle.HIGHEST_PROTOCOL)

    def leggiCartella(self):
        if os.path.isfile('dati/CC/cartella'+str(self.id)+'.pickle'):
            with open('dati/CC/cartella'+str(self.id)+'.pickle', 'rb') as f:
                return 'patologie: \n'+str(pickle.load(f))
        else:
            return False