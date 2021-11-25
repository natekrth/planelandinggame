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
name = ['TG', 'AA', "KLM", "AF", "QF", "BA", "JL", "QR", "MH", "EY"]
radar = Screen()
radar.setup(1000,1000)
radar.title("Plane Landing Game")
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
database = FlightDB("test")
text = Turtle()
text.hideturtle()
text.screen.bgcolor('black')
text.speed("fastest")
text.pencolor('green')
draw_radar()


# draw runway
pos = Coordinate(random.randint(-400, 400),random.randint(-400, 400))
heading = random.randint(0, 360)
length = random.randint(100,300)
runway = Runway(pos=pos, heading=heading, width=25, length=length)
runway.draw()


# init plane bot
for i in range(10): # int(ask)
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
            text.write("Plane Crash! Please Investigate", align='center', font=('Arial', 20, 'bold'))
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



