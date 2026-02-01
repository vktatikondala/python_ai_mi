import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(0,100,11)
y = np.sqrt(x).round(2)

fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y,'orange')
axes.set(xlabel='Number',ylabel='Sqrt')
axes.title.set_text('Square Roots')
plt.show()