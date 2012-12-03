#Variables used for Simulation
global newcount, count, Signaltape, newcount
newcount=0
count=0
Signaltape=[] # A List Data Structure for holding 'Signal' objects


#Function used to manipulate count variables which determines read indices[Bugged]	
def updatecount():
  global count
  global newcount
  newlocalcount=0
  for i in Signaltape:
    newlocalcount = newlocalcount+1
  if newcount < newlocalcount:
    global count, newcount, newlocalcount
    print("Increased Dump in Signalstack...refreshing count parameters")
    count=newcount
    newcount = newlocalcount
  else:
    global count, newcount, newlocalcount
    if (newcount == newlocalcount):
      print("No change in Stack...")
      
  print "newcount :"+str(newcount)
  print "count :" +str(count)
  a=raw_input()
  if( newcount > count):
    global newcount
    global count
    return (newcount-count)
  else:
    return 0