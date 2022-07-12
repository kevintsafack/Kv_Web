#calcul des distance parcourue

from Filtrage import Completer

from pyroutelib3 import Router #utilisé pour le calcul des distance
router = Router("car")

class Distance(Completer) :
    def __init__ (self,n_d_f,debut:str = " 00:00:00",fin:str = " 23:59:59"):
        super().__init__(n_d_f,debut,fin)
        
        self.Distance_total = []
    def CalculDeDistanceParJour(self) :
        
        def calcul(data):
            distance_par_jour = 0
            Itineraire = []
            if len(data) > 1:
                for (index , row) in data.iterrows() :
                    Itineraire.append([row.loc['lat'] , row.loc['lng']]) #matrice de la distance
        
                L = len(Itineraire)
                distance_point_par_point = [] # Tableau de distance point par point(continue)
                distance_cummulé_progrssive = [] # initialisation de la distance cumulée
        
                for i in range(1, L):
                    distance_point_par_point.append(router.distance(Itineraire[i-1],Itineraire[i]))#liste des distances entre deux points
                    distance_cummulé_progrssive.append(sum(distance_point_par_point))#liste des distances cumulées
                distance_par_jour = round(distance_cummulé_progrssive[-1], 2)
            else :
                distance_par_jour = 0
            return distance_par_jour
        
        Data = super().Completer_le_dataset()
        #Par jour
        gh=[]
        for i in range(0,len(Data[1]),1):
            gh.append(calcul(Data[1][i]))
        Distance_jour = [ gh , round(sum(gh),2) , round(sum(gh)/len(gh),2) , Data[-2] ]
        
        #Par semaine
        g=[]
        for i in range(0,len(Data[2]),1):
            g.append(calcul(Data[2][i]))
        distance_semaine = [ g , round(sum(g),2) , round(sum(g)/len(g),2) , Data[-1] ]
        
        return Distance_jour , distance_semaine
# distance totale par jour, somme sur la période , moyene sur la période
    





