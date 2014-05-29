#!/opt/python3/bin/python3


file1="james.txt"
file2="julie.txt"
file3="sarah.txt"
file4="mikey.txt"

filelist=[]
filelist.append(file1)
filelist.append(file2)
filelist.append(file3)
filelist.append(file4)

#filelist=[file1,file2]
print (filelist)

#for file in filelist:

def sanitize(time_string):
    print ("\nDebug time_string",time_string)
    if '-' in time_string:
        splitter='-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins,secs) = time_string.split(splitter)
    return (mins+'.'+secs)



    
def main():
    try:
        with open('james.txt','r') as jaf:
            data=jaf.readline()
        james=data.strip().split(',')
    
        with open('julie.txt','r') as juf:
            data=juf.readline()
        julie=data.strip().split(',')
    
        with open('mikey.txt') as mif:
            data=mif.readline()
        mikey=data.strip().split(',')
    
        with open('sarah.txt') as saf:
            data=saf.readline()
        sarah=data.strip().split(',')
    
    except  IOError as  err:
        print ('Could not open file: ' + str(err))
    
    
    
    clean_james=[]
    clean_julie=[]
    clean_mikey=[]
    clean_sarah=[]
    
    
    
    sanitize('3.41')
    
    for mytime in james:
       print ("\n%s" ,mytime)
       mynewtime = sanitize(mytime)
    
    
    
    

if __name__ == "__main__":
    main()
