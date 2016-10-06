import time

i=0
begin_time=time.clock()


while "c":
    i+=1
    over_time=time.clock()
    
    print ("I love   "+str(i)+"  "+str(i/over_time))
