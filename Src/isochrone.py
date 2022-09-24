import numpy as np


class Isochrone :

    def __init__(self,inId,inTs):
        self.id = inId
        self.ts = inTs 


    def get_boatInfos(self):
        pass

    def get_nbPoints(self):
        """
        returns the number of points of the isochrone forehead
        """
        pass

    def list_azimuths(self,inHdg,inSweptAngles,inSweptAnglesDelta):
        """
        computes a list of Azimuths for each point of the previous isochrone
        """
        pass

    def list_distances(self,inAzimuthList, inTwd, inTws, inDeltaT):
        """
        computes distance given a 
        """
        pass

    def reached_waypoint(self):
        pass

    def filterTWA(self):
        pass

    def clean_isochrone(self, leftNbPoints=200):
        """
        gets:
            (int) leftNbPoints : the number of left points of the isochrones forehead after cleaning
        
        selects valuable points 
        """
        pass

    def draw_isochrone(self):
        """
        Formats the points for folium Polyline draw
        """
        pass

    def compute_isochrone(self):
        pass
