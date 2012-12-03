from inits import updatecount, Signaltape
class Signal(object):
  def __init__(self, issuer, target, signalString, metadata=0):
    self.issuer = issuer
    self.target = target
    self.signalString = signalString
    self.metadata = metadata

class Device(object):
  def __init__(self, receptons,emitons):
    self.receptons = receptons
    self.emitons = emitons
  def pick_signal(self):
    pass
  def dump_signal(self):
    pass

class PersonChip(Device):
  def __init__(self, receptons, emitons, public_key, private_key, friendship_keys):
    self.public_key = public_key
    self.private_key = private_key
    self.friendship_keys = friendship_keys
    super(PersonChip, self).__init__(receptons, emitons)  

  def dump_signal(self, sig):
    Signaltape.append(sig)
    
  def process(self, sig):
    if (sig.signalString == '001'):
      emiton = Signal(self.public_key, sig.issuer, '010')
      if (emiton.signalString in self.emitons):
        print("The personChip is dumping 'WHO AM I SIGNAL'...")
        self.dump_signal(emiton)
    if (sig.signalString == '010' and (sig.issuer in self.friendship_keys)):
      emiton = Signal(self.public_key, sig.issuer, '011')
      if (emiton.signalString in self.emitons):
        print("The personChip is dumping 'I AM A FRIEND'")
        self.dump_signal(emiton)

        
  def pick_signal(self):
    no=updatecount()  
    if(no!=0):  
      for sig in Signaltape[-no:]:
        if( sig.signalString in self.receptons ):
          if( (sig.target == "FFFF" or sig.target == self.public_key) and (sig.issuer != self.public_key) ):
            print("PersonChip is picking up signal:" + sig.target +"|"+ sig.signalString)
            self.process(sig)
          else:
            print("No Signal for PersonChip is found...") 
  def action(self):
    printf("PersonChip:recieved and processing signal...")
    
  
  
class Door(Device):
  def __init__(self,receptons, emitons, public_key, private_key, friendship_keys=0):
    self.public_key = public_key
    self.private_key = private_key
    self.friendship_keys = friendship_keys
    super(Door, self).__init__(receptons, emitons)  

  def dump_signal(self, sig):
    Signaltape.append(sig)


  def process(self, sig):
    if (sig.signalString == '001'):
      emiton = Signal(self.public_key, sig.issuer, '010')
      if (emiton.signalString in self.emitons):
        self.dump_signal(emiton)
        print("Log: Dumping 010 - Door")
    if (sig.signalString == '010' and (sig.issuer in self.friendship_keys)):
      emiton = Signal(self.public_key, sig.issuer, '011')
      if (emiton.signalString in self.emitons):
        self.dump_signal(emiton)
        print("Log: Dumping 011 - Door")
    if (sig.signalString == '011' and (sig.issuer in self.friendship_keys)):
      emiton = Signal(self.public_key, "FFFF", '100')
      if (emiton.signalString in self.emitons):
        self.dump_signal(emiton)
        print("Log: Dumping 100 - Door")	
      emiton = Signal(self.public_key, "AB10", '101', {"message":"Your friend had arrived and I opened for him"})
      if (emiton.signalString in self.emitons):
        self.dump_signal(emiton)
        print("Log: Dumping 101 - Door")
      self.action()
      print("Log: Performed Action - Door")
    
  
  def pick_signal(self):
    no=updatecount()  
    if(no!=0):  
      for sig in Signaltape[-no:]:
        if( sig.signalString in self.receptons ):
          if( (sig.target == "FFFF" or sig.target == self.public_key) and (sig.issuer != self.public_key) ):
            print("Door is picking up signal:" + sig.target +"|"+ sig.signalString)
            self.process(sig)
          else:
            print("No Signal for Door is found...")

  def action(self):
    print("Door|Action: recieved and processing...[Open Door]")
     
class Clock(Device):
  def __init__(self, receptons, emitons, public_key, private_key):
    self.public_key = public_key
    self.private_key = private_key
    super(Clock, self).__init__(receptons, emitons)  

  def dump_signal(self, sig):
    Signaltape.append(sig)


  def process(self, sig):
    if (sig.signalString == '100'):
      emiton = Signal(self.public_key, "AB10", "101", {"message":"Door Triggered me to record current time"})
      if (emiton.signalString in self.emitons):
        self.dump_signal(emiton)
        print("Log: Dumping 101 - Clock")
      
  def pick_signal(self):
    no=updatecount()  
    if(no!=0):  
      for sig in Signaltape[-no:]:
        if( sig.signalString in self.receptons ):
          if( (sig.target == "FFFF" or sig.target == self.public_key) ):
            print("Clock is picking up signal:" + sig.target +"|"+ sig.signalString)
            self.process(sig)
          else:
            print("No Signal for Clock is found...")

  def action(self):
    print("Clock: recieved and processing...")
    
class JoePC(Device):
  def __init__(self, receptons, emitons, public_key, private_key):
    self.public_key = public_key
    self.private_key = private_key
    super(JoePC, self).__init__(receptons, emitons)  

  def dump_signal(self, sig):
    Signaltape.append(sig)
  
  
  def process(self, sig):
    if (sig.signalString == '001'):
      emiton = Signal(self.public_key, sig.issuer, "010")
      if (emiton.signalString in self.emitons):
        self.dump_signal(emiton)
        print("Log: Dumping 010 - JoePC")
    if (sig.signalString == '101'):
      self.action(sig.metadata)
    
      
  def pick_signal(self):
    no=updatecount()  
    if(no!=0):  
      for sig in Signaltape[-no:]:
        if( sig.signalString in self.receptons ):
          if( (sig.target == "FFFF" or sig.target == self.public_key) ):
            print("JoePC is picking up signal:" + sig.target +"|"+ sig.signalString)
            self.process(sig)
          else:
            print("No Signal for JoePC is found...")

  def action(self, metadata):
    print("JoePC: "+ metadata["message"])
