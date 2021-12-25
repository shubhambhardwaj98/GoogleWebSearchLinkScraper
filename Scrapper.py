import pandas as pd
import requests
import json
import csv
items = pd.read_csv('asd.csv')          #read names from the fil
items.columns = ['Medicine Name']
itemsList = items['Medicine Name'].tolist()        
linkList = []

for item in itemsList:
    params = {
        "q": item,
        "api_key" : 'E5197A3C2E8B44348BD4379C91FC4273',
        'page': '1',
        'num': '1'
    }
    api_result = requests.get('https://api.valueserp.com/search', params)
    #print(json.dumps(api_result.json(),indent=4, sort_keys=True))
    x  = json.dumps(api_result.json(),indent=4, sort_keys=True)
    aDict = json.loads(x)
    try:
        itemURL = aDict['organic_results'][0]['link']
        linkList.append(itemURL)
    except:
        linkList.append('NULL')
print(linkList)
fields = ['1mglinks']
with open('abc.csv', 'w') as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerow(fields)
    for url in linkList:
        write.writerow([url])