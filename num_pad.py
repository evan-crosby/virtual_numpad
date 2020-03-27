## Virtual Keypad (version 0.0.1)
# Written by Evan Crosby
# Date begun: 26/03/2020

# I am bored during the shutdown here in Italy due to the Covid-19
# novel corona virus and I don't like using keypads to type numbers
# as I find them clunky and aesthetically horrifying to look at and use
# on a laptop.

import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io.wavfile import write

# setup audio settings for system to record audio to
fs = 44100  # Sample rate
seconds = 2  # Duration of recording

# initiate recording
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
# This is where I will most likely add signal processing
sd.wait()  # Wait until recording is finished

print(myrecording.shape)
time_scale = np.arange(0,seconds, (1/fs))
print(time_scale.shape)

write('output.wav', fs, myrecording)

plt.plot(time_scale, myrecording)
plt.show()

# Output data to a wavfile
#write('output.wav', fs, myrecording)  # Save as WAV file
