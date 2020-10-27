import requests
import json
#from bs4 import BeautifulSoup
from urllib import request
import pandas as pd

url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0001-001?Authorization=CWB-47D46100-ED39-4FEF-8558-41F45A8DF1DF&locationName='
json_data = request.urlopen(url).read().decode("utf-8")
json_data = json.loads(json_data)

#frame = pd.DataFrame.from_dict(json_data)
#frame = pd.DataFrame.from_dict(json_data['records'])

for w in json_data['records']['location']:
    #for l in w:
    if w['stationId'] == 'C0E420':
        for t in w['weatherElement']:
            if t['elementName'] == 'TEMP' :
                print ("Temp: "+t['elementValue'])
            if  t['elementName'] =='HUMD':
                print ("Humd: "+t['elementValue'])
    #if w['stationId']== 'C0E420':
    #    print(w)
# html = requests.get('https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0001-001?Authorization=CWB-47D46100-ED39-4FEF-8558-41F45A8DF1DF&locationName=').content

# soup = BeautifulSoup(html,'lxml')
# links = soup.find_all('div',class_='cube-v9')

# for link in links:
#     print(link)

