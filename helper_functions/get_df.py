from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd

def get_running_back_df(link, season):
    
    """
    From Pro-Football-Reference link stub, request running back html, parse with BeautifulSoup, and
    collect given features
    Return information as a dataframe.
    """
    
    base_url = 'https://www.pro-football-reference.com'
    gamelog = '/gamelog/'
    
    #Create full url to scrape
    url = base_url + link + gamelog + season

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
        running_backs[row] = [i.text for i in items[:23]]

    # #Create a dataframe of running back stats
    df_running_backs = pd.DataFrame(running_backs).T.reset_index() #transpose

    df_running_backs.columns = ['Name','Date','Game', 'Week', 'Age', 'Team', '',
    'Opp', 'Result','Game_Started','Carries', 'Rush_Yards', 'Yards_per_Carry', 
    'Rush_TD','Targets','Receptions','Receiving_Yards','Y/R','Receiving_TD','Catch%', 
    'Y/Tgt', 'Total_TDs','Pts','Fumbles']

    df_running_backs['Name'] = np.where(df_running_backs['Name'], name , df_running_backs['Name'])
    df_running_backs = df_running_backs.drop(columns=['Date','Game','Team','Week','Age','','Opp','Result','Game_Started','Catch%'])

    #Convert columns to preferred data-types
    # df_running_backs['Date'] = pd.to_datetime(df_running_backs['Date'])
    df_running_backs[['Carries', 'Rush_Yards', 'Yards_per_Carry', 'Rush_TD','Targets',
    'Receptions','Receiving_Yards','Y/R','Receiving_TD', 'Y/Tgt','Total_TDs','Pts','Fumbles']] = df_running_backs[['Carries', 
    'Rush_Yards', 'Yards_per_Carry', 'Rush_TD','Targets', 'Receptions','Receiving_Yards','Y/R',
    'Receiving_TD','Y/Tgt','Total_TDs','Pts','Fumbles']].apply(pd.to_numeric)

    return df_running_backs[:-1]


def get_wide_receiver_df(link, season):
    
    """
    From Pro-Football-Reference link stub, request running back html, parse with BeautifulSoup, and
    collect given features
    Return information as a dataframe.
    """
    
    base_url = 'https://www.pro-football-reference.com'
    gamelog = '/gamelog/'
    
    #Create full url to scrape
    url = base_url + link + gamelog + season

    #Request HTML and parse
    response = requests.get(url)
    page = response.text
    soup = BeautifulSoup(page,"lxml")

    name = soup.find('h1').find('span').text

    table = soup.find('tbody')

    #Breaking down all data via rows via tr tag
    rows = [row for row in table.select('tr')] 

    wide_receivers = {}

    for row in rows:
        items = row.find_all('td')
        wide_receivers[row] = [i.text for i in items[:23]]

    # #Create a dataframe of running back stats
    df_wide_receivers = pd.DataFrame(wide_receivers).T.reset_index() #transpose

    df_wide_receivers.columns = ['Name','Date','Game', 'Week', 'Age', 'Team', '',
    'Opp', 'Result','Game_Started','Targets','Receptions','Receiving_Yards','Y/R','Receiving_TD','Catch%', 
    'Y/Tgt', 'Carries', 'Rush_Yards', 'Yards_per_Carry', 'Rush_TD','Total_TDs','Pts','Fumbles']

    df_wide_receivers['Name'] = np.where(df_wide_receivers['Name'], name , df_wide_receivers['Name'])
    df_wide_receivers = df_wide_receivers.drop(columns=['Date','Game','Team','Week','Age','','Opp',
    'Result','Game_Started','Catch%','Rush_TD','Total_TDs', 'Pts' ,'Fumbles'])

    #Convert columns to preferred data-types
    # df_wide_receivers['Date'] = pd.to_datetime(df_wide_receivers['Date'])

    df_wide_receivers[['Carries','Rush_Yards','Yards_per_Carry','Targets','Receptions','Receiving_Yards', 
    'Y/R', 'Receiving_TD','Y/Tgt']] = df_wide_receivers[['Carries','Rush_Yards','Yards_per_Carry','Targets','Receptions','Receiving_Yards', 
    'Y/R', 'Receiving_TD','Y/Tgt']].apply(pd.to_numeric)
    return df_wide_receivers[:-1]

    

def get_defense_df(team, season):
    
    """
    From Pro-Football-Reference link stub, request running back html, parse with BeautifulSoup, and
    collect given features
    Return information as a dataframe.
    """
    
    base_url = 'https://www.pro-football-reference.com/teams/'
    
    #Create full url to scrape
    url = base_url + team + "/" + season + ".htm"

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
    
    # df_defense['Date'] = pd.to_datetime(df_defense['Date'])
    df_defense[['Defense_Total_Yards','Defense_Pass_Yards','Defense_Rush_Yards']] = df_defense[['Defense_Total_Yards','Defense_Pass_Yards','Defense_Rush_Yards']].apply(pd.to_numeric)

    return df_defense


def fantasy_points(link, season):
    
    """
    Scrapes fantasy points for each individual player
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


    return df_fantasy_points[1:]

def all_individual_stats(position_df, position_df_link, season):

    """
    Creates a table with all players features for their individual game for given season
    """

    individual_stats = position_df(position_df_link.Link[0],season)

    for link in range(1, len(position_df_link.Link)):
        individual_stats = individual_stats.append(position_df(position_df_link.Link[link],season))

    return individual_stats.reset_index()