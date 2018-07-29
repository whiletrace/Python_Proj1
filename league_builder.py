
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
        self.playersort = self._player_sort()

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

    
                
            
    #test of access to players through self.players
    
    def _player_sort(self):
        sorted_list = sorted(self.players, key = lambda player: player.experience)
        List_no = sorted_list[:9]
        List_yes = sorted_list[9:]
        Sharks = List_no[:3] + List_yes[:3]
        Raptors = List_no[3:7] + List_yes[3:7]
        Dragons = List_no[7:9] + List_yes[7:9]
        teams =dict(Sharks = Sharks, Raptors= Raptors, Dragons= Dragons)
        print(teams)


        
        


        # gain ability to get value of attribute experience
        # create a list that toggles between players with Yes and No values
        # from this list create a tupple of three list
        # each list should have six players
        

       
       



# player class
class Player(Cordinator):
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