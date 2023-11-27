import scipy.integrate as integrate
import scipy.special as special
from numpy import sqrt, sin, cos, pi
import numpy as np

#FIX MEEEEEEEEEEEEEEEEEEEE I DONT THINK IM QUITE RIGHT

#import numpy as np
#def window_rms(a, window_size):
 # a2 = np.power(a,2)
  #window = np.ones(window_size)/float(window_size)
  #return np.sqrt(np.convolve(a2, window, 'valid'))


time_start = ''
time_end = ''
amplitude = ''
freq = ''
phase_ang = ''

# sqrt{ (Amp^2) * (cos^2[{ang_freq*time} + {phase_angle}]) dt }

#this function takes the square root, of the integral, of 
# (amplitude squared times, the cos squared of the (angular frequency times time ) 
# plus the phase angle) dt

#basically it will take your start and end times, the frequency of your signal, 
#the amplitude of your signal, and the phase angle(converts to radians) and gives you
#the mean value of your sinusoidal AC signal.

def sin_rms(time_end, amplitude, freq, phase_ang, time_start = 0,):
   # we first calculate what the time interval we will be integrating over
    t = ''
    #we save 
    inside = (((freq*2*pi)*(t)) + (freq*2*pi))
    print(inside)
    outside = float((amplitude**2)/t)
    def f(t):
        return (outside*(((sin(inside))**2)))
    #cos1 = ((cos(inside))**2)
    print(outside)
    result1 = integrate.quad(f,time_start,time_end)
    print(result1)
    result2 = sqrt(result1)
    return result2
    

if __name__ == '__main__':
    time_start = int(input())
    time_end = int(input())
    amplitude = int(input())
    freq = int(input())
    phase_ang = int(input())
    rms = sin_rms(time_end, amplitude, freq, phase_ang, time_start)
    print(rms)
#answer = window_rms(2,3) 
#print(answer)



