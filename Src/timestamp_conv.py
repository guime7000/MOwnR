import time
from calendar import timegm

def tsConv(inTimestamp):
    """
    Transforms a inTimestamp to the floored tenth minute
    """
    hhmmss = time.gmtime(inTimestamp)
    modHHMMSS=[]
    for i,elem in enumerate(hhmmss):
        modHHMMSS.append(elem)
    modHHMMSS[4]=((modHHMMSS[4]-1)//10)*10

    return timegm(modHHMMSS)

