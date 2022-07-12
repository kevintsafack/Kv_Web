import pandas as pd
from datetime import datetime
def conv(heure):
    h=int(heure)
    m=(heure%1)*60
    mi=int(m)
    s=int((m%1)*60)
    p=f'{h}:{mi}:{s}'
    p=pd.to_datetime(p)       
    return p

def conv1(heure):
    h=int(heure)
    m=(heure%1)*60
    mi=int(m)
    s=int((m%1)*60)
    p=f'{h}:{mi}:{s}' 
    return p


def conve1(heure):
    h=int(heure)
    m=(heure%1)*60
    mi=int(m)
    s=int((m%1)*60)
    p=f'{h}h{mi}m{s}s' 
    return p