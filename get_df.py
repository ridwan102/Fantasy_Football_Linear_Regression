from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd

def get_running_back_df(link):
    
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
    season = '/gamelog/2019'
    
    #Create full url to scrape
    url = base_url + link + season

    #Request HTML and parse
    response = requests.get(url)
    page = response.text
    soup = BeautifulSoup(page,"lxml")

    name = soup.find('h1').find('span').text

    table = soup.find('tbody')

    #Breaking down all data via rows via tr tag
    rows = [row for row in table.select('tr')] 

    running_backs = {}

    for row in rows:
        items = row.find_all('td')
        running_backs[row] = [i.text for i in items[:13]]

    # #Create a dataframe of running back stats
    df_running_backs = pd.DataFrame(running_backs).T.reset_index() #transpose

    df_running_backs.columns = ['Name','Date','Game', 'Week', 'Age', 'Team', '','Opp', 'Result','Game_Started',
    'Carries', 'Total_Rushing_Yards', 'Rushing_Yards_per_Attempt', 'Rushing_Touchdowns'] 

    # table_head = soup.find('thead').find_all('tr')[1]

    #Breaking down all data via rows 
    # column_headers = [row.text for row in table_head.find_all('th')[:14]]  # tr tag is for rows
    # column_headers[0] = 'Name'
    # df_running_backs.columns = column_headers

    df_running_backs['Name'] = np.where(df_running_backs['Name'], name , df_running_backs['Name'])
    df_running_backs = df_running_backs.drop(columns=['Game','Age','','Game_Started'])

    return df_running_backs


def get_wide_receiver_df(link):
    
    """
    From Pro-Football-Reference link stub, request wide receiver html, parse with BeautifulSoup, and
    collect 
        - Name 
        - Carries
        - Rush Yards
        - Rush Yard Per Attempt
        - Touchdowns
    Return information as a dictionary.
    """
    
    base_url = 'https://www.pro-football-reference.com'
    season = '/gamelog/2019'
    
    #Create full url to scrape
    url = base_url + link + season

    #Request HTML and parse
    response = requests.get(url)
    page = response.text
    soup = BeautifulSoup(page,"lxml")

    name = soup.find('h1').find('span').text

    table = soup.find('tbody')

    #Breaking down all data via rows via tr tag
    rows = [row for row in table.select('tr')] 

    running_backs = {}

    for row in rows:
        items = row.find_all('td')
        running_backs[row] = [i.text for i in items[:15]]

    # #Create a dataframe of running back stats
    df_wide_receivers = pd.DataFrame(running_backs).T.reset_index() #transpose

    df_wide_receivers.columns = ['Name','Date','Game', 'Week', 'Age', 'Team', '','Opp', 'Result','Game_Started',
    'Targets', 'Receptions', 'Total_Yards', 'Yards/Reception', 'Touchdowns', 'Catch%'] 

    df_wide_receivers['Name'] = np.where(df_wide_receivers['Name'], name , df_wide_receivers['Name'])
    df_wide_receivers = df_wide_receivers.drop(columns=['Game','Age','','Game_Started'])

    return df_wide_receivers


def get_defense_df(link):
    
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
    
    #Create full url to scrape
    url = base_url + link

    #Request HTML and parse
    response = requests.get(url)
    page = response.text
    soup = BeautifulSoup(page,"lxml")

    name = soup.find('h1').find_all('span')[1].text

    table = soup.find_all('tbody')[1]

    #Breaking down all data via rows via tr tag
    rows = [row for row in table.select('tr')] 

    defense = {}

    for row in rows:
        items = row.find_all('td')
        defense[row] = [i.text for i in items[:21]]

    # #Create a dataframe of running back stats
    df_defense = pd.DataFrame(defense).T.reset_index() #transpose

    df_defense.columns = ['Team','Day','Date','Time', 'Boxscore','Win/Loss','OT','Record','','Opponent','Points',
    'Opponent Score','1st Downs','Total_Yards','Pass_Yards','Rush_Yards','TurnOvers','1stDowns','Defense_Total_Yards','Defense_Pass_Yards','Defense_Rush_Yards','Turnovers'] 

    df_defense['Team'] = np.where(df_defense['Team'], name , df_defense['Team'])
    df_defense = df_defense.drop(columns=['Time','Boxscore','Win/Loss','OT','Record','','1st Downs','Total_Yards','Pass_Yards','Rush_Yards','TurnOvers'])

    return df_defense


def all_individual_stats(position_df, position_df_link):
    individual_stats = position_df(position_df_link.Link[0])

    for link in range(len(position_df_link.Link)):
        individual_stats = individual_stats.append(position_df(position_df_link.Link[link]))
    
    return individual_stats.reset_index()