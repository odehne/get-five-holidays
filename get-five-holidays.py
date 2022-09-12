from textwrap import indent
import requests
import sys 
import queryCache
from datetime import datetime

CACHE_FILENAME = 'cachedQueries.txt'
NAGER_API_URL_PREFIX = 'https://date.nager.at/api/v3/NextPublicHolidays'

#pyinstaller --noconfirm --onedir --console  "C:/git/priv/get-five-holidays/get-five-holidays.py"  
    
def getResultItems(items):
    if items == None:
        return None
    ret = ""
    for t in items:
        ret += f'{(t)},'
    return ret.strip(',')
    
if len(sys.argv) < 2:
    print(f'Wrong usage: get-five-holis <countryCode>')
    sys.exit(-1)

countryCode = sys.argv[1]
#today = str(datetime.now().date())
#check if cached results are available
cache = queryCache.load(CACHE_FILENAME)
cachedQueries = queryCache.fetch(countryCode, cache)

#Country code not in today's cache, let's make a request against the API endpoint
print(f'Fetching next 5 holidays for country {countryCode}')
nager_api_url_holidays = f'{NAGER_API_URL_PREFIX}/{countryCode}'
response = requests.get(nager_api_url_holidays)
if response.status_code != 200:
    print(f'Query failed, API returned {response.status_code}. Most likely given country code is not supported.')
else:
    holidays = response.json()
    for i in range(5):
        si=str(i)
        cachedQueries['countryCodes'][countryCode]['results'][si] = { 'holiday': holidays[i]["date"], 'localName': holidays[i]["localName"], 'counties': getResultItems(holidays[i]["counties"]), 'types': getResultItems(holidays[i]["types"])} 
    queryCache.save(cachedQueries, CACHE_FILENAME)
    queryCache.printQueryResult(cachedQueries['countryCodes'][countryCode]['results'])

