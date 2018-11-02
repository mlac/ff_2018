import csv

ff_analytics_data = 'week_2_data/Sunday_Evening_Game/ffa_customrankings2018-2.csv'
yahoo_analytics_data = 'week_2_data/Sunday_Evening_Game/Yahoo_DF_player_export.csv'
positions_we_care_about = ['QB','TE','RB','WR','DST']

output_file_ffa = 'week_2_data/Sunday_Evening_Game/cleaned_ffa_customrankings2018-2.csv'
output_file_yahoo = 'week_2_data/Sunday_Evening_Game/cleaned_Yahoo_DF_player_export.csv'
conversion_key_dict = {}

conversion_key_dict['Saints'] = 'New Orleans Saints'
conversion_key_dict['Steelers'] = 'Pittsburgh Steelers'
conversion_key_dict['Patriots'] = 'New England Patriots'
conversion_key_dict['Todd Gurley'] = 'Todd Gurley II'
conversion_key_dict['Buccaneers'] = 'Tampa Bay Buccaneers'
conversion_key_dict['Eagles'] = 'Philadelphia Eagles'
conversion_key_dict['Falcons'] = 'Atlanta Falcons'
conversion_key_dict['Browns'] = 'Cleveland Browns'
conversion_key_dict['Chargers'] = 'Los Angeles Chargers'
conversion_key_dict['Raiders'] = 'Oakland Raiders'
conversion_key_dict['Bills'] = 'Buffalo Bills'
conversion_key_dict['Giants'] = 'New York Giants'
conversion_key_dict['Marvin Jones'] = 'Marvin Jones Jr.'
conversion_key_dict['Lions'] = 'Detroit Lions'
conversion_key_dict['Panthers'] = 'Carolina Panthers'
conversion_key_dict['49ers'] = 'San Francisco 49ers'
conversion_key_dict['Odell Beckham'] = 'Odell Beckham Jr.'
conversion_key_dict['Dolphins'] = 'Miami Dolphins'
conversion_key_dict['Redskins'] = 'Washington Redskins'
conversion_key_dict['Cardinals'] = 'Arizona Cardinals'
conversion_key_dict['Texans'] = 'Houston Texans'
conversion_key_dict['Melvin Gordon'] = 'Melvin Gordon III'
conversion_key_dict['Titans'] = 'Tennessee Titans'
conversion_key_dict['Jaguars'] = 'Jacksonville Jaguars'
conversion_key_dict['Will Fuller'] = 'Will Fuller V'
conversion_key_dict['Rams'] = 'Los Angeles Rams'
conversion_key_dict['Colts'] = 'Indianapolis Colts'
conversion_key_dict['Sammie Coates'] = 'Sammie Coates Jr.'
conversion_key_dict['Jets'] = 'New York Jets'
conversion_key_dict['Paul Richardson'] = 'Paul Richardson Jr.'
conversion_key_dict['Chiefs'] = 'Kansas City Chiefs'
conversion_key_dict['Broncos'] = 'Denver Broncos'
conversion_key_dict['Packers'] = 'Green Bay Packers'
conversion_key_dict['Vikings'] = 'Minnesota Vikings'
conversion_key_dict['Cowboys'] = 'Dallas Cowboys'

players_this_week = []

with open(ff_analytics_data,'rb') as csvfile:
    reader = csv.reader(csvfile)
    with open(output_file_ffa,'w') as csv_out:
        writer = csv.writer(csv_out)
        skip_first_row = 0
        for row in reader:
            if skip_first_row == 0:
                writer.writerow(row)
                skip_first_row += 1
                pass
            else:
                if row[3] in positions_we_care_about:
                    if int(row[11]) < 1000:
                        if row[1] in conversion_key_dict.keys():
                            row[1] = conversion_key_dict[row[1]]
                        writer.writerow(row)
                        players_this_week.append(row[1])
                else:
                    pass
print players_this_week

with open(yahoo_analytics_data,'rb') as csvfile:
    reader = csv.reader(csvfile)
    with open(output_file_yahoo,'w') as csv_out:
        writer = csv.writer(csv_out)
        skip_first_row = 0
        for row in reader:
            if skip_first_row == 0:
                writer.writerow(row)
                skip_first_row += 1
                pass
            else:
                name = row[1] + ' ' + row[2]
                if name in players_this_week:
                    writer.writerow(row)
                else:
                    print name, row[3]
