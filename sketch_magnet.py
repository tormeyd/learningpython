#!/opt/python3/bin/python3
from __future__ import print_function


try:
    data = open ('sketch.txt')

    man = []
    other = []
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':',1)
            line_spoken=line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
            
        except ValueError:
            pass
    


    data.close()
except IOError:
    print ("datafile does not exist")

try:
   manout =  open('man_data.txt',"w")
   otherout =  open('other_data.txt',"w")

   print (man,file=manout)
   print (other,file=otherout)

except IOError as err:
   print ("File error: " +str(err)) 

finally:
   if 'manout' in locals():
       manout.close()
   if 'otherout' in locals():
       otherout.close()

   
