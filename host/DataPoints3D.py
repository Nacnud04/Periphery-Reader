import csv
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
import os
x = [0.0]
y = [0.0]
z = [0.0]
h = 0
i = 0
j = 0
xstation = 0
ystation = 0
zstation = 0
angle = 90
for i in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11) :
    with open('/home/pi/Desktop/mineProj/locationData/A-' + str(i) + '.csv', 'r') as csv_file:# open in readonly mode
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
            angle1 = float(f'{row[0]}')
            print(angle1)
            print(xstation)
            xstation = float(f'{row[2]}') * math.cos(angle1 * (math.pi / 180)) + xstation
            zstation = float(f'{row[2]}') * math.sin(angle1 * (math.pi / 180)) + zstation
            with open('/home/pi/Desktop/mineProj/locationData/top/SurveyStations_d.csv', 'a+') as csv_filetemp:
                csv_writer = csv.writer(csv_filetemp, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                if h == 0 :
                    csv_writer.writerow([0, 0])
                    h = 1
                csv_writer.writerow([xstation, zstation])
            line_count += 1
    os.remove('/home/pi/Desktop/mineProj/locationData/top/SurveyStations.csv')
    with open('/home/pi/Desktop/mineProj/locationData/top/SurveyStations_d.csv') as f, open('/home/pi/Desktop/mineProj/locationData/top/SurveyStations_d2.csv', 'w') as fw: 
        csv.writer(fw, delimiter=',').writerows(zip(*csv.reader(f, delimiter=',')))
    with open('/home/pi/Desktop/mineProj/locationData/top/SurveyStations_d2.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader :
            if line_count == 0:
                xstation1 = float(f'{row[0]}')
                try :
                    xstation2 = float(f'{row[1]}')
                    line_count += 1
                except :
                    line_count += 1
            elif line_count == 1:
                zstation1 = float(f'{row[0]}')
                try :
                    zstation2 = float(f'{row[1]}')
                    line_count += 1
                except :
                    line_count += 1
    os.remove('/home/pi/Desktop/mineProj/locationData/top/SurveyStations_d2.csv')
    h = 0
    with open('/home/pi/Desktop/mineProj/locationData/A-' + str(i) + '.csv', 'r') as csv_file:# open in readonly mode
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
            angle2 = float(f'{row[1]}')
            print(angle2)
            print(ystation)
            ystation = float(f'{row[2]}') * math.sin(angle2 * (math.pi / 180)) + ystation
            with open('/home/pi/Desktop/mineProj/locationData/side/SurveyStations_d.csv', 'a+') as csv_filetemp:
                csv_writer = csv.writer(csv_filetemp, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                if h == 0 :
                    csv_writer.writerow([0, 0])
                    h = 1
                csv_writer.writerow([0, ystation])
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
                ystation1 = float(f'{row[0]}')
                try :
                    ystation2 = float(f'{row[1]}')
                    line_count += 1
                except :
                    line_count += 1
    os.remove('/home/pi/Desktop/mineProj/locationData/side/SurveyStations_d2.csv')
    os.remove('/home/pi/Desktop/mineProj/locationData/side/SurveyStations_d.csv')
    os.remove('/home/pi/Desktop/mineProj/locationData/top/SurveyStations_d.csv')
    t = 0
    xpoint = [0.0]
    ypoint = [0.0]
    with open('/home/pi/Desktop/mineProj/locationData/A-' + str(i) + '.csv', 'r') as csv_file:# open in readonly mode
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            elif line_count == 3:
                print(row)
                with open('/home/pi/Desktop/mineProj/locationData/top/points.csv', 'a+') as csv_filetemp:
                    csv_writer = csv.writer(csv_filetemp, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    one = int(f'{row[0]}')
                    twox = int(f'{row[1]}') * math.cos(math.pi/16)
                    twoy = int(f'{row[1]}') * math.sin(math.pi/16)
                    threex = int(f'{row[2]}') * math.cos(math.pi/8)
                    threey = int(f'{row[2]}') * math.sin(math.pi/8)
                    fourx = int(f'{row[3]}') * math.cos(3*math.pi/16)
                    foury = int(f'{row[3]}') * math.sin(3*math.pi/16)
                    fivex = int(f'{row[4]}') * math.cos(math.pi/4)
                    fivey = int(f'{row[4]}') * math.sin(math.pi/4)
                    sixx = int(f'{row[5]}') * math.cos(5*math.pi/16)
                    sixy = int(f'{row[5]}') * math.sin(5*math.pi/16)
                    sevenx = int(f'{row[6]}') * math.cos(3*math.pi/8)
                    seveny = int(f'{row[6]}') * math.sin(3*math.pi/8)
                    eightx = int(f'{row[7]}') * math.cos(7*math.pi/16)
                    eighty = int(f'{row[7]}') * math.sin(7*math.pi/16)
                    nine = int(f'{row[8]}')
                    tenx = int(f'{row[9]}') * math.cos(9*math.pi/16)
                    teny = int(f'{row[9]}') * math.sin(9*math.pi/16)
                    elevenx = int(f'{row[10]}') * math.cos(10*math.pi/16)
                    eleveny = int(f'{row[10]}') * math.sin(10*math.pi/16)
                    twelvex = int(f'{row[11]}') * math.cos(11*math.pi/16)
                    twelvey = int(f'{row[11]}') * math.sin(11*math.pi/16)
                    thirteenx = int(f'{row[12]}') * math.cos(12*math.pi/16)
                    thirteeny = int(f'{row[12]}') * math.sin(12*math.pi/16)
                    fourteenx = int(f'{row[13]}') * math.cos(13*math.pi/16)
                    fourteeny = int(f'{row[13]}') * math.sin(13*math.pi/16)
                    fifteenx = int(f'{row[14]}') * math.cos(14*math.pi/16)
                    fifteeny = int(f'{row[14]}') * math.sin(14*math.pi/16)
                    sixteenx = int(f'{row[15]}') * math.cos(15*math.pi/16)
                    sixteeny = int(f'{row[15]}') * math.sin(15*math.pi/16)
                    seventeen = -1 * int(f'{row[16]}')
                    xpoint = [one, twox, threex, fourx, fivex, sixx, sevenx, eightx, 0, tenx, elevenx, twelvex, thirteenx, fourteenx, fifteenx, sixteenx, seventeen]
                    ypoint = [0, twoy, threey, foury, fivey, sixy, seveny, eighty, nine, teny, eleveny, twelvey, thirteeny, fourteeny, fifteeny, sixteeny, 0]
                    zpoint = [one, twox, threex, fourx, fivex, sixx, sevenx, eightx, 0, tenx, elevenx, twelvex, thirteenx, fourteenx, fifteenx, sixteenx, seventeen]
                line_count += 1
            else:
                line_count += 1
    print(xstation)
    print(ystation)
    print(zstation)
    angle = angle1 + 90 
    print(angle1)
    print('angle1')
    print(angle)
    print('angle')
    if angle != 0 or angle != 180 :
        xpoint = [x * (math.cos(angle * math.pi / 180)) - 0 * (math.sin(angle * math.pi / -180)) for x in xpoint]
        zpoint = [z * (math.sin(angle * math.pi / 180)) for z in zpoint]
    else :
        zpoint = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    print('I-Value: ' + str(i))
    if j == 0 :
        xpoint = [x + float(xstation1) for x in xpoint]
        ypoint = [y + float(ystation1) for y in ypoint]
        zpoint = [z + float(zstation1) for z in zpoint]
        xstation = xstation2
        ystation = ystation2
        zstation = zstation2
        j += 1
    elif j >= 1 :
        xpoint = [x + float(xstation) for x in xpoint]
        ypoint = [y + float(ystation) for y in ypoint]
        zpoint = [z + float(zstation) for z in zpoint]
        xstation = xstation1
        ystation = ystation1
        zstation = zstation1
        j += 1
    print(xpoint)
    print(ypoint)
    x.extend(xpoint)
    y.extend(ypoint)
    z.extend(zpoint)
    print('Lengths: X,'+str(len(x))+' Y,'+str(len(y))+' Z,'+str(len(z)))
    print('PointLengths: X,'+str(len(xpoint))+' Y,'+str(len(ypoint))+' Z,'+str(len(zpoint)))
print(x)
print(y)
print(z)
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_ylabel('1 Unit : 1 Foot')
ax.set_zlabel('North (+)')
ax.set_xlabel('Up (+)')
ax.scatter(y, z, x, marker = 'o', color = "blue")
i = 1
while i <= len(y) - 17 :
    ax.plot(y[i:i+17], z[i:i+17], x[i:i+17], color = "black")
    i += 17
i = 1
while i <= len(y) / 8 :
    ax.plot(y[i::17], z[i::17], x[i::17], color = "black")
    i += 1
plt.show()