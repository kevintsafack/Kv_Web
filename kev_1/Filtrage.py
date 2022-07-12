
from dataset import DataSets
from datetime import datetime
from datetime import date
import calendar
import pandas as pd

class Coupure(DataSets):
    def __init__ (self,n_d_f) :
        super().__init__(n_d_f)
    def DecoupeEnJour(self):
        F = []
        jour_graphe_abscisse = []
        for i in super().DataFrame().dt :
            F.append(str(i)[:10])
        for i in F :
            if F.count(i) > 1 :
                if jour_graphe_abscisse.count(i) == 0 :
                    jour_graphe_abscisse.append(i)
        jour_de_separation = pd.to_datetime(jour_graphe_abscisse) 
        return jour_graphe_abscisse , jour_de_separation



class SeparationEnJour(Coupure):
    def __init__ (self,n_d_f):
        super().__init__(n_d_f)
    def Separe(self):
        dataset_en_jour = [] 
        for i in super().DecoupeEnJour()[0] :
            dataset_en_jour.append( super().DataFrame().loc[i] )
        
        return dataset_en_jour

#Cette classe fait un découpage par jour avec le filtre
#don retourne directement un decoupage par jour filtré
class FiltreHoraire(SeparationEnJour):
    def __init__(self,n_d_f,debut:str = " 00:00:00",fin:str = " 23:59:59"):
        super().__init__(n_d_f)
        self.debut = debut
        self.fin = fin
    def Filtre_Horeiare(self):
        dataset_en_jour_filtre = []
        dataset_par_jour = super().Separe()
        Decoupe_joure = super().DecoupeEnJour()[0]
        for i in range(0 , len(dataset_par_jour) , 1) :
            dataset_en_jour_filtre.append( dataset_par_jour[i].loc[Decoupe_joure[i]+self.debut : Decoupe_joure[i]+self.fin] )
        return dataset_en_jour_filtre

class ReconstructionDuDataset(FiltreHoraire) :
    def __init__ (self,n_d_f,debut:str = " 00:00:00",fin:str = " 23:59:59"):
        super().__init__(n_d_f,debut,fin)
    def ReconstrureLeDataset(self):
        E = super().Filtre_Horeiare()
        dataset_construit = E[0]
        for i in range(1,len(E),1):
            dataset_construit = pd.concat( [dataset_construit,E[i]] ,axis=0 )
        return dataset_construit
        

      
class SeparationEnSemain(ReconstructionDuDataset):
    def __init__ (self,n_d_f,debut:str = " 00:00:00",fin:str = " 23:59:59"):
        super().__init__(n_d_f,debut,fin)
        self.obj = calendar.Calendar() #creation d'un calendrier
        self.Clendrier_par_an = []
        for j in range(2021 , 2026 , 1) :
            self.SD = []
             #cette liste contient une liste de calendrier 
            for i in range(1,13,1) :
                self.SD.append(self.obj.monthdatescalendar(j, i)) #calendrier
            self.Clendrier_par_an.append(self.SD)
            self.Tableau_de_semaine = []
            for z in range(0,len(self.Clendrier_par_an),1):
                for i in range(0,12,1) :
                    for j in range(0,len(self.Clendrier_par_an[z][i]),1):
                        self.Tableau_de_semaine.append(self.Clendrier_par_an[z][i][j])
        
    def Separation_en_semaine(self):
        Dataset_par_semaine = []
        les_jours_semaine = []
        x = self.Tableau_de_semaine
        Dataset_construit = super().ReconstrureLeDataset()
        for i in range(0,len(x),1) :
            try:
                if len(Dataset_construit.loc[ str(x[i][0]) : str(x[i][-1]) ])>1:
                    Dataset_par_semaine.append( Dataset_construit.loc[ str(x[i][0]) : str(x[i][-1]) ] )
                    les_jours_semaine.append(x[i]) 
            except:
                continue
       
        dataset_semaine =[Dataset_par_semaine[0]] #FG
        for i in range(1,len(Dataset_par_semaine),1):
            if dataset_semaine[-1].index[0] != Dataset_par_semaine[i].index[0] :
                dataset_semaine.append(Dataset_par_semaine[i])
           
        
   
        
        Liste_semaine = [les_jours_semaine[0]] #TG
        liste_des_jour = [] # la liste des jors de la semaine TG_1
        
        for i in range(0,len(les_jours_semaine),1):
            
            if Liste_semaine[-1][0] != les_jours_semaine[i][0] :
                Liste_semaine.append(les_jours_semaine[i])
            
        
        
        for i in range (0, len(Liste_semaine),1):
            liste_des_jour = liste_des_jour + Liste_semaine[i]
        
        liste_des_sem = []
        for i in range(0,len(Liste_semaine),1):
            liste_des_sem.append( "Du " + str(Liste_semaine[i][0]) + " au " +  str(Liste_semaine[i][-1]) )
        
        return dataset_semaine , liste_des_jour , liste_des_sem ,Liste_semaine

