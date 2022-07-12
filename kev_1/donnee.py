from dataset import dataset as dt
from Filtrage import separate_day as sj
from distance import dist
from vitesse import Vitesse_moyenne as vitesse # calcul la vitesse moyenne
from vitesse import vi # on recupere les vitesses 
from vitesse import heure #on recupre les heures

from temps_mis import temps_mis as tm







def results(data) :
    #1) traitement du dataset
    g = dt(data)
    #1) traitement du dataset
    
    #2) séparation en jour distinct
    D=sj(g)
    print('les données sont traité sur ',len(D[0]),' jours')
    #2) séparation en jour distinct
    
    #3) calcul de la distance, et enregistrement dans un tableau
    jr = D[0]
    p = D[1]
    d = []
    
    for i in range(len(jr)) :
       d.append(dist(jr[i])) if len(jr[i]) >2 else d.append(0)
    
    f1=[]
    for i in range(len(d)):
        f1.append(str(d[i])+ ' Km')
    #3) calcul de la distance, et enregistrement dans un tableau
    
    #4) calcul de la Vitesse moyenne, et enregistrement dans un tableau
    
    V = []
    for i in range(len(jr)):
        V.append(vitesse(jr[i]))
    
    vl=[]
    for i in range(len(jr)):
        vl.append(vi(jr[i]))
    hr=[]
    for i in range(len(jr)):
        hr.append(heure(jr[i]))
    
    #4) calcul de la Vitesse moyenne, et enregistrement dans un tableau
    
    #5) calcul du temps moyen, et enregistrement dans un tableau
    
    t_m = []
    for i in range(len(jr)):
        if V[i]!=0:
            t_m.append(d[i]/V[i])
        else :
            t_m.append(0)
    
    #5) calcul du temps moyen, et enregistrement dans un tableau
    
    #6) convertion de ce temps en mode pandas, et enregistrement dans un tableau
    
    tem = tm(t_m)
    
    pp=[]
    for i in range(len(p)):
        pp.append(str(p[i]))
    p1=[]
    for i in range(len(p)):
        p1.append(pp[i][:10])
    
    return d,V,tem[0],tem[1],f1,p,vl,hr,p1,jr
    
    




