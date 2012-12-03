from inits import *
from classes import *    

JoeFriend = PersonChip(["001", "010"], ["001", "010", "011"], "AB00", "XYXZ", ("D00R"))
JoeDoor = Door(["001", "010", "011"], ["001", "010", "100", "101"], "D00R", "ZZZZ", ("AB00"))
JoeClock = Clock(["100"], ["101"], "CL88", "XXXX")
JoeComputer = JoePC(['001', '101'], ['001', '010'], "AB10", "YYYY" )  
sig = Signal("AB00", "D00R", '001')

def trigger():
  global JoeFriend, JoeDoor, JoeClock, JoeComputer, newcount
  print(dir(JoeFriend))
  global sig
  global Signaltape
  Signaltape.append(sig)
  for i in Signaltape:
    global newcount
    newcount=newcount+1
  def displaySignaltape():
    global Signaltape
    for i in Signaltape:
      print "[Issuer: "+str(i.issuer)+"Target: "+str(i.target)+" String: "+str(i.signalString)+ " ]"
  displaySignaltape()



  def routine(): 
      global JoeFriend, JoeDoor, JoeClock, JoeComputer
      JoeFriend.pick_signal()
      displaySignaltape()
      JoeDoor.pick_signal()
      displaySignaltape()
      JoeClock.pick_signal()
      displaySignaltape()
      JoeComputer.pick_signal()
      displaySignaltape()

  while(updatecount()):
    routine()

if __name__ == '__main__':
  trigger()