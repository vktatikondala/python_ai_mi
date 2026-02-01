import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

x= np.linspace(0,100,10)
y = np.sqrt(x)
z= np.power(x,2)

# Adjacent
fig = plt.figure()
# Left, Bottom,  Width and Height, Can't exceed more than 1 combining, if more subplots there.
# for example,  here ax1,it starts with 0.1 left and upto 0.4 in width , and ax2 starts with 0.55 and width is 0.4
# combining, width 0.4 + 0.4 = 0.8, so it will within the frame.
# same time, from bottom, 0.5 to hight 0.4, its combminig , 0.9 is below 1 , fits in the frame.
ax1 = fig.add_axes([0.1,0.5,0.4,0.4])
ax1.set(title='Square Roots',xlabel='Number',ylabel='Square Roots')
ax2 = fig.add_axes([0.55,0.5,0.4,0.4])
ax2.set(title='Squares',xlabel='Number',ylabel='Square Number')

ax1.plot(x,y)
ax2.plot(x,z)
st.pyplot(fig)

# instead of we're specifying these dimensions, let python takes care it.

fig2, axes = plt.subplots(nrows=1, ncols=2) # its 1 * 2 = 2 subplots drawn.

axes[0].plot(x,y)
axes[0].set(title='Square Roots',xlabel='Number',ylabel='Value')
axes[1].plot(x,z)
axes[1].set(title='Square Numbers',xlabel='Number',ylabel='Value')
plt.tight_layout() # This will fix any over lap
st.pyplot(fig2)

# we can also draw two lines in same plot, for example.

fig3, axes3 = plt.subplots(nrows=1, ncols=1) # only 1 fig

axes3.plot(x,y, label='Square Roots')
axes3.plot(x,z, label='Square Numbers')
axes3.set( xlabel='Number',ylabel='Value')
plt.tight_layout()
plt.legend(loc=0) # This will show, which line is which label, loc = 0 is default, which is best
st.pyplot(fig3)


