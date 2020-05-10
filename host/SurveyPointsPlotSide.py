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
for i in (0, 1, 2, 3) :
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
        print(x)
        x = float(f'{row[2]}') * math.cos(angle * (math.pi / 180)) + x
        y = float(f'{row[2]}') * math.sin(angle * (math.pi / 180)) + y
        with open('/home/pi/Desktop/mineProj/locationData/side/SurveyStations_d.csv', 'a+') as csv_filetemp:
            csv_writer = csv.writer(csv_filetemp, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            if h == 0 :
                csv_writer.writerow([0, 0])
                h = 1
            csv_writer.writerow([x, y])
        line_count += 1
os.remove('/home/pi/Desktop/mineProj/locationData/side/SurveyStations.csv')
with open('/home/pi/Desktop/mineProj/locationData/side/SurveyStations_d.csv') as f, open('/home/pi/Desktop/mineProj/locationData/side/SurveyStations_d2.csv', 'w') as fw: 
    csv.writer(fw, delimiter=',').writerows(zip(*csv.reader(f, delimiter=',')))
with open('/home/pi/Desktop/mineProj/locationData/side/SurveyStations_d2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader :
        if line_count == 0:
            x = row
            line_count += 1
        elif line_count == 1:
            y = row
            line_count += 1
os.remove('/home/pi/Desktop/mineProj/locationData/side/SurveyStations_d2.csv')
x = list(map(float, x))
y = list(map(float, y))
print(x)
print(y)
plt.plot(x, y)
plt.plot(x, y, color='grey', marker='s', linestyle='', linewidth=2, markersize=6)
plt.plot(x, y, color='black', marker='x', linestyle='', linewidth=2, markersize=6)
plt.xlabel('1 unit = 1 foot')
plt.ylabel('Up âŸ¶')
plt.title('Side View')
os.remove('/home/pi/Desktop/mineProj/locationData/side/SurveyStations_d.csv')
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='lightblue')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
plt.axes().set_aspect('equal', 'datalim')
plt.show()
print(f'Processed {line_count} lines.')