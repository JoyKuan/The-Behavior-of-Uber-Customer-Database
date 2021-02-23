from collections import defaultdict
import urllib.parse
import pandas as pd
import csv, json
import sys
import requests
import re

#enter the file name and key name in command line
filename = sys.argv[1]  
csvFilePath = filename
data = pd.read_csv(csvFilePath)
df = pd.DataFrame(data)
d = df.set_index('User_ID').to_dict(orient='index')
# print(d)

jsondata = json.dumps(d)
# print(jsondata)

url = 'https://project551.firebaseio.com/index.json'
response = requests.put(url,jsondata)
print(json.dumps(response.json(), indent=2, separators=(',\t',':')))
