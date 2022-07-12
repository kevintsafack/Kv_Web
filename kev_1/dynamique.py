from vitesse import vt

import pandas as pd
from altair.expr import datum
import altair
import altair as alt
import numpy as np

def dyn(data):
    DS=[]
    for i in range(len(data[0])):
        ccc = pd.DataFrame({ 'vi':[], 'heure':[],'jr':[]})
        for j in range(len(data[6][i])):
            ccc.loc[j] = [data[6][i][j],data[7][i][j] ,data[8][i]]
        DS.append(ccc)

def dynn(data):
    DS=[]
    for i in range(len(data[0])):
        ccc = pd.DataFrame({ 'vi':[], 'heure':[],'jr':[]})
        for j in range(len(data[6][i])):
            ccc.loc[j] = [data[6][i][j],data[7][i][j] ,data[8][i]]
        DS.append(ccc)
    
    Tara = []
    for i in range(len(DS)):
        area1 = alt.Chart(DS[i]).mark_area(
            clip=True,
            interpolate='monotone',
            line={'color':'darkblue'},
            color=alt.Gradient(
                gradient='linear',
                stops=[alt.GradientStop(color='white', offset=0),
                       alt.GradientStop(color='darkblue', offset=1)],
                x1=1,
                x2=1,
                y1=1,
                y2=0
             )
    
        ).encode(
            alt.X('heure', scale=alt.Scale(zero=False, nice=False)),
            alt.Y('vi', scale=alt.Scale(domain=[0, 150]), title='vitesse en Km/h'),
            opacity=alt.value(1)
        ).properties(
            title='Comportement dinamyque du '+DS[i].jr[i],
            width=1000,
            #height=1000
        )#.interactive()
        
        #####
        lin_c = alt.Chart(DS[i]).mark_circle().encode(
            alt.X('heure', scale=alt.Scale(zero=False, nice=False)),
            alt.Y('vi',title=''),
            color=alt.value('#F5B041'),
            opacity=alt.value(5))
        ####    
        k=round(vt(DS[i].vi), 2)
        t_1 = 'Vitesse moyenne : ' + str(k)+' Km/H'
        t_2 = 'Vitesse limite_1 : 90 Km/H'
        t_3 = 'Vitesse limite_2 : 130 Km/H'
        k_m = pd.DataFrame({'k_m':[k],'v_l1':[90],'v_l2':[130],'v_l3':[0],'text1':t_1,'text2':t_2,'text3':t_3  })   
        ######################
        rule1 = alt.Chart(k_m).mark_rule(color='#18bc02').encode(
                y='k_m')
    
        rule2 = alt.Chart(k_m).mark_rule(color='#ff9e00').encode(
                y='v_l1')
    
        rule3 = alt.Chart(k_m).mark_rule(color=' #ff0000 ').encode(
                y='v_l2')
    
        rule4 = alt.Chart(k_m).mark_rule(color='#641E16').encode(
                y='v_l3')
    
        text1 = rule4.mark_text(
                align='left',
                baseline='middle', dy=65, color='#18bc02',size=12,
                dx=-500 
            ).encode(text='text1')
    
        text2 = rule4.mark_text(
                align='left',
                baseline='middle', dy=85, color='  #ff9e00  ',size=12,
                dx=-500 
            ).encode(text='text2')
    
        text3 = rule4.mark_text(
                align='left',
                baseline='middle', dy=105, color='  #ff0000  ',size=12,
                dx=-500 
            ).encode(text='text3')  
            ####################
        Tara.append((area1 + lin_c + rule1 + rule2 + rule3 + text1 + text2 + text3 ).properties(width=800,height=400))
        
    y1=[0]
    y1[0]=Tara[0]
    for i in range(1,len(Tara)):
        y1[0] =y1[0]&Tara[i]  
    
    return y1,Tara
    



















