import numpy as np

def bilinearInterp(inKnownCornersCoords, inKnownCornersValues, inX, inY):
    """
    Vectorised bilinear interpolation :
    Computes bilinear interpolation for several points and value fields at once
   
    Gets :
        - inKnownCornersCoords : - corners coordinates of the cell where interpolation occurs.
                                 - numpy array [[0,0,1,1],..., [0,0,1,1]]
                                             x1,y1,x2,y2      
                                                cell 1 ,...,   cell 2

        - inCornersValues : - values of the field to interpolate at the cells corner
                            - numpy array [[0,0,1,1],..., [0,0,1,1]]
                                        Q11,Q12,Q21,Q22
        
        - inX : numpy array of x coordinates where interpolation must be computed [[x1, x2, x3, ...., xn]]
        - inY : same as inX but with y coords !

    Returns :

        - numpy array containing the interpolated values at the desired points.

    Cell corner coords :
        P12 (x1,y2) ... P22 (x2,y2)
            |               |
            |               | 
        P11 (x1,y1) ... P21 (x2,y1)
    
    field values matrix :
        Q12 --- Q22
         |       |            
         |       |
        Q11 --- Q21



    Example :
        
    bilinearInterp(np.array([[0,0,1,1], [0,0,1,1]]),np.array([[0,0,1,2],[0,0,1,2]]),np.array([[0.5, 0.25]]),np.array([[0.5, 0.25]]))

    will compute interpolation of the field values:
    
    0 ... 2                         (1,1) ... (2,2)
    |     | in the cell of coords     |         |
    0 ... 1                         (0,0) ... (1,0)

    for the points (0.5,0.5) and (0.25,0.25).
    """

    if (inKnownCornersCoords.shape != inKnownCornersValues.shape ):
        raise Exception("Corners Coords array and Corners Values array must be of same dimension")
    
    if (inX.shape != inY.shape ):
        raise Exception("X coords array and Y coords array must be of same dimension")

    if (inX.shape[1] != inKnownCornersCoords.shape[0]):
        raise Exception("Corners arrays shape (n,p) and Points coords arrays shape (p,t) must have a common dim !")

    x1 = inKnownCornersCoords[:,0]
    y1 = inKnownCornersCoords[:,1]
    x2 = inKnownCornersCoords[:,2]
    y2 = inKnownCornersCoords[:,3]

    fq11 = inKnownCornersValues[:,0]
    fq12 = inKnownCornersValues[:,1]
    fq21 = inKnownCornersValues[:,2]
    fq22 = inKnownCornersValues[:,3]

    xMatrix = np.stack((x2-inX,inX-x1),axis=-1).reshape(inX.shape[1],2)
    
    gauche = np.stack((fq12,fq11),axis=-1)
    droite = np.stack((fq22,fq21),axis=-1)
    qMatrix=np.stack((gauche,droite),axis=-1)

    yMatrix = np.stack((y2-inY,inY-y1),axis=-1).reshape(inY.shape[1],2)

    coeffs = 1/((x2-x1)*(y2-y1))

    interpoledMatrix = coeffs*xMatrix@(qMatrix@yMatrix.T)

    interpolatedReshaped = interpoledMatrix.reshape(1,len(interpoledMatrix),interpoledMatrix.size//len(interpoledMatrix)).copy()
    
    mask = np.concatenate((np.array([1]),np.zeros(len(inKnownCornersValues)**2-1))).reshape(len(inKnownCornersValues)**2,1)
    repeatedMask = np.repeat(mask,len(inKnownCornersValues),axis=1)
    for i in range(1,len(inKnownCornersValues)):
        repeatedMask[:,i]=np.roll(repeatedMask[:,i],(len(inKnownCornersValues)+1)*i)
    
    filteredInterpolated = interpolatedReshaped*repeatedMask.T

    finalIdx = np.where(filteredInterpolated != 0)
    interpolatedFinal = filteredInterpolated[:,finalIdx[1],finalIdx[2]].reshape(len(inKnownCornersValues),1)


    return interpolatedFinal

# wikiBIs(np.array([[0,0,1,1], [0,0,1,1]]),np.array([[0,0,1,2],[0,0,1,2]]),np.array([[0.5, 0.25]]),np.array([[0.5, 0.25]]))
toto = bilinearInterp(np.array([[0,0,1,1]]),np.array([[0,0,1,2]]),np.array([[0.5, 0.25]]),np.array([[0.5, 0.25]]))
print(toto)
