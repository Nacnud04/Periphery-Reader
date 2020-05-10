import csv
import matplotlib.pyplot as plt
import math

with open('locationData.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 3:
            print(f'{row[0]} ' + f'{row[1]} ' + f'{row[2]} ' + f'{row[3]} ' + f'{row[4]} ' + f'{row[5]} ' + f'{row[6]} ' + f'{row[7]} ' + f'{row[8]}')
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
            x = [one, twox, threex, fourx, fivex, sixx, sevenx, eightx, 0, tenx, elevenx, twelvex, thirteenx, fourteenx, fifteenx, sixteenx, seventeen]
            y = [0, twoy, threey, foury, fivey, sixy, seveny, eighty, nine, teny, eleveny, twelvey, thirteeny, fourteeny, fifteeny, sixteeny, 0]
            plt.plot(x, y)
            print(x)
            print(y)
            plt.xlabel('x-axis')
            plt.ylabel('y-axis')
            plt.title('test graph')
            plt.show()
        line_count += 1
    print(f'Processed {line_count} lines.')