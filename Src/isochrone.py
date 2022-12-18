import numpy as np


class Isochrone :
    """
    A class implementing Isochrone object.

    
    """

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

    def list_azimuths(self,inHdg,inSweptAngle,inSweptAngleDelta):
        """
        Generates a numpy array containing all desired azimuths for destination calculation for each point of the previous isochrone

        Gets : 
            - inHdg, the actual heading of the boat in degrees
            - inSweptangle, the value of the angle aperture
            - inSweptAngleDelta, is the step value, in degrees, to sweep the inSweptAngle angle aperture.

        Returns :
            - a numpy array containing (inSweptANgle / inSweptAngleDelta) points

        Example : With inHdg = 150, inSweptAngle = 200 and inSweptAngleDelta = 1, we'll get a numpy array containing
        1° step values from 50° to 249°
        """
        return (np.arange(-inSweptAngle/2,inSweptAngle/2,inSweptAngleDelta) + inHdg) % 360

    def list_distances(self,inAzimuthList, inTwd, inTws, inDeltaT):
        """
        computes distance given a 
        """
        pass

    def reached_waypoint(self):
        pass

    def filterTWA(self):
        pass

    def clean_isochrone(self, leftNbPoints=300):
        """
        gets:
            (int) leftNbPoints : the number of points left on the isochrone forehead after cleaning
        
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
