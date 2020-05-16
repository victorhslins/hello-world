# Victor's Mpl Notes
# USEFUL LINKS:
# Datasets used below: shorturl.at/syETZ
# Matplotlib Format Strings: shorturl.at/tyFQU
# Corey Schafer's video about matplotlib (the one I used to write this guide): shorturl.at/gvzR1
# Obs.: for simplicty, from now on I will refer to matplotlib as 'mpl'.

# Import pylot from matplotlib with a 'shortcut' plt 
# (if you haven't matplotlib yet, go to your terminal, type without quotes 'pip install matplotlib and press enter')
from matplotlib import pyplot as plt

# Built-in mpl plot styles. If you print this command, it will show in the terminal the available plot styles to be used.
# print(plt.style.available)
# If you want to use one of the styles, you should do as the following:
# plt.style.use('name_of_the_style')

# X-Ages data (ages)
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# Median Python Developer Salaries by Age
# Y-Axis Data
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
# Plot the data provided above, give it a color (e.g. Yellow in Hexadecimal), a line width, a linestyle, and a label.
plt.plot(ages_x, py_dev_y, color ='#002DE0', linewidth = 3, label='Python Devs')

# Median JavaScript Developer Salaries by Age
# Y-Axis Data 
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
# Plot the data provided above, give it a color (e.g. Orange in Hexadecimal), a line width, a linestyle, and a label.
plt.plot(ages_x, js_dev_y, color = '#FA8900', linewidth = 3, label = 'JavaScript')

# Median developer Salaries by Age
# Provides the y-axis data
dev_y = [38496, 42000, 46752, 49320, 53230, 
        56000, 62316, 64928, 67317, 68748, 73752]
# Plot the data provided above, give it a color (e.g. Grey in Hexadecimal), a linestyle, and a label.
plt.plot(ages_x, dev_y, color = '#4C4A48', linestyle = '--', label='All Devs')

# Label the x-axis
plt.xlabel('Ages')
# Label the y-axis
plt.ylabel('Median Salary (USD)')
# Gives a title to the plot
plt.title('Median Salary (USD) by Age')

# Include the legend in the plot using the labels assigned before
plt.legend()

# Generates a grid for the graph
plt.grid(True)

# Makes the padding better (just visualization stuff)
plt.tight_layout()

# If you wish so, you can save the plot as an image or other types of doc, to this file's current directory.
# You just need to uncomment the following single line of code.
# plt.savefig('plot.png')

# Shows combined plot of the datasets
plt.show()
