
import csv

'''

    note:
    to see output for any method in console
    uncomment print() statements in respective method

    '''

#oordinator class
class Coordinator():
    """docstring for Coordinator"""

    def __init__(self, csv_file = None):

        #Coordinator attributes value: method calls
        self.players = self._read_file_return_players(csv_file)
        self.playersort = self._player_sort()
        self.teams = self._create_team()
        self.write_file = self._write_to_file()

    # cordinator will create players from the soccer_players csv
    
    
    
    # for check access player.Name
    def _read_file_return_players(self,csv_file):

        # read data from soccer_players csv
        with open('soccer_players.csv', newline = '') as csvfile:

            # var holds a list of strings which will be passed to ortderd dict
            fieldnames = ['name', 'height','experience','gaurdians']

            # convert data from csv to a usable format ordered dict
            # fieldnames consumed as keys for ordered dict key value
            reader = csv.DictReader(csvfile, fieldnames = fieldnames)
            #print(reader)

            # instantiate player objects from parced csv data
            player_pool = [Player(**row) for row in reader][1:]
            #for item in player_pool:
                #print(item)

        #return value unsorted list of player objects
        return player_pool

    # method sorts player objects for team instantiation
    def _player_sort(self):

        #Consumes return value of def_read_file_return_players
        # initial sort completed based upon player attr: experience 
        sorted_list = sorted(self.players, key = lambda player: player.experience)
        # uncomment to see initial sort
        #print(sorted_list)

        # from sorted list players are sorted further 
        List_no = sorted_list[:9]
        #print(List_no)

        List_yes = sorted_list[9:]
        #print(List_yes)

        #bplayer sorts lists are complete
        Sharks =  List_no[:3] + List_yes[:3]
        Raptors = List_no[3:6] + List_yes[3:6]
        Dragons = List_no[6:9] + List_yes[6:9]
        #print(Sharks)
        #print(Raptors)
        #print(Dragons)

        #creation of dicts from list sorting: {name: teamsname, players: [players]}
        Sharksdict = dict([('name','Sharks'), ('players', Sharks)])
        Dragonsdict = dict([('name','Dragons'), ('players', Dragons)])
        Raptorsdict = dict([('name','Raptors'), ('players', Raptors)])
        Compl_Teams = Sharksdict, Dragonsdict, Raptorsdict
        # for item in Comp_Teams:
        #   print(item)

        #return tuple of dicts
        return Compl_Teams
        
    
    
    #method instantiates team istances
    def _create_team(self):

        # list comprehension that instantiates team instances 
        # Consumes return value of method _player_sort: tuple of dicts
        # Class unpacks dicts on object instantiation
        Team_list = [ Team(**item) for item in self.playersort]

        # return value: list of team objects
        # uncomment to see list of team objects
        # print(Team_List)
        return Team_list

     #Create a text file
    def _write_to_file(self):
        with open("team.txt", "a") as file:
            for item in self.teams:
                team_name = str(item)
                file.write('\n''\n')
                file.write(team_name)
                for player in item.players:
                    playerstats = str(player)
                    file.write('\n')
                    file.write(playerstats)

# Player class
    # name
    # age
    # experience
    # gardians
class Player():
    """docstring for player"""
    def __init__(self, **kwargs):
        # checks to see what is getting passed to instance args and kwargs for team attr 
        # print('ARGS: ', args)
        # print('KWARGS: ', kwargs)
        # print('------------------')
       # object instance attr set bt kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)

    # over ride str method for object instance for ease of formatting
    def __str__(self):
        return "{}, {}, {}".format(self.name, self.experience, self.gaurdians)

# Team class
    # name
    # playerss
class Team():
    """docstring for team"""

    #in this case name: 'Sharks' players: [Player objects]
    def __init__(self,*args, **kwargs):

        # checks to see what is getting passed to instance
        # print('ARGS: ', args)
        # print('KWARGS: ', kwargs)
        # print('------------------')
        # object instance attr set bt kwargs
        for key, value,in kwargs.items():
            setattr(self, key, value)

    # over ride str method for object instance for ease of formatting
    def __str__(self):
        return '{}:'.format(self.name)

# script inititialization
if __name__ == '__main__':  
    John = Coordinator()
