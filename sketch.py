#!/opt/python3/bin/python3
from __future__ import print_function


try:
    data = open ('sketch.txt')

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':',1)
            print (role, end='')
            print (' said: ',end='')
            print (line_spoken)
        except ValueError:
            print ("\nException !!!!!!!!")
    

    data.close()
except IOError:
    print ("datafile does not exist")
