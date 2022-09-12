import sys
import os
import json
from datetime import datetime

#Loads our cached query results
def load(fileName):
    if os.path.exists(fileName):
        file = open(fileName, "r")
        if file.mode == "r":
            return json.load(file)
    return None

#writes the cached queries into our cache file
def save(results, fileName):
    with open(fileName, 'w') as f:
        json.dump(results, f, indent=4)

def fetch(countryCode, cachedQueries):
    today = str(datetime.now().date())
    if cachedQueries != None:
        if cachedQueries['fetchDate']==today:
            if countryCode in cachedQueries['countryCodes']:
                print(f'Fetching today\'s cached results for country {countryCode}')
                printQueryResult(cachedQueries['countryCodes'][countryCode]['results'])
                sys.exit(0)
            else:
                cachedQueries['countryCodes'][countryCode]={ 'results': {} }
                return cachedQueries
    return {'fetchDate':str(datetime.now().date()), 'countryCodes':{ countryCode: { 'results': {} }}}

def printQueryResult(holidays):
    for i in range(5):
        si = str(i)
        if holidays[si]['counties'] == None:
            print(f'{holidays[si]["holiday"]}, {holidays[si]["localName"]}, accross country, {holidays[si]["types"]}')
        else:
            print(f'{holidays[si]["holiday"]}, {holidays[si]["localName"]}, only in [{holidays[si]["counties"]}], {holidays[si]["types"]}')
 