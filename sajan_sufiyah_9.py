# Sufiyah Sajan
# Dictionaries

# Part 1

import urllib.request

urls = {
    "New York": "https://w1.weather.gov/xml/current_obs/KLGA.xml",
    "Texas": "https://w1.weather.gov/xml/current_obs/KATT.xml",
    "Hawaii": "https://w1.weather.gov/xml/current_obs/PHSF.xml",
    "California": "https://w1.weather.gov/xml/current_obs/KBIH.xml"
   } 

print("Your Weather Report")
print()
print("Current observations are available for:")
for location in urls.keys():
    print('- %s' % location)
print()

city = input("Enter the city you would like a weather report for: ")
while city not in urls.keys():
    city = input("No data available. Please try another city: ")

print("Accessing weather data . . .")
print()
    
try:
    response = urllib.request.urlopen(urls[city])
    data = response.read().decode('utf-8')
    #lines = data.split('\n')
    #print(lines)
except IOError:
    print("File cannot be found.")
else:
    print("The current weather has been accessed for ", city)

# Part 2
import xml.etree.ElementTree as ET
print()

if data:
    weather_xml = ET.XML(data)

try:
    info = {
        "location": weather_xml.find('location').text,
        "weather": weather_xml.find('weather').text,
        "temperature": weather_xml.find('temp_f').text,
        "humidity": weather_xml.find('relative_humidity').text,
        "wind": [weather_xml.find('wind_dir').text, weather_xml.find('wind_mph').text, weather_xml.find('wind_kt').text],
        "observation": weather_xml.find('observation_time').text
    }
except AttributeError:
    print('Error parsing one or more attributes from the XML data.')
    print()
    
# Part 3
if info:
    print("Information available:")
    for availableinfo in info.keys():
        print('- %s' % availableinfo)
    print()
    infoinput = input('What weather information would you like? ')
    
    while infoinput not in info.keys():
        print('That data is not available.')
        infoinput = input('What weather information would you like? ')
        
    while infoinput != 'done':
        if infoinput == 'location':
            print('This weather report is for %s' % info['location'])
            print()
        elif infoinput == 'weather':
            print('It is %s in %s' % (info['weather'], info['location']))
            print()
        elif infoinput == 'temperature':
            print('The temperature in %s is %s degrees F' % (info['location'], info['temperature']))
            print()
        elif infoinput == 'humidity':
            print('The humidity in %s is %s%%' % (info['location'], info['humidity']))
            print()
        elif infoinput == 'wind':
            print('The wind in %s is %s at %s MPH (%s KT)' % (info['location'], info['wind'][0], info['wind'][1], info['wind'][2]))
            print()
        elif infoinput == 'observation':
            print('The weather observation in %s was %s' % (info['location'], info['observation']))
            print()
        elif infoinput != 'done':
            print('That data is not available.')
            print()
        infoinput = input('What weather information would you like?  Or, to end, enter "done" ')
        
# Part 4
print()
exporting = input("Would you like to export the weather report and generate a data visualization? (yes/no) ")
if exporting == 'yes':
    report = """
- Location: {location}
- Weather: {weather}
- Humidity: {humidity}
- Temperature: {temperature}
- Wind:
    - Direction: {wind[0]}
    - Speed (MPH): {wind[1]}
    - Speed (KT): {wind[2]}
 - Observation: {observation}""".format(**info)
    file = open("full_weather_report.txt", "w")
    file.write("Weather for ")
    file.write(city)
    file.write('\n')
    file.write(report)
    print("The full weather report has been exported, generating your visualization . . .")
    file.close()

import turtle

screen = turtle.Screen()
screen.setup(500,500)

#Grey background represents temperature below 70 F
if float(info['temperature']) <= 70.0:
    screen.bgcolor("grey")
#Blue background represents temperature above 70 F
if float(info['temperature']) > 70.0:
    screen.bgcolor("light blue")
    
t = turtle.Turtle()

t.penup()
t.goto(100,-100)
t.pencolor("yellow")
t.pensize(7)
t.pendown()
t.begin_fill()
t.circle(90)
t.penup()
t.fillcolor("yellow")
t.end_fill()
t.penup()

#white circles represent level of wind speed.
#The more and larger the white circles are means higher wind speed MPH
if float(info['wind'][1]) < 8:
    t.goto(-150,0)
    t.pencolor("white")
    t.pensize(10)
    t.pendown()
    t.circle(20)
    t.penup()
    t.goto(20,-30)
    t.pendown()
    t.circle(20)
    t.penup()
elif float(info['wind'][1]) >= 8 and float(info['wind'][1]) <= 20:
    t.goto(-150,0)
    t.pencolor("white")
    t.pensize(10)
    t.pendown()
    t.circle(30)
    t.penup()
    t.goto(20,-30)
    t.pendown()
    t.circle(30)
    t.penup()
    t.goto(200,-60)
    t.pendown()
    t.circle(30)
    t.penup()
    t.goto(90,100)
    t.pendown()
    t.circle(30)
elif float(info['wind'][1]) >= 21:
    t.goto(-150,0)
    t.pencolor("white")
    t.pensize(10)
    t.pendown()
    t.circle(40)
    t.penup()
    t.goto(20,-30)
    t.pendown()
    t.circle(40)
    t.penup()
    t.goto(200,-60)
    t.pendown()
    t.circle(40)
    t.penup()
    t.goto(90,100)
    t.pendown()
    t.circle(40)
    t.penup()
    t.goto(20,90)
    t.pendown()
    t.circle(40)
    t.penup()
    t.goto(110,180)
    t.pendown()
    t.circle(40)




