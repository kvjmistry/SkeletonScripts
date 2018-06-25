import numpy as np
import matplotlib.pyplot as plt

# These can be overwritten in the plot commands
plt.close("all”)  # Close all open figures

plt.rcParams['axes.linewidth'] = 3                 # Sets the boarder width 
plt.rcParams.update({'errorbar.capsize': 1.2})    # Gives a cap to the errorbars
plt.rcParams["font.weight"] = "bold"              # sets all font weights to bold
plt.rcParams["font.size"] = 20                    # Sets all font sizes to bold
plt.rcParams["axes.labelweight"] = "bold"         # Sets all label fontweights to bold 
plt.rcParams["lines.markersize"] = 4
plt.rcParams["grid.linestyle"] = "--"
plt.rcParams['figure.figsize'] = 8, 8 # Sets the figure size
