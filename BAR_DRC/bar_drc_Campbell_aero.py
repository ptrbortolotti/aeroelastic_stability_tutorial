
import os
import glob
import numpy as np
import matplotlib.pyplot as plt
import pyFAST.linearization.linearization as lin

MyDir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Script Parameters
BladeLen     = 100.  # Blade length, used to tune relative modal energy [m] NOTE: not needed if fst files exists
TowerLen     = 137  # Tower length, used to tune relative modal energy [m] idem
folder_name = os.path.join(MyDir, 'outputs/bar_drc/stability_bar_drca_towdt_ctrl')

fstFiles = glob.glob(folder_name + '/*.fst') # list of fst files where linearization were run, lin file will be looked for
fig_name = folder_name + '/Campbell'
fstFiles.sort() # not necessary

try:
    # Edit the mode ID file manually to better identify/distribute the modes
    modeID_file = folder_name + '/Campbell_ModesID.csv'
    fig, axes, figName =  lin.plotCampbellDataFile(modeID_file, 'ws', ylim=None, to_csv=True)
except:
    # Find lin files, perform MBC, and try to identify modes. A csv file is written with the mode IDs.
    OP, Freq, Damp, UnMapped, ModeData, modeID_file = lin.postproCampbell(fstFiles, BladeLen, TowerLen)
    fig, axes, figName =  lin.plotCampbellDataFile(modeID_file, 'ws', ylim=None, to_csv=True)


axes[0].set_ylim([0., 3.])
axes[0].set_xlim([0, 26])
axes[1].set_ylim([-0.1, 1.])
axes[1].set_xlim([0, 26])
fig.savefig(fig_name + '.png')
fig.savefig(fig_name + '.pdf')

if __name__=='__main__':
    plt.show()

