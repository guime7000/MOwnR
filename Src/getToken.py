import requests
import json 
import logging
import time
from datetime import datetime
import os

import getArborescence

"""
    Retrieves a 1 hour validity Token after checking the current token isn't valid anymore

    Logs : wether token has been written to file (response [200]) or an error occured (response [400])

    Gets : - inApiDict : dict containing all API infos extracted from projectMap.JSON file
           - inAccounParams : email account and password credentials
    
    Returns : - writes token export timestamp and token in a JSON file.
"""

# Loads VR email account and password File
with open('/home/tom/Developpement/Git/MOwnR/Prod/Secret/email.config', 'r') as accountFile :
    accountParams = accountFile.readlines()

# Loads Project Map JSON file :
arborescence = getArborescence.getArborescence()

# Sets Token log file path
logFileName = 'token.log'
logFilePath = os.path.join(arborescence['root'],arborescence['storage']['data']['log'],logFileName)
logging.basicConfig(filename=logFilePath, encoding='utf-8', level=logging.INFO)

apiResponseError = True
tokenFilePath = os.path.join(arborescence['root'],arborescence['storage']['data']['wnd'],'token.JSON')

while apiResponseError:

    tokenTimestamp = int(time.time())
    loginHeaders = arborescence['api']['login']['headers']
    loginDict = json.JSONEncoder().encode({"email": accountParams[0].replace("\n",""),
                                           "password": str(accountParams[1]),
                                           "raceId": arborescence['api']['raceId'],
                                           "legNum": arborescence['api']['leg_num']})

    urlString = arborescence['api']['url'] + arborescence['api']['login']['subUrl']
    response = requests.post(urlString, data = loginDict, headers = loginHeaders)

    if response.status_code == 200 :
        with open(tokenFilePath, 'w') as outfile :
            json.dump({'exportTs': tokenTimestamp, 'token': response.headers['Token']},outfile,indent = 2)

        logTimestamp = datetime.utcfromtimestamp(tokenTimestamp).strftime('%Y-%m-%d %H:%M:%S')
        logging.info(f"{logTimestamp} : Token written to {tokenFilePath}")

        apiResponseError = False

    else :
        logging.error(f"{logTimestamp} : code {response.status_code}" )
        time.sleep(30)


    
