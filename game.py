from turtle import Turtle, Screen
from plane import Plane
from coordinate import Coordinate
from runway import Runway
from database import FlightDB
import time
import random


def investigation():
    """
    GUI receive input from player which have 3 choices
    1. all : give flight data(time and blackbox) of all plane in the screen
    2. callsign : give flight data of that plane with flight data of player's plane
    3. exit : exit program
    """
    while True:
        investigate = radar.textinput("Plane Landing Game", "Investigate!(type all/callsign of the plane/exit)")
        if investigate in name:                     # check if plane is exist by callsign
            print("Player's blackbox")
            database.search('Player')               # get Player's flight data from database
            print(investigate + "'s blackbox")
            database.search(investigate)            # get flight data from database by callsign of the plane
            print("")
        elif investigate == 'all':
            print("Player's blackbox")
            database.search('Player')               # get Player's flight data from database
            for m in range(10):                     # 10 plane on the screen
                print(name[m] + "'s blackbox")
                database.search(name[m])            # get each plane's flight data from database
                print("")
        elif investigate == 'exit':
            print("Thank you for playing")
            time.sleep(3)
            exit()
        else:                                       # if user input not in 3 choices will go back ask again
            print("type all/callsign of the plane/exit")
            continue

def draw_radar():
    """draw radar line on the screen using turtle"""
    radius = 100

    # draw vertical and horizontal line on the screen
    text.forward(500)
    text.backward(1000)
    text.forward(500)
    text.left(90)
    text.forward(500)
    text.backward(1000)
    text.right(90)

    # set turtle to middle of the screen to prepare for next drawing
    text.penup()
    text.goto(0, 0)
    text.pendown()

    # draw circle on the screen 5 times each time increase radius by 100
    for i in range(5):
        text.goto(0, -radius)
        text.circle(radius)
        radius += 100
    text.penup()


# initialize game
bot_list = []    # list that will contains plane object
runway_color_list = ['black', 'white', 'pink', 'orange']
name = ['TG', 'AA', "KLM", "AF", "QF", "BA", "JL", "QR", "MH", "EY"]  # list contains callsign of each plane
database = FlightDB("Flight database")  # create database

# setup screen
radar = Screen()
radar.setup(1000,1000)
radar.title("Plane Landing Game")


# set to be global variable
bg_color = ''
runway_c = ''
radar_sweep = 0
# GUI receive input from player to pick radar background color
while True:
    radar_color = radar.textinput("Plane Landing Game", "Pick Radar Color 1.Dark/2.White (1-2)").lower()
    if radar_color == "1" or radar_color == 'dark':
        bg_color = "black"
        break
    elif radar_color == "2" or radar_color == 'white':
        bg_color = "white"
        break
    else:
        print("Pick only 1.Dark or 2.White")
        continue

# GUI receive input from player to pick runway color
while True:
    question = "Pick Runway Color 1.Black/2.White/3.Pink/4.Orange (1-3)"
    runway_color = radar.textinput("Plane Landing Game", question).lower()
    if runway_color == "1" or runway_color == "black":
        if bg_color == 'black':                                 # check radar color and background color is the same
            print("Radar and Runway can't be the same color")
            continue                                            # go back and pick new runway color
        else:
            runway_c = runway_color_list[0]                     # black color
            break
    elif runway_color == "2" or runway_color == "white":
        if bg_color == 'white':                                 # check radar color and background color is the same
            print("Radar and Runway can't be the same color")
            continue                                            # go back and pick new runway color
        else:
            runway_c = runway_color_list[1]                     # white color
            break
    elif runway_color == "3" or runway_color == "pink":
        runway_c = runway_color_list[2]                         # pink color
        break
    elif runway_color == "4" or runway_color == "orange":
        runway_c = runway_color_list[3]                         # orange color
        break
    else:                                                       # check user input is not in 4 choices
        print("Pick only 1.Black or 2.White or 3.Pink or 4.Orange")
        continue                                                # go back and pick new runway color

