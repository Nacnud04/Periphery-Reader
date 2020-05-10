import csv
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
#f'{row[0]}'
import os
x = 0
y = 0
z = 0
h = 0
i = 0
for i in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11) :
   with open('/home/pi/Desktop/mineProj/locationData/A-' + str(i) + '.csv', 'r') as csv_file:# open in readonly mode
       i = i + 1
       csv_reader = csv.reader(csv_file, delimiter=',')
       line_count = 0
       for row in csv_reader:
           if line_count == 0:
               line_count += 1
           elif line_count == 1:
               print(f'{row[0]}' + ', ' + f'{row[1]}' + ', ' + f'{row[2]}')
               with open('/home/pi/Desktop/mineProj/locationData/top/SurveyStations.csv', 'a+') as csv_filetemp:
                   csv_writer = csv.writer(csv_filetemp, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                   csv_writer.writerow([f'{row[0]}', f'{row[1]}', f'{row[2]}'])
               line_count += 1
           else:
               line_count += 1
with open('/home/pi/Desktop/mineProj/locationData/top/SurveyStations.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader :
        angle = float(f'{row[0]}')
        print(angle)
        print(x)
        x = float(f'{row[2]}') * math.cos(angle * (math.pi / 180)) + x
        z = float(f'{row[2]}') * math.sin(angle * (math.pi / 180)) + z
        with open('/home/pi/Desktop/mineProj/locationData/top/SurveyStations_d.csv', 'a+') as csv_filetemp:
            csv_writer = csv.writer(csv_filetemp, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            if h == 0 :
                csv_writer.writerow([0, 0])
                h = 1
            csv_writer.writerow([x, z])
        line_count += 1
os.remove('/home/pi/Desktop/mineProj/locationData/top/SurveyStations.csv')
with open('/home/pi/Desktop/mineProj/locationData/top/SurveyStations_d.csv') as f, open('/home/pi/Desktop/mineProj/locationData/top/SurveyStations_d2.csv', 'w') as fw: 
    csv.writer(fw, delimiter=',').writerows(zip(*csv.reader(f, delimiter=',')))
with open('/home/pi/Desktop/mineProj/locationData/top/SurveyStations_d2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader :
        if line_count == 0:
            x = row
            line_count += 1
        elif line_count == 1:
            z = row
            line_count += 1
os.remove('/home/pi/Desktop/mineProj/locationData/top/SurveyStations_d2.csv')
x = list(map(float, x))
z = list(map(float, z))
h = 0
i = 0
for i in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11) :
   with open('/home/pi/Desktop/mineProj/locationData/A-' + str(i) + '.csv', 'r') as csv_file:# open in readonly mode
       i = i + 1
       csv_reader = csv.reader(csv_file, delimiter=',')
       line_count = 0
       for row in csv_reader:
           if line_count == 0:
               line_count += 1
           elif line_count == 1:
               print(f'{row[0]}' + ', ' + f'{row[1]}' + ', ' + f'{row[2]}')
               with open('/home/pi/Desktop/mineProj/locationData/side/SurveyStations.csv', 'a+') as csv_filetemp:
                   csv_writer = csv.writer(csv_filetemp, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                   csv_writer.writerow([f'{row[0]}', f'{row[1]}', f'{row[2]}'])
               line_count += 1
           else:
               line_count += 1
with open('/home/pi/Desktop/mineProj/locationData/side/SurveyStations.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader :
        angle = float(f'{row[1]}')
        print(angle)
        print(y)
        y = float(f'{row[2]}') * math.sin(angle * (math.pi / 180)) + y
        with open('/home/pi/Desktop/mineProj/locationData/side/SurveyStations_d.csv', 'a+') as csv_filetemp:
            csv_writer = csv.writer(csv_filetemp, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            if h == 0 :
                csv_writer.writerow([0, 0])
                h = 1
            csv_writer.writerow([0, y])
        line_count += 1
os.remove('/home/pi/Desktop/mineProj/locationData/side/SurveyStations.csv')
with open('/home/pi/Desktop/mineProj/locationData/side/SurveyStations_d.csv') as f, open('/home/pi/Desktop/mineProj/locationData/side/SurveyStations_d2.csv', 'w') as fw: 
    csv.writer(fw, delimiter=',').writerows(zip(*csv.reader(f, delimiter=',')))
with open('/home/pi/Desktop/mineProj/locationData/side/SurveyStations_d2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader :
        if line_count == 0:
            line_count += 1
        elif line_count == 1:
            y = row
            line_count += 1
os.remove('/home/pi/Desktop/mineProj/locationData/side/SurveyStations_d2.csv')
os.remove('/home/pi/Desktop/mineProj/locationData/side/SurveyStations_d.csv')
os.remove('/home/pi/Desktop/mineProj/locationData/top/SurveyStations_d.csv')
y = list(map(float, y))
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
fig = plt.figure()
ax = plt.axes(projection='3d')
print(z)
print(y)
print(x)
ax.set_ylabel('1 Unit : 1 Foot')
ax.set_zlabel('North (+)')
ax.set_xlabel('Up (+)')
ax.scatter(y, z, x, marker = 's', color = 'grey')
ax.scatter(y, z, x, marker = 'x', color = 'black')
ax.plot3D(y, z, x, 'gray')
plt.show()