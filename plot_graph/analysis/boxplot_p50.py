import plotly.graph_objects as go

fig = go.Figure()


# conn_2
fig.add_trace(go.Box(
    y=[998,984,1092,1155,1121,1145, 1162,1123, 1314,1221,1049,1152,1125,1048,1232,1387,1109,1422,1048,1119,1218, 1135, 1074, 1179, 1033,1132,1134,1159,1188,1289,1181,1184,1083,1140,1056,1241,1277,1353, 1302],
    name='conn_2',
    boxpoints='all',
    marker_color='red',
    boxmean='sd' # represent mean and standard deviation
))

# conn_4
fig.add_trace(go.Box(
    y=[1328,1342,1135,1482, 1432,1303,1544,1462, 1666, 1600,1389, 1435, 1479, 1414, 1680, 1981, 1471,1879,1413, 1486, 1634, 1682, 1474,1580, 1411,1462,1498, 1605, 1649, 1625, 1494,1544, 1449, 1543,1408, 1610, 1723,1845, 1750],
    name='conn_4',
    boxpoints='all',
    marker_color='blue',
    boxmean='sd' # represent mean and standard deviation
))

# conn_8
fig.add_trace(go.Box(
    y=[2023,1706,1723,1891,1733, 2018,2437,2407,2721, 2563,2283,2634,2492,2427,2829,3254,2343,2881,2328, 2407,2658, 2725, 2378, 2645, 2314,2344, 2393,2776,2726,2570,2471, 2527, 2355,2515,2378,2559, 2803, 2955, 2906],
    name='conn_8',
    boxpoints='all',
    marker_color='yellow',
    boxmean='sd' # represent mean and standard deviation
))

# conn_16
fig.add_trace(go.Box(
    y= [2876,2569, 3097,3003, 3277, 3563,4156, 4242, 5198, 4914, 4199,4681,4666, 4316,4845, 5672, 4205,5441, 4096, 4333, 4657, 4957, 4195, 4602, 4126,4159, 4185, 4692,4866, 4545, 4653, 4549,  4154, 4153, 4193,4618,5235, 5403, 5356],
    name='conn_16',
    boxpoints='all',
    marker_color='black',
    boxmean='sd' # represent mean and standard deviation
))

# conn_32
fig.add_trace(go.Box(
    y= [5390,4556,5309, 5166,5156, 5192,7517, 8264,9120, 8763,8027, 8124, 8279,7369,9355,10283, 8083,9704, 7669,8227,8614, 8969,7848,8193,7608,7634,8035,8279, 9253,8425,8445,8532,7539,7475,7299,8652,9364,9537, 10057],
    name='conn_32',
    boxpoints='all',
    marker_color='pink',
    boxmean='sd' # represent mean and standard deviation
))

# conn_64
fig.add_trace(go.Box(
    y=[8457,8157,7682,9318,9277,8510,14662,15875,16376,16252,14777,15481,15883,14272,18042,19876,15131,18587,15117,15655,16421,15826,15766,15324,15349,15370,15605,15427,17201,15880,15577,15959,15288,15622,14066,16077,16773,17665,18139],
    name='conn_64',
    boxpoints='all',
    marker_color='green',
    boxmean='sd' # represent mean and standard deviation
))
fig.show()
