from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

def all_running_backs_stats(year):

    base_url = 'https://www.pro-football-reference.com/years/'
    position = '/rushing.htm'
    
    #Create full url to scrape
    url = base_url + year + position

    response = requests.get(url)
    page = response.text

    soup = BeautifulSoup(page,"lxml")

    table = soup.find('tbody')

    #Breaking down all data via rows 
    rows = [row for row in table.select('tr')]  # tr tag is for rows

    #Calling running backs
    running_backs_dict = {}

    for row in rows[:25]:
        items = row.find_all('td')
        link = items[0].find('a')
        running_back_stat, url = link.text, link['href']
        running_backs_dict[running_back_stat] = [url] + [i.text for i in items]

    #Create a dataframe of movies
    df_all_running_backs = pd.DataFrame(running_backs_dict).T 
    df_all_running_backs.columns = ['Link','Player','Team','Age',
                        'Position', 'Games_Played', 'Games_Started','Carries_Attempted', 'Total_Yards',
                        'Total_Touchdowns','1D', 'Longest_Run', 'Yards_per_Attempt', 'Yards_per_Game','Fumbles']

    return df_all_running_backs