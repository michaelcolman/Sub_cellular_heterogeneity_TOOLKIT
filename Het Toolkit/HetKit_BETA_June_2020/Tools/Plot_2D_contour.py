import numpy as np
import pylab as p
import mpl_toolkits.axisartist as AA
from mpl_toolkits.axes_grid1 import make_axes_locatable
import sys
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.colors import LightSource
from matplotlib import cm
import statistics


#  Set font size and
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 24}

p.rc('font', **font)

Autumn_cmap = LinearSegmentedColormap.from_list('mycmap', [(0, [0.2,0,0.6]),
                                                    (0.25, [0.6,0,0.45]),
                                                    (0.5, [1,0,0]),
                                                    (0.75, [1,0.5,0]),
                                                    (1,[1,1,0.2])]
                                            )

figSRF = p.figure(facecolor='white', figsize=(18,12), dpi=100)

filename = sys.argv[1] + '.dat'

print('filename = ' + filename)

linescan_data = np.loadtxt(filename, unpack=True)

linescan_data = linescan_data[:, 5000:5500]

maximum = np.amax(linescan_data)
minimum = np.amin(linescan_data)

linescan_data = (linescan_data-minimum)/(maximum-minimum)

lY = len(linescan_data)
lX = len(linescan_data[0])

print(lX, lY, maximum)
x = np.linspace(0,lX,lX)
y = np.linspace(0,lY,lY)
X,Y = np.meshgrid(x,y)

ax1 = figSRF.add_subplot(1,1,1)
#V = np.arange(minimum, maximum, 7)
#V = [0.5, 0.55, 0.65, 0.75, 0.85, 0.95, 1.05, 1.15, 1.25, 1.35, 1.45, 1.5]
#V = [0, 0.1, 0.15, 0.2, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.9, 1.0]
V = [0.0, 0.4, 0.8, 1.2, 1.6, 2.0]
D = ax1.contourf(X, Y, linescan_data , V, alpha=1, cmap="coolwarm", vmin=0, vmax=1.0)
C = ax1.contour(X, Y, linescan_data, V, colors='black', linewidth=.5, vmin=0, vmax=1.0)

ax1.set_xticklabels('',visible=False)
ax1.set_yticklabels('',visible=False)
p.colorbar(D, ax = ax1)
p.subplots_adjust(left=0.0,bottom=0.0,right=1.0,top=1.0,wspace=0.0,hspace=0.0)
fig_name = 'Linescan.png'
p.savefig(fig_name)
