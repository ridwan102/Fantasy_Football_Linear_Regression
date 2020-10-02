from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

def all_position_stats(year, stat):

    base_url = 'https://www.pro-football-reference.com/years/'
    
    #Create full url to scrape
    url = base_url + year + '/' + stat + '.htm'

    response = requests.get(url)
    page = response.text

    soup = BeautifulSoup(page,"lxml")

    table = soup.find('tbody')

    #Breaking down all data via rows 
    rows = [row for row in table.select('tr')]  # tr tag is for rows

    #Calling running backs
    position_dict = {}

    for row in rows[:25]:
        items = row.find_all('td')
        link = items[0].find('a')
        position_stat, url = link.text, link['href']
        position_dict[position_stat] = [url] + [i.text for i in items]

    #Create a dataframe of movies
    df_all_stats = pd.DataFrame(position_dict).T

    return df_all_stats


def all_rb_defense_headers(year, stat):

    base_url = 'https://www.pro-football-reference.com/years/'
    
    #Create full url to scrape
    url = base_url + year + '/' + stat + '.htm'

    response = requests.get(url)
    page = response.text

    soup = BeautifulSoup(page,"lxml")

    table_head = soup.find('thead').find_all('tr')[1]

    #Breaking down all data via rows 
    column_headers = [row.text for row in table_head.find_all('th')]  # tr tag is for rows
    column_headers[0] = 'Link'

    return column_headers

def all_wide_receiver_headers(year, stat):

    base_url = 'https://www.pro-football-reference.com/years/'
    
    #Create full url to scrape
    url = base_url + year + '/' + stat + '.htm'

    response = requests.get(url)
    page = response.text

    soup = BeautifulSoup(page,"lxml")

    table_head = soup.find('thead').find('tr')

    #Breaking down all data via rows 
    column_headers = [row.text for row in table_head.find_all('th')]  # tr tag is for rows
    column_headers[0] = 'Link'

    return column_headers