import numpy as np
import os
import matplotlib.pyplot as plt
from palettable.scientific.sequential import Imola_9, Hawaii_13, Imola_9





folder = '/Users/pbortolo/work/3_projects/3_BAR/stability/outputs/bar_urc'
folder_of = 'stability_bar_urca_towdt_ctrl'
folder_plots = '/Users/pbortolo/work/3_projects/3_BAR/stability/plots'

op_of = np.loadtxt(os.path.join(folder,folder_of, 'op.csv'), skiprows = 1)
freq_of = np.loadtxt(os.path.join(folder,folder_of, 'freq.csv'), skiprows = 1)
damp_of = np.loadtxt(os.path.join(folder,folder_of, 'damp.csv'), skiprows = 1)

freq_of[freq_of==0.] = None
damp_of[damp_of==0.] = None

ws = op_of[:,0]

lw=1.5
fig,ax = plt.subplots(1,2)
fig.set_size_inches(10,4.0,forward=True) # default is (6.4,4.8)
ax[0].plot(ws, op_of[:,1]/60., c='k', linestyle=':', linewidth=lw)
ax[0].plot(ws, 3.*op_of[:,1]/60., c='k', linestyle=':', linewidth=lw)
ax[0].plot(ws, 6.*op_of[:,1]/60., c='k', linestyle=':', linewidth=lw)
ax[0].plot(ws, 9.*op_of[:,1]/60., c='k', linestyle=':', linewidth=lw)
ax[0].plot(ws, freq_of[:,0], c = np.array(Hawaii_13.colors[2])/256., linestyle='-', linewidth=lw)
ax[0].plot(ws, freq_of[:,2], c = np.array(Imola_9.colors[4])/256., linestyle='-', linewidth=lw)
ax[0].plot(ws, freq_of[:,1], c = np.array(Imola_9.colors[5])/256., linestyle='-', linewidth=lw)
ax[0].plot(ws, freq_of[:,3], c = np.array(Imola_9.colors[0])/256., linestyle='-', linewidth=lw)
ax[0].plot(ws, freq_of[:,4], c = np.array(Imola_9.colors[1])/256., linestyle='-', linewidth=lw)
ax[0].plot(ws, freq_of[:,5], c = np.array(Imola_9.colors[2])/256., linestyle='-', linewidth=lw)
ax[0].plot(ws, freq_of[:,6], c = np.array(Hawaii_13.colors[4])/256., linestyle='-', linewidth=lw)
ax[0].plot(ws, freq_of[:,7], c = np.array(Hawaii_13.colors[5])/256., linestyle='-', linewidth=lw)
ax[0].plot(ws, freq_of[:,8], c = np.array(Hawaii_13.colors[3])/256.,  linestyle='-.', linewidth=lw)
ax[0].plot(ws, freq_of[:,11], c = np.array(Imola_9.colors[3])/256.,  linestyle='-.', linewidth=lw)
ax[0].plot(ws, freq_of[:,12], c = np.array(Imola_9.colors[3])/256.,  linestyle='-.', linewidth=lw)
ax[0].plot(ws, freq_of[:,13], c = np.array(Imola_9.colors[3])/256.,  linestyle='-.', linewidth=lw)
ax[0].plot(ws, freq_of[:,9], c = np.array(Hawaii_13.colors[6])/256.,  linestyle='-.', linewidth=lw)
ax[0].plot(ws, freq_of[:,10], c = np.array(Hawaii_13.colors[6])/256.,  linestyle='-.', linewidth=lw)
ax[0].plot(ws, freq_of[:,14], c = np.array(Hawaii_13.colors[6])/256.,  linestyle='-.', linewidth=lw)
# ax[0].plot(ws, freq_of[:,11], c = np.array(Imola_9.colors[3])/256.,  linestyle='-.', linewidth=lw)
# ax[0].plot(ws, freq_of[:,12], c = np.array(Imola_9.colors[3])/256.,  linestyle='-.', linewidth=lw)
# ax[0].plot(ws, freq_of[:,13], c = np.array(Imola_9.colors[3])/256.,  linestyle='-.', linewidth=lw)
# ax[0].plot(ws, freq_of[:,14], c = np.array(Imola_9.colors[3])/256.,  linestyle='-.', linewidth=lw)
# ax[0].plot(ws, freq_of[:,15], c = np.array(Imola_9.colors[3])/256.,  linestyle='-.', linewidth=lw)


