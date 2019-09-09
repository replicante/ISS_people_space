#!/usr/bin/env python
# -*- coding: utf-8 -*-

# check ISS location, pass for a particular location or how many people
# are in the space, using Open Notify API (http://open-notify.org)

import requests
from datetime import datetime
import json
 
def get_next_pass(lat, lon, alt):
    # alt variable is optional
    iss_url = 'http://api.open-notify.org/iss-pass.json'
    location = {'lat': lat, 'lon': lon, 'alt': alt}
    response = requests.get(iss_url, params=location).json()
    
    next_pass = response['response'] [0] ['risetime']
    next_pass_time= datetime.utcfromtimestamp(next_pass)
    
    second_pass = response['response'] [1] ['risetime']
    second_pass_time= datetime.utcfromtimestamp(second_pass)
    
    third_pass = response['response'] [2] ['risetime']
    third_pass_time= datetime.utcfromtimestamp(third_pass)
    
    print(f"For latitude: {lat}, longitude: {lon} and altitude: {alt},\
    the next pass (UTC) are: {next_pass_time}, {second_pass_time}, {third_pass_time}\n")

def people_space():
    people_url = 'http://api.open-notify.org/astros.json'
    response = requests.get(people_url).json()

    print('People in the space: ', response['number'])
    print()
    people = response['people']

    for n in people:
        print(n['name'] + ' is in ' + n['craft'])
    print()

def position():
    iss_urlnow = "http://api.open-notify.org/iss-now.json"
    response = requests.get(iss_urlnow).json()
    time_now = response['timestamp']
    time_utc = datetime.utcfromtimestamp(time_now)
    print(response['message'], ",time UTC", time_utc, response['iss_position'])

def main():
    print("ISS pass times, people in space and current position.\n")
    # change the value for your localization
    get_next_pass(52.5243683, 13.4105301,75) 
    people_space()
    position()

if __name__ == '__main__':
    main()
    
    
    
