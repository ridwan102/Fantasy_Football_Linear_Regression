from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd

def fantasy_points(link, season):
    
    """
    From Pro-Football-Reference link stub, request running back html, parse with BeautifulSoup, and
    collect 
        - Name 
        - Carries
        - Rush Yards
        - Rush Yard Per Attempt
        - Touchdowns
    Return information as a dictionary.
    """

    base_url = 'https://www.pro-football-reference.com'
    fantasy = '/fantasy/'

    #Create full url to scrape
    url = base_url + link + fantasy + season

    #Request HTML and parse
    response = requests.get(url)
    page = response.text
    soup = BeautifulSoup(page,"lxml")

    name = soup.find('h1').find('span').text

    table = soup.find('tbody')

    #Breaking down all data via rows via tr tag
    rows = [row for row in table.select('tr')] 

    fantasy_points = {}

    for row in rows:
        # fantasy_points[row] = rows.find_all(class_='right')[28].text
        items = row.find_all('td',attrs={'data-stat':'fantasy_points'})
        fantasy_points[row] = [i.text for i in items]
    
    df_fantasy_points = pd.DataFrame(fantasy_points).T.reset_index() #transpose

    df_fantasy_points.columns = ['Name','Fantasy_Points']

    df_fantasy_points['Name'] = np.where(df_fantasy_points['Name'], name , df_fantasy_points['Name'])
    
    # df_defense['Date'] = pd.to_datetime(df_defense['Date'])
    df_fantasy_points[['Fantasy_Points']] = df_fantasy_points[['Fantasy_Points']].apply(pd.to_numeric)


    return df_fantasy_points