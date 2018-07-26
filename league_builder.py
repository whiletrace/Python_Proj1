
import csv
# Optional
    # create classes and objects
    # player class 
        # player attributes
        # name
        # age
        # experience
        # gardians

#coordinator class
class Cordinator:
    """docstring for cordinator"""
    def __init__(self, csv_file = None):
        self.players = self._read_file_return_players(csv_file)
        

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

    
    def _player_sort(self):
       print('Running self._make_teams()\n')
       print(self.players)




# player class
class Player:
    """docstring for player"""
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
            pass

# team class
class Team:
    """docstring for team"""
    def __init__(self, players = None, *args):
        # will have a name
        # will contain players
        self.players = players
        for name in args:
            setattr(self, 'name',args)
    #Class method to create teams from players
    @classmethod
    def create_team(cls, player_pool):
        # cordinator will create teams
        count = 0
        players = []
        for player in player_pool:
            while count < 3:
                players.append(player)
                count += 1
        return cls(players)
        #create three teams Raptors Dragons Sharks I believe the these too can be a set
        # cordinator will distribute players to teams
        pass


        pass
    
    # each team will have equal number of players
    # each team will have equal number of experienced players



# Each team has the same number of players and the same number of experienced players 
# Create a text file that has each team name with the players listed underneath the team name
# the players printed should be formatted such as name, age height, experienced,Gaurdians
if __name__ == '__main__':
    
 John = Cordinator()
 John.playercreate
 Raptors = Team.create_team( "Raptors")