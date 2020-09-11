import swift
import subprocess
import os
import webbrowser
import datetime
import google
import requests
import time
import pywhatkit as kit
from selenium import webdriver


##############################################Swift Start Functions###########################################
def trigger():
    while True:
        action = swift.swift_ker()
        if "swift" in action:
            skill()


def start_swift():
    flag = 1
    while flag < 5:
        print("\rStarting Swift" + ("." * flag), end=" ")
        time.sleep(1)
        flag = flag + 1
    swift.play("/Users/sagnikchakraborty/SwiftBeta/audio/Swift_start.mp3")
    print("\nAsk Me Anything")
    trigger()


##############################################Swift Start Functions###########################################

##############################################Swift Basic Skill Functions###########################################
# Know Time
def sw_time():
    now = datetime.datetime.now()
    htime = swift.cttxt(now.strftime("%H"))
    mtime = swift.cttxt(now.strftime("%M"))
    stime = swift.cttxt(now.strftime("%S"))
    swift.talk("Now the time is " + htime + "hours and" + mtime + "minutes and" + stime + "seconds")
    trigger()


# Know date
def sw_date():
    now = datetime.datetime.now()
    print("Current date is:  ")
    ydate = swift.cttxt(now.strftime("%Y"))
    mdate = now.strftime("%B")
    ddate = swift.cttxt(now.strftime("%d"))
    swift.talk("Today is " + ddate + mdate + ydate)
    trigger()


# Open anything in Swift
def openinswift(name):
    open_name=name.replace("open ", "")
    swift.talk("Are you sure you want to open" + open_name)
    act = swift.input()
    if "yes" in act:
        if os.system('open -a' + open_name) == 0:
                swift.talk("Done")
                trigger()
        else:
            open_namet = "https://www." + open_name + ".com"
            swift.talk("opening" + open_name)
            webbrowser.open(open_namet, new=2)
            trigger()
    if "no" in act:
        swift.talk("Ok, not opening " + open_name)
        trigger()


# Web Functions
def swift_search_youtube(input):
    webbrowser.open("https://www.youtube.com/results?search_query=" + input)
    swift.talk("I found this on Youtube" + input)
    swift.talk("check it out")
    trigger()


def swift_search_web(input):
    lib = input
    url = "https://www.google.co.in/search?q=" + (str(lib)) + "&oq=" + (
        str(lib)) + "&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
    webbrowser.open_new(url)
    swift.talk("I found this on google for" + input)
    swift.talk("check it out")
    trigger()


# Play Anything From Web
def swift_play(action):
    kit.playonyt(action)
    swift.talk("Playing " + action)


# Weather Functions
def swift_wehth():
    def weather_data(query):
        res = requests.get(
            'http://api.openweathermap.org/data/2.5/weather?' + query + '&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');
        return res.json();

    def print_weather(result, city):
        swift.talk("Currently {} is having {}".format(city, result['weather'][0]['description']))
        swift.talk("the temperature is {} degree centigrade ".format(result['main']['temp']))
        swift.talk("Wind speed is {} m/s".format(result['wind']['speed']))
        swift.talk("Weather is {}".format(result['weather'][0]['main']))

    def weather():
        swift.talk("For which city would you like to know the weather?")
        city = swift.input()
        print()
        try:
            query = 'q=' + city;
            w_data = weather_data(query);
            print_weather(w_data, city)
            print()
        except:
            swift.talk('Sorry the City name is not found')

    weather()


# Calculation Functions
def swift_calculate():
    app_id = "WOLFRAMALPHA_APP_ID"
    client = wolframalpha.Client(app_id)

    indx = input.lower().split().index('calculate')
    query = input.split()[indx + 1:]
    res = client.query(' '.join(query))
    answer = next(res.results).text
    swift.talk("The answer is " + answer)
    return


##############################################Swift Basic Skill Functions###########################################


##############################################Swift Basic Skills###########################################
def skill():
    # swift.talk("Yes?")
    action = swift.input()
    if "what is the time" in action:
        try:
            sw_time()
        except:
            swift.talk("Cannot Access System Time")
            trigger()
    if "what is the date" in action:
        try:
            sw_date()
        except:
            swift.talk("Cannot Access System Date")
            trigger()
    if "open" in action:
        try:
            openinswift(action)
        except:
            swift.talk("I don't have a Opening App skill installed")
            trigger()
    if "search for" and "on youtube" in action:
        try:
            action = action.replace('search', '')
            action = action.replace(' for', '')
            action = action.replace(' on', '')
            action = action.replace(' youtube', '')
            swift_search_youtube(action)
        except:
            swift.talk("I don't have an search skill")
            trigger()
    if "search for" and "on web" in action:
        try:
            action = action.replace('search', '')
            action = action.replace(' for', '')
            action = action.replace(' on', '')
            action = action.replace(' web', '')
            swift_search_web(action)
        except:
            swift.talk("I don't have an search skill")
            trigger()
    if "what's the weather today" in action:
        try:
            swift_wehth()
            trigger()
        except:
            swift.talk("I don't have a weather skill installed")
            trigger()
    if "play" in action:
        try:
            action = action.replace('play', '')
            swift_play(action)
            trigger()
        except:
            swift.talk("I don't have an search skill")
            trigger()
    if "start automation" in action:
        try:
            swift_auto()
        except:
            swift.talk("You don't have an automation setup")
            trigger()
    else:
        swift.talk("Sorry, I didn't understand that")
        trigger()

##############################################Swift Basic Skills###########################################
