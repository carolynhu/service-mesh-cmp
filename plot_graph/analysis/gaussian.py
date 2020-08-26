import plotly.figure_factory as ff
import numpy as np

x1 = [1337,1226,1211,1348,1229,1307,1183,1452,1433,1330,1314,1420,1220,1182,1213,1358,1410]
x2 = [1675,1651,1499,1845,1758,1465,1700,2157,1735,1709,1872,2031,1788,1468,1689,1707,1481]
x3 = [2815,2244,2221,2751,2424,2425,2379,2951,2920,2785,2274,2285,2853,2472,2504,2381,2306]
x4 = [3866,3477,3453,3972,4295,3941,3560,4409,3681,3827,3427,3885,3797,3760,3961,3540,3637]
x5 = [6691,7447,6037,6940,6586,5875,5582,7399,6855,6746,6920,6264,6553,6341,6449,6654,6074]
x6 = [12118,12181,11876,11952,12161,11935,9828,12402,11916,12493,14008,11620,11629,11983,11781,13919,11841]

group_labels = ['conn-2', 'conn-4', 'conn-8', 'conn-16', 'conn-32', 'conn-64']

colors = ['red', 'blue', 'yellow', 'black', 'pink', 'green']

# Create distplot with curve_type set to 'normal'
fig = ff.create_distplot([x1, x2, x3, x4, x5, x6], group_labels, bin_size=10000,
                         curve_type='normal', # override default 'kde'
                         colors=colors)

# Add title
fig.update_layout(title_text='v2-sd-full-nullvm_both plotted with Normal Distribution')
fig.show()
