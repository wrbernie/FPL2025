from importlib.metadata import entry_points
from scrapers import *
from sorters import *
from writers import *

def create_gw_data():

    print("here")
    for i in range(1,39):
        data = scr_gw_live(i)
        data = data["elements"]
        gw = pd.DataFrame()
        ids = pd.DataFrame()
        

        for j in range(len(data)):
            stats = pd.DataFrame.from_records(data[j]["stats"],index = [j])
            id = pd.DataFrame({'id':[data[j]['id']]}, index = [j])
            ids = pd.concat([ids,id],axis=0)
            gw = pd.concat([gw,stats],axis=0)
        
        dataout = pd.concat([ids,gw],axis=1)
        wr_gw_live(dataout,i)

        print('finished gameweek ' + str(i))

    print('ending')

def create_manager_data(entry_id):
    
    mngdata = scr_manager_info(entry_id)
    mngname = mngdata["player_first_name"]

    print("Creating Summary File")
    sumdata = scr_team_summary(entry_id)
    wr_team_summary(sumdata,mngname)

    print("Creating Transfer File")
    transferdata = scr_team_transfers(entry_id)
    wr_team_transfers(transferdata,mngname)

    print("Getting Picks")
    for i in range(1,39):
        pickdata = scr_team_picks(entry_id,i)
        wr_gw_picks(pickdata,i,mngname)
        print("gw " + str(i) + " created")


def create_player_data():
    """ Pulls season long data and creates a csv file with it

    """
    data = scr_data()
    wr_player_data(data)



def main():

    df = pd.read_csv('manager_ids.csv')
    for i in df.team_id:    
        create_manager_data(i)

    create_player_data()

if __name__ == "__main__":
    create_player_data()

    


