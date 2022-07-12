
from pyroutelib3 import Router

router = Router("car")
def route(data):
    d=[]
    for (index, row) in data.iterrows():
        d.append([row.loc['lat'], row.loc['lng']])
    f=[]
    for i in range(len(d)*2-2) :
        h=[]
        if i%2 == 0 :
            h.append(d[int(i/2)])
            h.append(d[int(i/2)+1])
            f.append(h)
    r=[]
    for i in range(0,409):
        depart = router.findNode(f[i][0][0], f[i][0][1])
        arrivee = router.findNode(f[i][1][0], f[i][1][1])
        status, route = router.doRoute(depart, arrivee)
        for j in range(len(route)) :
            r.append(route[j])
    return(r)





