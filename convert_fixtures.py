#!/usr/bin/env python

import csv
import datetime

file_location = '/Users/malc/Desktop/fixtures.txt'
csv_file_location = '/Users/malc/Desktop/csv_file.csv'

fixtures = []
fixture_date = ''

with open(file_location) as data:
    for line in data:
        fixture = {}
        if ' v ' not in line:
            fixture_date = datetime.datetime.strptime(line.strip(), '%d %B %Y').strftime('%d/%m/%y')
        elif ' v ' in line:
            if ',' in line:
                real_line = line.split(',', 1)[0]
            else:
                real_line = line
            vs = real_line.strip().split(' v ')
            home_team = vs[0]
            away_team = vs[1]
            fixture['Div']='E0'
            fixture['Date']=fixture_date
            fixture['HomeTeam']=home_team
            fixture['AwayTeam']=away_team
            fixtures.append(fixture)
            
keys = ['Div','Date', 'HomeTeam', 'AwayTeam']
f = open(csv_file_location, 'w+')
dict_writer = csv.DictWriter(f, keys)
dict_writer.writer.writerow(keys)
dict_writer.writerows(fixtures)