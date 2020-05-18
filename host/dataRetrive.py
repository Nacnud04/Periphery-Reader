#!/usr/bin/env python
import serial
import csv
from statistics import mean

azumith = [180]
ally = [0]
finy = 0.0
try :
    ser = serial.Serial('/dev/ttyACM0',9600)
    print("Establishing Serial on /dev/ttyACM0...")
except :
    try :
        ser = serial.Serial('/dev/ttyACM1',9600)
        print("Establishing Serial on /dev/ttyACM1...")
    except :
        print("No microcontroller found.")
ser.close()
ser.open()

def yValToDeg():
    global finy
    finy = 90 * (mean(ally) / (-1500))
    print(finy)
    
while True:
    data = ser.readline()
    print(data)
    if data == b'StatName:\r\n' :
        data = ser.readline()
        print(data.decode())
        open(str(data.decode("utf-8")) + '.csv', 'w+')
        file = str(data.decode("utf-8")) + '.csv'
        file = file.rstrip()
    elif data == b'Distance:\r\n' :
        data = ser.readline()
        print(data.decode("utf-8"))
        distance = float(data.decode("utf-8"))
    elif data == b'Angles:\r\n' :
        with open(file, 'w+') as output_file:
            i = 1
            azumith = [180]
            ally = [0]
            while i <= 150 :
                data = ser.readline()
                values = data.decode("utf-8")
                x, y, z, a = values.split(',')
                discard, a = a.split(':')
                discard, y = y.split(':')
                azumith.append(int(a))
                azumith.insert(0, int(a))
                ally.append(int(y))
                #ally.insert(0, int())
                print(values)
                i += 1
            print(azumith)
            print(mean(azumith))
            print(ally)
            yValToDeg()
            csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(['Angle From North',    'Angle From Horiz.',    'Distance'])
            csv_writer.writerow([mean(azumith), finy, distance])
    elif data == b'Data\r\n' :
        i = 1
        with open(file, 'a+') as output_file:
            csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(['Map'])
            data = ser.readline()
            print(data.decode("utf-8"))
            datapoints = [int(data.decode("utf-8"))]
            while i <= 16 :
                data = ser.readline()
                print(data.decode("utf-8"))
                datapoints.append(int(data.decode("utf-8")))
                i += 1
            csv_writer.writerow(datapoints)
    elif data == b'Rewrite\r\n' :
        print('Beginning rewrite...') 
        with open(file, 'r') as read_file:
            reader = csv.reader(read_file)
            for row in reader :
                if line_count == 0 :
                    row0 = row
                elif line_count == 1 :
                    row1 = row
        with open(file, 'w+') as new_file:
            rewrite = csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csvwriter.writerow(row0)
            csvWriter.writerow(row1)
        print('Finished rewrite.')
    elif data == b'Temp + Humid\r\n' :
        data = ser.readline()
        print(data.decode("utf-8"))
        temp = data.decode("utf-8")
        data = ser.readline()
        print(data.decode("utf-8"))
        humid = data.decode("utf-8")
        temp = temp.rstrip()
        humid = humid.rstrip()
        with open(file, 'a+') as output_file:
            csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(['Temperature', 'Humidity'])
            csv_writer.writerow([temp, humid])
