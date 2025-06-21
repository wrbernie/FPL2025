"""These functions will retrieve data from FPL website and return a text file"""

import requests
import json
import time

def scr_data():
    """
    Gets the fpl player data from database
    """
    response = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    responseStr = response.text
    data = json.loads(responseStr)
    return data

def scr_team_summary(entry_id):
    """ Retrieve the gameweek by gameweek summary/history data for a specific entry/team
    Args:
        entry_id (int) : ID of the team whose data is to be retrieved
    """
    base_url = "https://fantasy.premierleague.com/api/entry/"
    full_url = base_url + str(entry_id) + "/history/"
    response = ''
    while response == '':
        try:
            response = requests.get(full_url)
        except:
            time.sleep(5)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    data = json.loads(response.text)
    return data

def scr_entry_data(entry_id):
    """Retrieves team/manager info/data for current season
    
    Args: Team ID
    """
    base_url = "https://fantasy.premierleague.com/api/entry/"
    full_url = base_url + str(entry_id) + "/"
    response = ''
    while response == '':
        try:
            response = requests.get(full_url)
        except:
            time.sleep(5)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    data = json.loads(response.text)
    return data


def scr_player_summary(PID):
    """This function scrapes for gw data for an individual player
    
    Args:
        PID (int): ID for the player who will be reteieved.
        Returns: Text file of data for a specific player.
    """
    base_URL = "https://fantasy.premierleague.com/api/element-summary/"
    full_URL = base_URL + str(PID) + "/"
    response = ''
    while response == '':
        try:
            response = requests.get(full_URL)
        except:
            time.sleep(5)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    data = json.loads(response.text)
    return(data)


def scr_team_picks(entry_id,gw):
    """This function scrapes for gw specific data for a specific team.
    
    Args:
    entry_id(int): ID for specific team to be colected.
        gw (int): The desired gameweek
    """
    base_URL = "https://fantasy.premierleague.com/api/entry/"
    full_URL = base_URL + str(entry_id) + "/event/" + str(gw) + "/picks/"

    response = ''
    while response == '':
        try:
            response = requests.get(full_URL)
        except:
            time.sleep(5)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    data = json.loads(response.text)
    return(data)

def scr_gw_live(gw):
    """This function scrapes for all player data in a specific gameweek.

    Args:        
        gw(int): The gameweek that will be scraped.
        returns: Text file with gameweek data.
    """
    base_URL = "https://fantasy.premierleague.com/api/event/"
    full_URL = base_URL + str(gw) + "/live/"
    response = ''
    while response == '':
        try:
            response = requests.get(full_URL)
        except:
            time.sleep(5)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    data = json.loads(response.text)
    return(data)

def scr_team_transfers(entry_id):
    """This function scrapes for a teams transfers throught the season

    Args:
        entry_id (int): The(entry_id)that will be scraped
        returns: csv file with player transfers
    """
    base_url = "https://fantasy.premierleague.com/api/entry/"
    full_url = base_url + str(entry_id) + "/transfers/"
    response = ''
    while response == '':
        try:
            response = requests.get(full_url)
        except:
            time.sleep(5)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    data = json.loads(response.text)
    return data

def scr_manager_info(entry_id):
    """Scrapes a team Entry and returns profile info
    """
    base_url = "https://fantasy.premierleague.com/api/entry/"
    full_url = base_url + str(entry_id) + "/"
    response = ''
    while response == '':
        try:
            response = requests.get(full_url)
        except:
            time.sleep(5)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    data = json.loads(response.text)
    return data

def scr_club_data():
    """"Scrapes for team infomation for that season"""
    base_url = "https://footballapi.pulselive.com/football/compseasons/489/teams"
    response = ''
    while response == '':
        try:
            response = requests.get(base_url)
        except:
            time.sleep(5)
    if response.status_code != 200:
        raise Exception("Response was code " + str(response.status_code))
    data = json.loads(response.text)
    return data

def main():
    print("starting script")

    data = scr_club_data

    print(data)

    print("ending script")
    

if __name__ == "__main__":
    main()