class Completer(SeparationEnSemain) :
    def __init__ (self,n_d_f,debut:str = " 00:00:00",fin:str = " 23:59:59"):
        super().__init__(n_d_f,debut,fin)
        
    def Completer_le_dataset(self):
        #Fonction progrssive : elle remplie le dataset du haut vers le bas
        def Progressive(SA,TR:str):
            data = pd.DataFrame({'lat':[],'lng':[],'altitude':[],
                                 'angle':[],'speed':[],'dt':[]})
            data.loc[0]=[SA.lat[-1],SA.lng[-1],SA.altitude[-1],SA.angle[-1],SA.speed[-1],TR]
            data.dt = pd.to_datetime(data.dt)
            dte = data.dt
            data = data.rename(columns={'dt':'dte', 'lat':'lat', 'lng':'lng', 'altitude':'altitude',
                                            'angle':'angle', 'speed':"speed"})
            data = pd.concat( [data,dte] , axis=1 )
            data=data.set_index('dte')
            return data
        
           
        FG_1 = super().ReconstrureLeDataset() # Donnele dataset reconstruit avec les jours filtrées
        FG = super().Separation_en_semaine()[1] # Liste des jours de la semaine
        X = [] # liste des jour de la semaine en chaine de caractère
        for i in range(0,len(FG),1):
            X.append(str(FG[i]))
        
        # on doit recupér la liste ds jour du dataset dans une variable X_1
        X_1 = super().DecoupeEnJour()[0]
        
        dataset_complet = []
        if X[0] == X_1[0] :
            dataset_complet = FG_1.loc[X[0]]
        else :
            dataset_complet = Progressive(FG_1.loc[X_1[0]],X[0])
        
        
        FG_1 = pd.concat([dataset_complet,FG_1],axis = 0)
        FG_1_1  = []
        
        if X[-1] == X_1[-1]:
            FG_1_1 = FG_1 
        else:
            FG_1 = pd.concat([ FG_1,Progressive(FG_1.loc[X_1[-1]],X[-1])],axis = 0)
            FG_1_1 = FG_1 
        
        
        j = 0
        for i in X:
            a = j+1
            
            if len(FG_1_1.loc[i]) > 0 :
                
                dataset_complet = pd.concat( [dataset_complet,FG_1_1.loc[i]] ,axis=0 )
                
            else :
                
                po = Progressive(FG_1_1.loc[X[a-1]],i)
                dataset_complet = pd.concat( [dataset_complet ,  po  ] ,axis=0 )
        
        dataset_par_jour_complet = []
        for i in X :
            dataset_par_jour_complet.append(dataset_complet.loc[i])
        
        
        data_semaine = super().Separation_en_semaine()[0]
        l_semaine = super().Separation_en_semaine()[2]
        return dataset_complet  , dataset_par_jour_complet, data_semaine ,X, l_semaine