# GUI receive input from player to pick radar sweep speed 1-3 (slow-fast)
while True:
    sweep = radar.textinput("Plane Landing Game", "Pick Radar sweep speed (1-3)")
    if sweep == '1':
        radar_sweep = 50       # sweep every 50 millisecond
        break
    elif sweep == '2':
        radar_sweep = 30       # sweep every 30 millisecond
        break
    elif sweep == '3':
        radar_sweep = 0.01     # sweep every 0.01 millisecond
        break
    else:                      # check user input is not 1 or 2 or 3
        print("Wrong Level")
        continue               # go back and pick new speed

# setup turtle
text = Turtle()
text.hideturtle()
text.speed("fastest")
text.pencolor('green')
text.screen.bgcolor(bg_color)   # set background color by user input
draw_radar()


# draw runway with random position, random heading, and random length
pos = Coordinate(random.randint(-400, 400),random.randint(-400, 400))
heading = random.randint(0, 360)
length = random.randint(100,300)
runway = Runway(pos=pos, heading=heading, width=25, length=length, color=runway_c)
runway.draw()


# initialize plane bot with callsign, random start position, and random heading
for i in range(10):
    pos = Coordinate(random.randint(-400, 400),random.randint(-400, 400))
    heading = random.randint(0, 360)
    bot = Plane(callsign=name[i], heading=heading, pos=pos)  # bot's default color is green
    bot_list.append(bot)         # put plane object in list
    bot.goto_start_position()    # set bot to start position

# initialize player's plane with random heading and random position
pos = Coordinate(random.randint(-400, 400),random.randint(-400, 400))
heading = random.randint(0, 360)
p = Plane(callsign='Player', heading=heading, pos=pos, color='blue')
p.goto_start_position()         # set player's plane to start position

# runway's ils data
pos_x, pos_y, top, bot, left, right, ils_heading, max_head, min_head, ils_length = runway.ils_data()

# main game
while True:
    x, y = p.show_pos()                  # x is x-coordinate of player's plane, y is y-coordinate of player's plane
    for plane in bot_list:               # get each bot plane object
        plane.forward(10)                # set bot plane speed
        plane.flight_data(time.ctime())  # save flight data by time in real world
        plane.show_flightdata()          # show text flight data of each bot plane
        # create hit box away from itself 12 distance
        plane_top, plane_bot, plane_left, plane_right = plane.position_data(12)
        # create hit box away from itself 80 distance
        warning_top, warning_bot, warning_left, warning_right = plane.position_data(80)

        # check player's plane collision with bot plane
        if y <= plane_top and y >= plane_bot and x <= plane_right and x >= plane_left:
            text.goto(300, 300)
            text.pendown()
            text.color('red')
            text.write("Planes Crashed! Please Investigate", align='center', font=('Arial', 20, 'bold'))
            time.sleep(1)
            investigation()
        # check player's plane is close to bot plane
        if y <= warning_top and y >= warning_bot and x <= warning_right and x >= warning_left:
            plane.close_call()      # change color of bot plane to red
            p.close_call()          # change color of player's plane to red
        else:
            plane.normal_state('green')
            p.normal_state('blue')

    p.forward(13)                     # set player's plane speed
    p.flight_data(time.ctime())       # save player's plane flight data by time in real world
    p.show_flightdata()               # show text flight data of player's plane
    plane_heading = p.show_heading()
    radar.listen()                    # listen for user keyboard input
    radar.delay(radar_sweep)          # radar sweep (screen delay by given millisecond)

    # check player's plane capture the runway's localizer
    if y < top and y > bot and x < right and x > left and plane_heading > min_head and plane_heading < max_head:
        print("Capture the localizer")
        for plane in bot_list:
            plane.clear()                                        # clear bot flight data text on the screen
            plane.hide()                                         # hide bot plane
        p.clear()                                                # clear player's flight data text on the screen
        p.approach(pos_x, pos_y, ils_heading, ils_length)        # player's plane approach to the runway
        text.goto(300, 300)
        text.pendown()
        text.color('green')
        text.write("Landing Completed ✈️", align='center', font=('Arial', 30, 'bold'))
        time.sleep(1)
        investigation()

    # check player's plane capture the runway's localizer but in wrong heading
    elif y < top and y > bot and x < right and x > left:
        print("Missed the localizer")

    if KeyboardInterrupt:
        radar.onkey(fun=p.left, key='Left')     # press left arrow on keyboard to turn left player's plane
        radar.onkey(fun=p.right, key='Right')   # press right arrow on keyboard to turn right player's plane
        continue



