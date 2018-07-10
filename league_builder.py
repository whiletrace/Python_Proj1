
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
class player(object):
    """docstring for player"""
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
            pass

# team class
class team(object):
    """docstring for team"""
    def __init__(self, arg):
        super(team, self).__init__()
        self.arg = arg
        pass
    # will have a name
    # will contain players
    # each team will have equal number of players
    # each team will have equal number of experienced players

#coordinator class
class cordinator(object):
    """docstring for cordinator"""
    def __init__(self, arg):
        super(cordinator, self).__init__()
        self.arg = arg
        
     # cordinator will create players from the soccer_players csv
     def playercreate(self):
        # read data from soccer_players csv
        # convert data to a usable format I believe a set of dictionaries
        with open('soccer_players.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row['first_name'], row['last_name'])


        # cordinator will create teams
            #create three teams Raptors Dragons Sharks I believe the these too can be a set
            # cordinator will distribute players to teams
            # equal number of 




# Each team has the same number of players and the same number of experienced players 
# Create a text file that has each team name with the players listed underneath the team name
# the players printed should be formatted such as name, age height, experienced,Gaurdians
if __name__ == '__main__':
    main()