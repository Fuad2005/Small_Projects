import mido
from mido import Message, MidiFile, MidiTrack

# create a midi file object
mid = MidiFile()

# create a track
track = MidiTrack()
mid.tracks.append(track)

# add some notes to the track
for note in [60, 62, 64, 65, 67, 69, 71]:
    # create a note on message
    on = Message('note_on', note=note, velocity=64, time=0)
    track.append(on)
    # create a note off message
    off = Message('note_off', note=note, velocity=64, time=32)
    track.append(off)

# save the midi file
mid.save('piano.mid')