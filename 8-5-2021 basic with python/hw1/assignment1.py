# Name: Phasit Sangklub
# ID: 6201012610061
# Assignment 1 : Read, write and, plot
# ====================================

import csv
from matplotlib.pyplot import plot,ylabel,show,xlabel,grid
from math import sqrt

class Point2:
    def __init__(self,x,y):
        self._x = x
        self._y = y

    def get_distance(self,other):
        return sqrt(pow(self._x - other._x,2) + pow(self._y - other._y,2))

    def __add__(self,other):
        return Point2(self._x + other._x,self._y + other._y)
    
    def __sub__(self,other):
        return Point2(self._x - other._x,self._y - other._y)
    
    def __str__(self) -> str:
        return "Position (x,y) : (" + str(self._x) + "," +str(self._y) + ")"

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,value):
        self._x = value 

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self,value):
        self._y = value 

if __name__ == "__main__" :

    # Read csv data
    ws_path ='/'.join( __file__.split('/')[:-1]) + "/"
    csv_read_filename = "data.csv"
    with open(ws_path+csv_read_filename) as csvfile:
        csv_reader = csv.reader(csvfile)
        header_list = next(csv_reader)
        csv_data = [[int(data[0]), int(data[1]),int(data[2])] for data in csv_reader]
    
    # Calculate distance value
    point_arr = [None] * len(csv_data)
    x_arr = [None] * len(csv_data)
    y_arr = [None] * len(csv_data)
    dist_arr = [None] * len(csv_data)
    dist_sum = 0
    for index,point_data in enumerate(csv_data):
        obj = Point2(point_data[1],point_data[2])
        point_arr[index] = obj
        x_arr[index] = obj.x
        y_arr[index] = obj.y
        if index == 0 :
            dist = 0
        else:
            dist = point_arr[index].get_distance(point_arr[index-1])
        dist = round(dist,3)
        dist_sum += dist
        dist_arr[index] = dist


    # Print output to terminal
    print("point\tx\ty\tdistance")
    for index,point_data in enumerate(point_arr):
        print(str(index) + "\t" + str(point_data.x) + "\t" + str(point_data.y) + "\t" + str(dist_arr[index]))
    print("\t\tTotal\t"+ str(dist_sum))

    # Append distance header and data to array
    header_list.append("distance")
    [dataline.append(dist_arr[index]) for index,dataline in enumerate(csv_data)]
   
    #write csv file
    csv_write_filename = "goal.csv"
    with open(ws_path+ csv_write_filename, 'w') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(header_list)
        for writeline in csv_data:
            csv_writer.writerow(writeline)


    #visualization in matplotlib
    plot(x_arr,y_arr)
    grid()
    ylabel('Y axis')
    xlabel('X axis')
    show()
    


    




