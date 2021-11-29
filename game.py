from turtle import Turtle, Screen
from plane import Plane
from coordinate import Coordinate
from runway import Runway
from blackbox import BlackBox
from database import FlightDB
import time
import random

def investigation():
    while True:
        investigate = radar.textinput("Plane Landing Game",
                                      "Investigate!(type 'all'/callsign of the plane/exit)")  # เขียนเป็น gui ให้ดู blackbox
        if investigate in name:
            print("Player's blackbox")
            database.search('Player')
            print(investigate + "'s blackbox")
            database.search(investigate)
            print("")
        elif investigate == 'all':
            database.search('Player')
            print("Player's blackbox")
            for m in range(10):
                print(name[m] + "'s blackbox")
                database.search(name[m])
                print("")
        elif investigate == 'exit':
            print("Thank you for playing")
            time.sleep(3)
            exit()
        else:
            continue

def draw_radar():
    radius = 100
    text.forward(500)
    text.backward(1000)
    text.forward(500)
    text.left(90)
    text.forward(500)
    text.backward(1000)
    text.right(90)
    text.penup()
    text.goto(0, 0)
    text.pendown()
    for i in range(5):
        text.goto(0, -radius)
        text.circle(radius)
        radius += 100
    text.penup()

plane_list = []
runway_color_list = ['black', 'white', 'pink', 'orange']
name = ['TG', 'AA', "KLM", "AF", "QF", "BA", "JL", "QR", "MH", "EY"]
radar = Screen()
radar.setup(1000,1000)
radar.title("Plane Landing Game")

database = FlightDB("test")
text = Turtle()
text.hideturtle()

bg_color = ''
runway_c = ''
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

while True:
    question = "Pick Runway Color 1.Black/2.White/3.Pink/4.Orange (1-3)"
    runway_color = radar.textinput("Plane Landing Game", question).lower()
    if runway_color == "1" or runway_color == "black":
        if bg_color == 'black':
            print("Radar and Runway can't be the same color")
            continue
        else:
            runway_c = runway_color_list[0]
            break
    elif runway_color == "2" or runway_color == "white":
        if bg_color == 'white':
            print("Radar and Runway can't be the same color")
            continue
        else:
            runway_c = runway_color_list[1]
            break
    elif runway_color == "3" or runway_color == "pink":
        runway_c = runway_color_list[2]
        break
    elif runway_color == "4" or runway_color == "orange":
        runway_c = runway_color_list[3]
        break
    else:
        print("Pick only 1.Black or 2.White or 3.Pink or 4.Orange")
        continue

while True:
    sweep = radar.textinput("Plane Landing Game", "Pick Radar sweep speed 1-3")
    if sweep == '1':
        radar_sweep = 50
        break
    elif sweep == '2':
        radar_sweep = 30
        break
    elif sweep == '3':
        radar_sweep = 0.01
        break
    else:
        print("Wrong Level")
        continue

text.screen.bgcolor(bg_color)
text.speed("fastest")
text.pencolor('green')
draw_radar()


# draw runway
pos = Coordinate(random.randint(-400, 400),random.randint(-400, 400))
heading = random.randint(0, 360)
length = random.randint(100,300)
runway = Runway(pos=pos, heading=heading, width=25, length=length, color=runway_c)
runway.draw()


# init plane bot
for i in range(10):
    pos = Coordinate(random.randint(-400, 400),random.randint(-400, 400))
    heading = random.randint(0, 360)
    bot = Plane(callsign=name[i], heading=heading, pos=pos)
    plane_list.append(bot)
    bot.goto_start_position()

# player plane
callsign = random.choice(name)
pos = Coordinate(random.randint(-400, 400),random.randint(-400, 400))
heading = random.randint(0, 360)
p = Plane(callsign='Player', heading=heading, pos=pos, color='blue')
p.goto_start_position()


pos_x, pos_y, top, bot, left, right, ils_heading, max_head, min_head, ils_length = runway.ils_data()

while True:
    x, y = p.show_pos()
    for plane in plane_list:
        plane.forward(10)
        plane.flight_data(time.ctime())
        plane.text()
        plane_top, plane_bot, plane_left, plane_right = plane.position_data(12)
        warning_top, warning_bot, warning_left, warning_right = plane.position_data(80)
        if y <= plane_top and y >= plane_bot and x <= plane_right and x >= plane_left:
            text.goto(300, 300)
            text.pendown()
            text.color('red')
            text.write("Planes Crashed! Please Investigate", align='center', font=('Arial', 20, 'bold'))
            time.sleep(1)
            investigation()

        if y <= warning_top and y >= warning_bot and x <= warning_right and x >= warning_left:
            plane.close_call()
            p.close_call()
        else:
            plane.normal_state('green')
            p.normal_state('blue')

    p.forward(13)
    p.flight_data(time.ctime())
    p.text()
    plane_heading = p.show_heading()
    radar.listen()
    radar.delay(radar_sweep)

    if y < top and y > bot and x < right and x > left and plane_heading > min_head and plane_heading < max_head:
        print("Capture the localizer")
        for plane in plane_list:
            plane.clear()
            plane.hide()
        p.clear()
        p.approach(pos_x, pos_y, ils_heading, ils_length)
        text.goto(300, 300)
        text.pendown()
        text.color('green')
        text.write("Landing Completed ✈️", align='center', font=('Arial', 30, 'bold'))
        time.sleep(1)
        investigation()

    elif y < top and y > bot and x < right and x > left:
        print("Missed the localizer")

    if KeyboardInterrupt:
        radar.onkey(fun=p.left, key='Left')
        radar.onkey(fun=p.right, key='Right')
        continue



