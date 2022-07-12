import pandas as pd
from vitesse import Vitesse

class Temps(Vitesse):
    def __init__ (self,n_d_f,debut:str = " 00:00:00",fin:str = " 23:59:59"):
        super().__init__(n_d_f,debut,fin)
        print(self.fin)
        print(self.debut)
        self.t_d_t = pd.to_datetime('2022'+" "+str(pd.to_datetime(self.fin[1:] ) - pd.to_datetime(self.debut[1:]))[7:])
        #t_d_t = temps de travail
        
        print(self.t_d_t)
        
    def Calcul_temps(self):
        
        def conv1(heure):
            h=int(heure)
            m=(heure%1)*60
            mi=int(m)
            s=int((m%1)*60)
            p=f'{h}:{mi}:{s}' 
            return p
        
        
        def conve1(heure):
            if int(heure) < 24:
                h=int(heure)
                m=(heure%1)*60
                mi=int(m)
                s=int((m%1)*60)
                p=f'{h}h{mi}m{s}s' 
                return p
            else :
                j=int((heure-heure%24)/24)
                x=heure%24
                h=int(x)
                m=(x%1)*60
                mi=int(m)
                s=int((m%1)*60)
                p=f'{j}j{h}h{mi}m{s}s' 
                return p
        
        def temps_mis(t):
            tp=[]
            for i in range(len(t)):
                tp.append(conv1(t[i])) #forma en :::
            tp1=[]
            for i in range(len(t)):
                tp1.append(conve1(t[i]))  #format texte hms
            fp=[]
            for i in range(len(tp)):
                fp.append('2022'+" "+tp[i])
            
            pp=pd.to_datetime(fp)
            return pp,tp1
        
        def division_d_v(V,D):
            Temps = []
            for i in range(0,len(V),1):
                if V[i] != 0 :
                    T = round(D[i]/V[i] , 2)
                else :
                    T = 0
                Temps.append(T)
            return Temps
            
        #Distance_1 = super().CalculDeDistanceParJour() # Tableau des distance par jour
        #print(Distance_1)
        Distance_2 = super().CalculDeDistanceParJour() # Tableau des distance par semaine
        
        #Vitesse_1 = super().Calcul_vitesse_moyenne()# Tableau des vitesse par jour
        #print(Vitesse_1)
        Vitesse_2 = super().Calcul_vitesse_moyenne() # Tableau des vitesse par jour
        
        #par jour 
        t=division_d_v(Vitesse_2[1][0],Distance_2[1][0] )
        print(t)
        X = temps_mis(t)
        immobile = []
        for i in range(0,len(X[0]),1):
            x = str(self.t_d_t-X[0][i])[7:]
            immobile.append(x)
        
        
        return immobile , Distance_2[1][-1] , self.n_d_f[5:-4]
        
#temps _immobile; période d'immobilité ; nom de la voiture

# PP == valeur de date traçable qui sera  utilise pour le graphe tu temps mis
# tp1 == la valeur en text du temps mis qui sera affiché sur le graphe
# t == valeur de la vitsse en nombre réel
# 














