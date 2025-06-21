import csv
import math
import os
from tracemalloc import BaseFilter
import pandas as pd
from scrapers import *


def extract_stat_names(dict_of_stats):
    """ Extracts all the names of the statistics

    Args:
        dict_of_stats (dict): Dictionary containing key-value pair of stats
    """
    stat_names = []
    for key, val in dict_of_stats.items():
        stat_names += [key]
    return stat_names

def sort_manager_history(manager):
    """Will change the headers of the team history"""
    filename = os.getcwd() + "/data/managers/" + manager + "/25/gw_history.csv"
    df = pd.read_csv(filename)
    df = df.rename(columns={"event":"gw","points_on_bench":"bench_points","rank":"gw_rank","event_transfers":"gw_transfers","event_transfers_cost":"gw_transfers_cost"})
    df = df[['gw','points','bench_points','gw_transfers','gw_transfers_cost','total_points','gw_rank','overall_rank','bank','value',]]
    df.to_csv(filename,index = False)

def merge_picks(gw,manager):
    """adds info to gameweek picks"""
    basefile = "data/managers/" + manager + "/25/gameweeks/"
    fullfile = basefile + 'gw' + str(gw) + 'picks.csv'

    dfp = pd.read_csv(fullfile)
    dfid = pd.read_csv('data/seasons/25/player_ids.csv')
    dfgw = pd.read_csv('data/seasons/25/gameweeks/gw' + str(gw) + '.csv')

    dfp.rename(columns={"element":"id"},inplace=True)
    dfmerged = dfp.merge(dfgw,on='id')
    dfmerged = dfmerged.merge(dfid,on='id')
    dfmerged = dfmerged[['id','is_captain', 'is_vice_captain','in_dreamteam','first_name','second_name','multiplier','total_points',
        'goals_scored', 'assists', 'clean_sheets','bonus', 'bps','minutes','yellow_cards','red_cards',
       'goals_conceded','own_goals', 'saves','penalties_missed','penalties_saved', 
       'ict_index','influence','threat', 'creativity',]]

    dfmerged.to_csv(fullfile,index = False)


def sort_players(data):
    """Creates a file with sorted data for all the players in the game.
    
    Args: Raw player data
    """
    statnm = extract_stat_names(data[0])
    fnm = os.getcwd() + '/data/seasons/25/player_data_raw.csv'
    os.makedirs(os.path.dirname(fnm), exist_ok=True)
    f = open(fnm, 'w+', encoding='utf-8',newline='')
    w = csv.DictWriter(f, sorted(statnm))
    w.writeheader()
    for player in data:
        w.writerow({k:str(v).encode('utf-8').decode('utf-8') for k, v in player.items()})

def expand_picks():
    basefolder = os.getcwd() + '/data/managers/willie/gameweeks/'
    picksdf = pd.read_csv(basefolder + 'gw1picks.csv')
    

def ID_Players():
    """Creates a file that lists ID, Last Name, and First Name within FPL
    
    Args: The Raw data file that includes all data for the whole game"""

    headers = ['id', 'first_name', 'second_name']
    fin = open(os.getcwd() + '/playerdata.csv', 'r+', encoding='utf-8')
    outname = os.getcwd() + '/player_ids.csv'
    
    fout = open(outname, 'w+', encoding='utf-8', newline='')
    reader = csv.DictReader(fin)
    writer = csv.DictWriter(fout, headers, extrasaction='ignore')
    writer.writeheader()
    for line in reader:
        writer.writerow(line)

def sort_livedata(data):
    """reads in live data for a current week and creates a file for every player in the game
    """

def main():
    ID_Players()
    

if __name__ == "__main__":
    main()