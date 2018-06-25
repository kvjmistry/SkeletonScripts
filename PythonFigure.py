# A skeleton for making figures in python

plt.figure(<number>)
plt.errorbar(x , y, e , fmt='ro',  markersize=2, label = ‘Label');
plt.ylabel(“Y LABEL [UNIT]");
plt.xlabel(“X LABEL [UNIT]”);
plt.xlim()
plt.ylim()
plt.grid()
plt.legend(loc=1) # put legend at the top right of the plot 
plt.savefig(“NAME.png”, dpi=500);
