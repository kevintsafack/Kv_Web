a=[]
for k in range(0,2050,1) : 
     m = [] 
     for j in range(0,13,1) : 
         t = []
         for i in range(0,32,1) :
             t.append(f'{k}-{j}-{i}')
         m.append(t)
     a.append(m)

class Date:
    def __init__(self,annee_debut,annee_fin):
        self.annee_debut = annee_debut
        self.annee_fin = annee_fin
    def Constrution_De_Date (self):
        a=[]
        for k in range(self.annee_debut,self.annee_fin,1) :
            m = []
            for j in range(0,13,1) :
                t = []
                for i in range(0,32,1) :
                    t.append(f'{k}-{j}-{i}')
                m.append(t)
            a.append(m)
            
D = Date(2010,2013)
P=D.Constrution_De_Date()