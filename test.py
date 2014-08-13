
import obspy
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from obspy.core import read
from obspy.core import Stream
from obspy.core import event
from obspy.signal.trigger import arPick

#Import an example file
st = read('2381.dat')
#st += read('/home/jade-01/safod/Apr29/2382.dat')
#print st[0].stats

#Need to add a distance to the header
count = 0
q = 1
for i in range(0,240):
    tr = st[i]
    t = np.arange(0,tr.stats.npts/tr.stats.sampling_rate,tr.stats.delta)
 
    #To change metadata
    print tr.stats
    if i%3 == 0:
        count += 1524
  
    tr.stats.distance = count 
    st[i] = tr

#Event.pick(st[0:6]);

#plot all traces for R1
streamX = Stream(st[0:240:3])
streamX.plot(type='section',grid_color='white',method='full',scale=0.5)
event.__Pick()

#plot all traces for R2
streamY = Stream(st[1:240:3])
streamY.plot(type='section',grid_color='white',method='full',scale=0.5)

#plot all traces for Axial
streamZ = Stream(st[2:240:3])
streamZ.plot(type='section',grid_color='white',method='full',scale=0.5)
