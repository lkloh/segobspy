
import obspy
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from obspy.core import read
from obspy.core import Stream
from obspy.core import event
from obspy.signal.trigger import arPick

#Import an example file
st = obspy.seg2.seg2.readSEG2('2381.dat')
print st
print st[1].data

