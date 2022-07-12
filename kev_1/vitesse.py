from distance import Distance

class Vitesse(Distance):
    def __init__ (self,n_d_f,debut:str = " 00:00:00",fin:str = " 23:59:59"):
        super().__init__(n_d_f,debut,fin)

    def Calcul_vitesse_moyenne(self) :
        
        def calcul_vitesse(dat):
            vites=[]
            for (index, row) in dat.iterrows():
                vites.append(row.loc['speed'])
            v2=[]
            for i in range(len(vites)) : 
                if vites[i]!=0 : 
                    v2.append(vites[i])
            
            if len(v2)>0:
                p=sum(v2)/len(v2)
                d=round(p, 2)
                return d
            else :
                v2=[0]
                p=sum(v2)/len(v2)
                d=round(p,2)   
                return d
        
        Data = super().Completer_le_dataset()
        #Vitesse_moyenne _jour
        gh=[]
        for i in range(0,len(Data[1]),1):
            gh.append(calcul_vitesse(Data[1][i]))
        Vitesse_jour = [ gh  , round(sum(gh)/len(gh),2) , Data[-2] ]
        
        #Vitesse_moyenne_semaine
        g=[]
        for i in range(0,len(Data[2]),1):
            g.append(calcul_vitesse(Data[2][i]))
        Vitesse_semaine = [ g , round(sum(g)/len(g),2) , Data[-1] ]
        
        return Vitesse_jour , Vitesse_semaine
