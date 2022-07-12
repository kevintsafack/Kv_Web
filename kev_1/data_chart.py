import pandas as pd
from altair.expr import datum
import altair
import altair as alt
import numpy as np



def dataframe(data):
    c2 = pd.DataFrame({ 'Distance':[], 'Vitesse':[],'Temps_mis':[],'Temps_val':[],'D_val':[],'jour':[],'jr':[]})
    for i in range(len(data[0])):
        c2.loc[i] =  [data[0][i],data[1][i],data[2][i],data[3][i],data[4][i],data[5][i],data[8][i]]
    
    kk=[(round(np.mean(c2.Distance), 2)),(round(np.sum(c2.Distance), 2))]
    k='   distance moyenne : '+str(kk[0]) +' Km'
    k1='  distance totale : '+str(kk[1]) +' Km'
    tt=np.mean(c2.Temps_mis)
    t= '  Temps moyen : '+str(tt)[11:19]
    
    d_m = pd.DataFrame({'d_m':[kk[0]],'d_t':[kk[1]],'d_d':[0] ,'text':k,'text1':k1})
    
    t_m = pd.DataFrame({'t_m':[tt],'d_d':[0],'text':t})
    return c2,d_m,t_m

def chart(source):
    ######################
    rule1 = alt.Chart(source[-1]).mark_rule(color='#58D68D').encode(
        y='t_m'
    )
    
    rule10 = alt.Chart(source[-1]).mark_rule(color='#641E16').encode(
    y='d_d'
    )
    
    text11 = rule10.mark_text(
        align='left',
        baseline='middle', dy=70, color='#58D68D',size=12,
        dx=-400 
    ).encode(text='text')
    ####################

    ######################
    rule2 = alt.Chart(source[1]).mark_rule(color='#154360').encode(
        y='d_m'
    )
    
    rule23 = alt.Chart(source[1]).mark_rule(color='#154360').encode(
    y='d_d')


    text12 = rule23.mark_text(
        align='left',
        baseline='middle', dy=90, color='#154360',size=12,
        dx=-400
    ).encode(text='text')

    text123 = rule23.mark_text(
        align='left',
        baseline='middle', dy=110, color='#154360',size=12,
        dx=-400 
    ).encode(text='text1')
    ####################
    
    base = alt.Chart(source[0]).encode(alt.X('jr', title='Jours de la semaine'))
    
    line_A = base.mark_bar(color='#5276A7',size=10,cornerRadiusTopLeft=3,cornerRadiusTopRight=3).encode(
    alt.Y('Distance',axis=alt.Axis(titleColor='#5276A7'), title='Distance parcourue en Km'))
    
    line_B = base.mark_line(color='#F18727').encode(
    alt.Y('Temps_mis', axis=alt.Axis(titleColor='#F18727'), title='temps mis'))
    
    line_C = base.mark_circle(color='#a34d00').encode(alt.Y('Temps_mis',title=''),)
    
    dh= base.mark_area(
    clip=True,
    interpolate='monotone',
    line={'color':'darkorange'},
    color=alt.Gradient(
        gradient='linear',
        stops=[alt.GradientStop(color='white', offset=0),
               alt.GradientStop(color='darkorange', offset=1)],
        x1=1,
        x2=1,
        y1=1,
        y2=0)).encode(alt.Y('Temps_mis',title=''),opacity=alt.value(0.8))
    
    text = line_A.mark_text(
    align='center',
    baseline='middle', dy=-10, color='#154360',
    dx=0).encode(text='D_val')
    
    text1 = line_A.mark_text(
    align='center',baseline='middle', dy=-25, color='#a34d00',dx=-0).encode(text='Temps_val')
    
    
    return alt.layer((rule1 + dh + line_C  ), ( rule2 + line_A + text +  text11 + text12 + text123 + text1)).properties(width=800,height=400,
                                                            title='Temps d’activité avec kilométrage journalier du véhicule' )
    