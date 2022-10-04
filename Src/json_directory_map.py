import json
import os

"""
Generates a projectMap JSON config file for the project

"""

# Root Directory of the project
rootDir = '/home/tom/Bureau/Developpement/Git/MOwnR/'

# Virtual Regatta's wind files Directory
vrWndDir = 'https://static.virtualregatta.com/winds/'

# Storage directories architecture
dataDir = 'Data/'
foliumDir = dataDir + 'Folium/'
gribDir = dataDir + 'Gribs/'
isochroneDir = dataDir + 'Isochrones/'
mapDir = dataDir +'MapsVR/'
polarDir = dataDir + 'Polaires/'
sourceCodeDir = 'Src/'
wndDir = dataDir + 'Wnd/'

#Virtual Regatta's API parameters

ApiUrl = 'https://roboats.virtualregatta.com/api/'
login = 'login'
legInfo = 'infos/slow'
boatInfo = 'infos/fast'
boatActions = 'boat/actions'

raceId = 531 # Iroboat Qualification Race
leg = 1 # leg number for the raceId Race



# Project map dictionary
arborescence = {"root" : rootDir,
                "vrwind" : vrWndDir,
                "storage" : {
                    "src": sourceCodeDir, 
                    "data" : { 
                        "wnd": wndDir, 
                        "grib": gribDir, 
                        "polar" : polarDir, 
                        "map" : mapDir, 
                        "iso" : isochroneDir,
                        "folium" : foliumDir
                        }
                    },
                "api": {
                    "url":ApiUrl,
                    "leg": legInfo,
                    "bs": boatInfo,
                    "ba": boatActions,
                    "raceId" : raceId,
                    "leg_num" : leg,
                    "login" : {
                        "subUrl" : login,
                        "headers" : {'accept': '*/*','Content-Type': 'application/json'},
                        },
                    "slow" :{
                        "subUrl" : legInfo
                        },
                    "fast" :{
                        "subUrl" : boatInfo
                        }
                    }
                }

with open(os.path.join(rootDir,sourceCodeDir,'projectMap.JSON'), 'w') as outfile :
    json.dump(arborescence,outfile,indent = 2)
    
                