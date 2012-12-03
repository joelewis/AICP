A python program to simulate, Communication of Intelligent Physical Devies in Real World to demonstrate my design of AICP Protocol.

Assumed to be comprising of four Intelligent Household Entities(A Door, A PersonChip, A Clock, A Computer )
Four objects of their kind are instantiated and a 'Signal Stream' is constructed initially by placing an arbitrary Signal.
Each of the devices( or Entity ) has its own set of 'Receptons' and 'Emitons'

'Receptons' are similar to the sensory inputs of AI Agents, except that receptons are Signals and follow a standardized pattern. 

'Emitons' are Signals that are emitted by the Devices( recorded in 'SignalTape' Object in Program but may represent Real World Signals in Real Time)
Similar to Receptons, Emitons are also standardised.

Each Device reacts to Signal Stream, corresponding to its Receptons and end up with an Action and/or Dumping a Signal of its own through its Emitons.

The Communication Design that is being proposed is that, 
  A well recognized set of standards are to be formulated with which Future Intelligent Devices are built as units which react based on Events in 'Receptons' and based on the Decision made by the Agent, a series of Actions and Communicate Signals based on their Emitons follow.
  
  (or)
  
  A Standard Protocol that are accepted by a variety of Agents, that ensures effective Communication between  Agents( or Devices), with or without Manual Intervention.
  
In the simulation Program a Sample Standards of Recepton and Emiton Signals is used as follows:
  Each Signal String Consists of three bits, mapping one-to-one with a specific 'Talk Message'
  
  001 - "Who Are You"
  010 - "Who Am I"
  011 - "Im a Friend"
  100 - "Record Time"
  101 - "Notify Computer"
  
  Above Table represents a tiny Standard, applying for Household Tasks.
  
  Each Signal in Signal Stream consists of a Signal Object which contains information about "Who Issued the Signal", "To Whom it's Intended" and "Signal String".
  
  Test Scenario in Simulation Program:
    A PersonChip on a wrist interrogates Devies in the Environment with 001.
    The various Devices(Door, Computer) in the Environment Emit 010 Emitons.
    The PersonChip looks for a door with a matching 'friendhip_key' and emits 011-"I'm a Friend" Emiton targetted at the Door.
    The Door picks 011 from Signal Stream and performs its Action and Dumps two more Emitons of its own into Signal Stream, namely 100, 101.
    The Clock picks up 100, performs its Action and Dumps its Emiton Signals, if applies.
    The Computer does the same. It picks up 101 and performs Action and Dumps its own Emiton.
    The Process Continues untill the task is accomplished and there are no more signals in the Signal Stream.
    
  To test Devices of your own, put your class file of the device in classes.py and trigger the main function.
  Follow the pattern of previously defined classes to create your own.