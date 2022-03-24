from audioop import avg
import numpy as np
import matplotlib.pyplot as plt
import os

freq = 0.627315 # Hz, first backward whirling edge mode
ws_range = 2.
avg_ws = 25.
Tinit = 60.
Tmax = 300.
Tsampling = 0.01

time  = np.arange(0., Tmax+Tsampling, Tsampling)
windspeed = avg_ws + ws_range * np.sin(time*2.*np.pi*freq)


wnd = np.zeros((len(time)+1,9))
wnd[1:,0] = time + Tinit
wnd[0,1] = avg_ws
wnd[1:,1] = windspeed

header =    '!     Time        Wind        Wind      Vertical     Horiz.     Pwr. Law   Lin. Vert.     Gust       Upflow   \n !                Speed        Dir        Speed       Shear     Vert. Shr     Shear       Speed       Angle    \n !     (s)        (m/s)       (deg)       (m/s)        (-)         (-)         (-)        (m/s)       (deg) \n'

run_dir                = os.path.dirname( os.path.realpath(__file__) ) + os.sep

np.savetxt(os.path.join(run_dir, 'wind.wnd'), wnd, header=header, fmt = '%.4e')