import requests
from bs4 import BeautifulSoup
import pandas as pd

#===========================================================
#======CORPORATE_BONDS=====================================
#===========================================================

# Create an URL object
url = 'https://kase.kz/ru/bonds/'
# Create object page
page = requests.get(url)

# parser-lxml = Change html to Python friendly format
# Obtain page's information
soup = BeautifulSoup(page.text, 'lxml')

table1 = soup.find('table', id='sorting_table_bonds_list')
headers = []

for i in table1.find_all('th'):
    title = i.text
    title = title.replace('\n', '')
    title = title.strip()
    headers.append(title)

#create a dataframe of corporate bonds
cbonds = pd.DataFrame(columns=headers)

for j in table1.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    length = len(cbonds)
    cbonds.loc[length] = row

cbonds = cbonds.replace('\n','', regex=True)
cbonds = cbonds.replace('–', '', regex=True)
cbonds = cbonds.replace(' ', '', regex=True)

cbonds.to_excel('c_bonds.xlsx')


#print(cbonds)