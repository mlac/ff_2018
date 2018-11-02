from collections import defaultdict
'''
DocString - should actually tell you what this file does...

Highlight inputs, and outputs.

'''

import csv

# Location of data folder for the week
data_folder = 'week_2_data/Sunday_Evening_Game'

# Enter the name / location for the dat file for the week
output_file = 'week_2_data/Sunday_Evening_Game/week_2_evening_dat.dat'

# Enter the location of input data for the week
ff_analytics_data = "week_2_data/Sunday_Evening_Game/cleaned_ffa_customrankings2018-2.csv"
yahoo_fantasy_data = "week_2_data/Sunday_Evening_Game/cleaned_Yahoo_DF_player_export.csv"


#cost max parameter
maximum_cost = 200.0
maximum_cost_output = 'param Cmax := ' + str(maximum_cost) + ' ;'

# Define output lists
output_Param_Player = defaultdict(list)

output_Param_Player_Positions = defaultdict(list)


#define intermediate player matrix list to build out position matrix
position_matrix_dict = defaultdict(list)
#                            QB,WR,RB,TE,DEF,WRT
position_matrix_dict['QB'] = [1,0,0,0,0,0]
position_matrix_dict['WR'] = [0,1,0,0,0,1]
position_matrix_dict['RB'] = [0,0,1,0,0,1]
position_matrix_dict['TE'] = [0,0,0,1,0,1]
position_matrix_dict['DEF']= [0,0,0,0,1,0]

# define a class for each player

class Player:

    def __init__(self, name):
        self.name = name
        self.position = ''
        self.exp_points = 0.0
        self.exp_lower_points = 0.0
        self.exp_upper_points = 0.0
        #arbitrarily high salary in case it doesn't exist
        self.salary = 100
        self.position_matrix = []
        self.game_time = ''

    def add_position(self, position):
        self.position = position
        #auto populate position matrix once position is assigned
        self.position_matrix = position_matrix_dict[position]

    def add_exp_points(self, expected_points):
        self.exp_points = expected_points

    def add_exp_upper_points(self, expected_upper_points):
        self.exp_upper_points = expected_upper_points

    def add_exp_lower_points(self, expected_lower_points):
        self.exp_lower_points = expected_lower_points

    def add_salary(self, salary):
        self.salary = salary

    def add_game_time(self, game_time):
        self.game_time = game_time

#Populate output lists
player_instance_list = []
player_in_yahoo_names_list = []


with open(yahoo_fantasy_data,'rb') as csvfile:
    reader = csv.reader(csvfile)
    skip_first_row = 0
    for row in reader:
        if skip_first_row == 0:
            skip_first_row += 1
            pass
        else:
            player_class_instance = row[1]+'_'+row[2]
            player_in_yahoo_names_list.append(row[1] + ' ' + row[2])
            player_name = row[1] + ' ' + row[2]
            position = row[3]
            salary = row[8]
            game_time = row[7]
            player_class_instance = Player(player_name)
            # print player_class_instance.name
            player_class_instance.add_position(position)
            player_class_instance.add_salary(salary)
            player_class_instance.add_game_time(game_time)
            player_instance_list.append(player_class_instance)
            # print vars(player_class_instance)
            skip_first_row +=1

#print player_instance_list
print player_in_yahoo_names_list

players_in_ff_analytics_list = []


with open(ff_analytics_data,'rb') as csvfile:
    reader = csv.reader(csvfile)
    skip_first_row = 0
    for row in reader:
        if skip_first_row == 0:
            skip_first_row += 1
            pass
        else:
            players_in_ff_analytics_list.append(row[1])

players_in_yahoo_not_in_FF_analytics_list = []
players_in_both_lists = []

for player in player_in_yahoo_names_list:
    if player in players_in_ff_analytics_list:
        players_in_both_lists.append(player)
    else:
        players_in_yahoo_not_in_FF_analytics_list.append(player)

print len(players_in_yahoo_not_in_FF_analytics_list)
print players_in_yahoo_not_in_FF_analytics_list


with open(ff_analytics_data,'rb') as csvfile:
    reader = csv.reader(csvfile)
    skip_first_row = 0
    for row in reader:
        if skip_first_row == 0:
            skip_first_row += 1
            pass
        else:
            skip_first_row += 1
            exp_points = float(row[7])
            expected_lower_points = float(row[8])
            expected_upper_points = float(row[9])

            for player in player_instance_list:
                try:
                    if row[1] == player.name:
                        player.add_exp_points(exp_points)
                        player.add_exp_lower_points(expected_lower_points)
                        player.add_exp_upper_points(expected_upper_points)
                except:
                    print row[1] + ' not in original list'


# Write Output Lists
output = open(output_file,'w')

#write header row for output_Param_Player
output.write('param: P:        v       C     := \n')

# write out lines of dictionary to file
for player in player_instance_list:
    try:
        output.write('"' + str(player.name) + '"' + "    " + str(player.exp_points) +
                 "    " + str(player.salary) + "\n")

    except AttributeError:
        print player.name + " not included in analysis"
        player_instance_list.remove(player)

output.write(';')

# write Cost max parameter
output.write('\n\n')
output.write(maximum_cost_output)
output.write('\n\n')

# write out header for output_Param_Position_limits
output.write( 'param:   S:  Smin    Smax    := \n')
output.write( '         QB    1       1     \n')
output.write( '         WR    3       4     \n')
output.write( '         RB    2       3     \n')
output.write( '         TE    1       2     \n')
output.write( '         DEF   1       1     \n')
output.write( '         WRT   7       7;    \n\n\n')

# write out
output.write( 'param e:     QB  WR  RB  TE     DEF  WRT := \n')
for player in player_instance_list:
    output.write( '"' + str(player.name)+ '"' + '    ' + str(player.position_matrix[0])
                                            + '    '
                                            + str(player.position_matrix[1])
                                            + '    '
                                            + str(player.position_matrix[2])
                                            + '    '
                                            + str(player.position_matrix[3])
                                            + '    '
                                            + str(player.position_matrix[4])
                                            + '    '
                                            + str(player.position_matrix[5])
                                            + '    '
                                            + '\n')

output.write( ';')

output.close()
