import matplotlib.pyplot as plt
import numpy as np

# Make some dummy data
np.random.seed(1)
dummy_data = np.random.lognormal(size=40)

def make_labels(ax, boxplot):

    # Grab the relevant Line2D instances from the boxplot dictionary
    iqr = boxplot['boxes'][0]
    caps = boxplot['caps']
    med = boxplot['medians'][0]
    fly = boxplot['fliers'][0]

    # The x position of the median line
    xpos = med.get_xdata()

    # Lets make the text have a horizontal offset which is some
    # fraction of the width of the box
    xoff = 0.10 * (xpos[1] - xpos[0])

    # The x position of the labels
    xlabel = xpos[1] + xoff

    # The median is the y-position of the median line
    median = med.get_ydata()[1]

    # The 25th and 75th percentiles are found from the
    # top and bottom (max and min) of the box
    pc25 = iqr.get_ydata().min()
    pc75 = iqr.get_ydata().max()

    # The caps give the vertical position of the ends of the whiskers
    capbottom = caps[0].get_ydata()[0]
    captop = caps[1].get_ydata()[0]

    # Make some labels on the figure using the values derived above
    ax.text(xlabel, median,
            'Median = {:6.3g}'.format(median), va='center')
    ax.text(xlabel, pc25,
            '25th percentile = {:6.3g}'.format(pc25), va='center')
    ax.text(xlabel, pc75,
            '75th percentile = {:6.3g}'.format(pc75), va='center')
    ax.text(xlabel, capbottom,
            'Bottom cap = {:6.3g}'.format(capbottom), va='center')
    ax.text(xlabel, captop,
            'Top cap = {:6.3g}'.format(captop), va='center')

    # Many fliers, so we loop over them and create a label for each one
    print(fly.get_ydata())
    for flier in fly.get_ydata():
        ax.text(1 + xoff, flier,
                'Outlier = {:9.9g}'.format(flier), va='center')

# Make the figure
red_diamond = dict(markerfacecolor='r', marker='o')
fig3, ax3 = plt.subplots()
ax3.set_title('P50 Outliers')

# Create the boxplot and store the resulting python dictionary
my_boxes = ax3.boxplot([8457,8157,7682,9318,9277,8510,14662,15875,16376,16252,14777,15481,15883,14272,18042,19876,15131,18587,15117,15655,16421,15826,15766,15324,15349,15370,15605,15427,17201,15880,15577,15959,15288,15622,14066,16077,16773,17665,18139], flierprops=red_diamond)

# Call the function to make labels
make_labels(ax3, my_boxes)

plt.show()