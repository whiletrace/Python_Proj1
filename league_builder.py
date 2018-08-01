
import csv

# Optional

    # player class 
        # player attributes
        # name
        # age
        # experience
        # gardians

# create classes and objects

#oordinator class
class Coordinator():
    """docstring for Coordinator"""
    def __init__(self, csv_file = None):
        self.players = self._read_file_return_players(csv_file)
        self.playersort = self._player_sort()
        self.teams = self._create_team()

    # cordinator will create players from the soccer_players csv
    
    def _read_file_return_players(self,csv_file):

        # read data from soccer_players csv
        # convert data to a usable format ordered dict
        # create player class instances
        # for check access player.Name

        with open('soccer_players.csv', newline = '') as csvfile:
            fieldnames = ['name', 'height','experience','gaurdians']
            reader = csv.DictReader(csvfile, fieldnames = fieldnames)
            player_pool = [Player(**row) for row in reader][1:]
        return player_pool

    
    #Sorts players for teams
       
    def _player_sort(self):
        sorted_list = sorted(self.players, key = lambda player: player.experience)
        List_no = sorted_list[:9]
        List_yes = sorted_list[9:]
        Sharks =  List_no[:3] + List_yes[:3]
        Raptors = List_no[3:7] + List_yes[3:7]
        Dragons = List_no[7:9] + List_yes[7:9]
        Sharksdict = dict([('name','Sharks'), ('players', Sharks)])
        Dragonsdict = dict([('name','Dragons'), ('players', Dragons)])
        Raptorsdict = dict([('name','Raptors'), ('players', Raptors)])
        Compl_Teams = Sharksdict, Dragonsdict, Raptorsdict
        return Compl_Teams
        
        

    #create teams from sorted players
    def _create_team(self):

        Team_list = [ Team(**item) for item in self.playersort ]
        for item in Team_list:
            print(dir(item))
        
        return Team_list
        


# Player class
class Player():
    """docstring for player"""
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
            

# Team class

# Team class
class Team():
    """docstring for team"""
    # if pass in key arguments ouput should be named attributes and values
    #in this case name: 'Sharks' players: [Player objects]
    def __init__(self,*args, **kwargs):
        print('ARGS: ', args)
        print('KWARGS: ', kwargs)
        print('------------------')
        for key, value,in kwargs.items():
            setattr(self, key, value)
    
    # This calls self.teams = self._create_team() because method does not yet return value

    
if __name__ == '__main__':
    john = Coordinator()
        # will have a name
        # will contain players
        
    #Class method to create teams from players
   
        #create three teams Raptors Dragons Sharks I believe the these too can be a set
        # cordinator will distribute players to teams
     

# Each team has the same number of players and the same number of experienced players 
# Create a text file that has each team name with the players listed underneath the team name
# the players printed should be formatted such as name, age height, experienced,Gaurdians

    
 
