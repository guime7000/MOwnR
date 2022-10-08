import numpy as np

"""
Vectorised Rhumb line calculation. 

Returns destination point coordinates (Lat / Lon) at a certain distance D from a starting point (Lat/Lon coordinates) following a given azimuth

Gets : - inLat latitude (in DEGREES) of the starting point 
       - inLon longitude (in DEGREES) of the starting point
       - inDists : numpy array of distances (in METERS) from the starting point 
       - inAzimuths : numpy array of azimuths (in DEGREES) to follow from starting point

Returns : - a numpy array (n x 2) containing n rows of Lat / Lon destination coordinates

"""

def rhumbLines(inLat, inLon, inDists, inAzimuths):
    
    radInLat = np.deg2rad(inLat)
    radInLon = np.deg2rad(inLon)
    radInAzimuths = np.deg2rad(inAzimuths)

    earthRadius = 6_371_000 # meters
    delta = inDists /earthRadius
    deltaLat = delta * np.cos(radInAzimuths)

    smallQ = np.cos(radInLat)
    deltaLon = delta * np.sin(radInAzimuths) / smallQ

    outLat =  radInLat + deltaLat
    outLon = radInLon + deltaLon

    return np.array([np.rad2deg(outLat),np.rad2deg(outLon)]).T
