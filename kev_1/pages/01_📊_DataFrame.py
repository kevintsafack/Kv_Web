


import sys
sys.path.append('C:/Users/TSAFACK_KevinHulric_/Desktop/kev/kev_1/')
from dataset import *
from Filtrage import *
from distance import *
#from dataset import DataSets
import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError
from streamlit_option_menu import option_menu
import time
st.set_page_config(page_title="DataFrame Demo", page_icon="📊")

################################################################♣
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
#############################################################
r = Uplaodss().uploid()
############################################################
selected = option_menu(
        menu_title=None,
        options = ["Insérez","project","Contact"],
        icons = ["file-earmark-arrow-down-fill","book","envelope"],
        orientation = "horizontal"
        
        )


if selected == "Insérez":
    st.title("Insérez votre fichier csv")
    if len(r[0])>0:
        st.success(str(len(r[1]))+" Fichiers ont été ajouté avec succes 👍")
    
    
if selected == "project":
    my_bar = st.progress(0)  
    try:
        for i in range(0,len(r[0])):
            time.sleep(0.00001)
            my_bar.progress(int((i+1)/len(r[0])*100))
            st.write("filename:", r[1][i])
            st.write(DataSets(r[0][i]).DataFrame())
    except:
        st.write("Wait")
    #st.write(len(Uplaods().uploid()))
    
        
    

if selected == "Contact":
    my_bar = st.progress(0)
    try:
        for i in range(0,len(r[0])):
            time.sleep(0.00001)
            my_bar.progress(int((i+1)/len(r[0])*100))
            st.write("filename:", r[1][i])
            st.write(Distance(r[0][i]).CalculDeDistanceParJour()[1])
    except:
        st.write("Wait")
        
#print(globals())