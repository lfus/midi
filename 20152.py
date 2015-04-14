'''

All melodic movement happens in a diatonic scale, a key.
   
Each step in the melodic movement generates and is
(increasingly) dependent on the sum of the steps.

Each piece is divided into groups of step movements. 

Each group has a different sum of its steps. 

Each piece is divided into timed regions. 

Each timed region has one scale/key assigned to it.

Rhythm is nth element groups, 1 element is a run.

'''
#Import the library

from midiutil.MidiFile import MIDIFile
import random
from numpy import *

# Create the MIDIFile Object with 1 track
MyMIDI = MIDIFile(1)

# Tracks are numbered from zero. Times are measured in beats.

track = 0  
time = 0

Major = array([2,4,5,7,9,11,]) 
Minor = array([2,3,5,7,9,10,])

# Add track name and tempo.
MyMIDI.addTrackName(track,time,"rnd")
MyMIDI.addTempo(track,time,125)

for i in range(1,15):

    # Add a note. addNote expects the following information:
    track = 0
    channel = 0

    pitch = 60 + random.choice(Major)
    time = random.randint(0,52)

    duration = 1
    volume = 100

    # Now add the note.
    MyMIDI.addNote(track,channel,pitch,time,duration,volume)


# And write it to disk.
binfile = open("output.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()
