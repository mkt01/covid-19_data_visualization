import requests
import pandas as pd
import matplotlib.pyplot as plt
import locale
from locale import atof

#Get data from worldometers using BeautifulSoup 
url = requests.get("https://www.worldometers.info/coronavirus/")
from bs4 import BeautifulSoup
soup = BeautifulSoup(url.content, 'html.parser')
title = soup.title 
titleText = title.get_text()
print(titleText)
dt = []
for table in soup.find_all('table', class_ = 'table table-bordered table-hover main_table_countries'):
	th = [e.text.strip() for e in table.find_all('th')]
	for tr in table.find_all('tr'):
		td = tr.find_all('td')
		row = [e.text.strip().replace(',','') for e in td]
		dt.append(row)

# generate DataFrame from above data
df = pd.DataFrame(dt,columns=th)
df = pd.DataFrame(dt,columns=th, index=df['Country,Other'])
df = df[['TotalCases', 'TotalDeaths', 'TotalRecovered', 'ActiveCases', 'Serious,Critical']][2:12].copy()
df = df.astype(int)

# plotting data
df.plot.bar(rot=0)#stacked=True)
plt.title(titleText)
plt.show()
print(df)
