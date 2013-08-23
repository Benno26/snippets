#!/usr/bin/env python

import csv
import datetime
import os

home_path = os.path.expanduser('~')
file_location = 'fixtures.txt'
csv_location = 'csv_file.csv'

file_path = os.path.join(home_path,file_location)
csv_path = os.path.join(home_path,csv_location)

fixtures = []
fixture_date = ''

with open(file_path) as data:
    for line in data:
        fixture = {}
        if ' v ' not in line:
            fixture_date = datetime.datetime.strptime(line.strip(), '%d %B %Y').strftime('%d/%m/%y')
        elif ' v ' in line:
            if ',' in line:
                real_line = text.split(',', 1)[0]
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
f = open(csv_path, 'w+')
dict_writer = csv.DictWriter(f, keys)
dict_writer.writer.writerow(keys)
dict_writer.writerows(fixtures)