ax[0].set_xlim([3,25])
ax[0].set_ylim(bottom=0, top=2.0)
ax[0].set_ylabel('Frequency (Hz)', weight='bold')
ax[0].set_xlabel('Wind Speed (m s$^{-1}$)', weight='bold')
ax[0].grid(color=[0.8, 0.8, 0.8], linestyle="--")

ax[1].plot(ws, damp_of[:,0]*100., c = np.array(Hawaii_13.colors[2])/256., label = '1G', linestyle='-', linewidth=lw)
ax[1].plot(ws, damp_of[:,2]*100., c = np.array(Imola_9.colors[4])/256., label = '1TFA', linestyle='-', linewidth=lw)
ax[1].plot(ws, damp_of[:,1]*100., c = np.array(Imola_9.colors[5])/256., label = '1TSS', linestyle='-', linewidth=lw)
ax[1].plot(ws, damp_of[:,3]*100., c = np.array(Imola_9.colors[0])/256., label = '1BFBW', linestyle='-', linewidth=lw)
ax[1].plot(ws, damp_of[:,4]*100., c = np.array(Imola_9.colors[1])/256., label = '1BFC', linestyle='-', linewidth=lw)
ax[1].plot(ws, damp_of[:,5]*100., c = np.array(Imola_9.colors[2])/256., label = '1BFFW', linestyle='-', linewidth=lw)
ax[1].plot(ws, damp_of[:,6]*100., c = np.array(Hawaii_13.colors[4])/256., label = '1BEBW', linestyle='-', linewidth=lw)
ax[1].plot(ws, damp_of[:,7]*100., c = np.array(Hawaii_13.colors[5])/256., label = '1DTFrFr', linestyle='-', linewidth=lw)
ax[1].plot(ws, damp_of[:,8]*100., c = np.array(Hawaii_13.colors[3])/256., label = '1BEFW', linestyle='-', linewidth=lw)
ax[1].plot(ws, damp_of[:,11]*100., c = np.array(Imola_9.colors[3])/256., label = 'UHD', linestyle='-.', linewidth=lw)
ax[1].plot(ws, damp_of[:,12]*100., c = np.array(Imola_9.colors[3])/256., linestyle='-.', linewidth=lw)
ax[1].plot(ws, damp_of[:,13]*100., c = np.array(Imola_9.colors[3])/256., linestyle='-.', linewidth=lw)
ax[1].plot(ws, damp_of[:,9]*100., c = np.array(Hawaii_13.colors[6])/256., label = 'ULD', linestyle='-.', linewidth=lw)
ax[1].plot(ws, damp_of[:,10]*100., c = np.array(Hawaii_13.colors[6])/256., linestyle='-.', linewidth=lw)
ax[1].plot(ws, damp_of[:,14]*100., c = np.array(Hawaii_13.colors[6])/256., linestyle='-.', linewidth=lw)
# ax[1].plot(ws, damp_of[:,11]*100., c = np.array(Imola_9.colors[3])/256., linestyle='-.', linewidth=lw)
# ax[1].plot(ws, damp_of[:,12]*100., c = np.array(Imola_9.colors[3])/256., linestyle='-.', linewidth=lw)
# ax[1].plot(ws, damp_of[:,13]*100., c = np.array(Imola_9.colors[3])/256., linestyle='-.', linewidth=lw)
# ax[1].plot(ws, damp_of[:,14]*100., c = np.array(Imola_9.colors[3])/256., linestyle='-.', linewidth=lw)
# ax[1].plot(ws, damp_of[:,15]*100., c = np.array(Imola_9.colors[3])/256., linestyle='-.', linewidth=lw)

ax[1].set_xlim([3,25])
ax[1].set_ylim(bottom=-20., top=120.)
ax[1].set_ylabel('Aeroelastic Damping (%)', weight='bold')
ax[1].set_xlabel('Wind Speed (m s$^{-1}$)', weight='bold')
fig.suptitle('BAR-URC', weight='bold')
#ax[1].legend()
ax[1].grid(color=[0.8, 0.8, 0.8], linestyle="--")
ax[1].legend(bbox_to_anchor=(0.35, 0.02,1,1))
plt.tight_layout()
fig.savefig(os.path.join(folder_plots, 'campbell_bar_urc_aero.pdf'))
fig.savefig(os.path.join(folder_plots, 'campbell_bar_urc_aero.png'))
plt.show()
