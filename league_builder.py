
import csv
# Optional
    # create classes and objects
    # player class 
        # player attributes
        # name
        # age
        # experience
        # gardians

# player class
class Player(object):
    """docstring for player"""
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
            pass

# team class
class team(object):
    """docstring for team"""
    def __init__(self, *args):
        super(team, self).__init__()
        self.name = name 
        self.players = {}
        pass
    # will have a name
    # will contain players
    # each team will have equal number of players
    # each team will have equal number of experienced players

#coordinator class
class Cordinator():
    """docstring for cordinator"""
    
     # cordinator will create players from the soccer_players csv
    def playercreate(self):
        # read data from soccer_players csv
        # convert data to a usable format ordered dict
        # create player class instances
        # for check access player.Name 

        with open('soccer_players.csv', newline = '') as csvfile:
            fieldnames = ['name', 'height','experience','gaurdians']
            reader = csv.DictReader(csvfile, fieldnames = fieldnames)
            player_pool = [Player(**row) for row in reader][1:]
        return player_pool
                
    
    def teamcreate(self, player_pool):
        # cordinator will create teams
        #create three teams Raptors Dragons Sharks I believe the these too can be a set
        # cordinator will distribute players to teams
        pass
            
# Each team has the same number of players and the same number of experienced players 
# Create a text file that has each team name with the players listed underneath the team name
# the players printed should be formatted such as name, age height, experienced,Gaurdians
if __name__ == '__main__':
    
 John = Cordinator()
 John.playercreate()