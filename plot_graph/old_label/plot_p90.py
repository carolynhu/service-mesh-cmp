import matplotlib.pyplot as plt
plt.ylabel('latency,milliseconds')
plt.xlabel('connections')

# P99
x1=[64,32,16,8,4,2]
x2=[64,32,16,8,4,2]
x3=[64,32,16,8,4,2]
x4=[64,32,16,8,4,2]

y1=[14.987, 9.963, 6.143,4.383, 3.317, 2.83]
y2=[12.699, 6.912,4.182, 2.489, 1.748, 1.427]
y3=[8.981, 5.818,3.443,2.22, 1.492,1.247]
y4=[2.839, 1.732,1.05,0.738,0.656, 0.457]

# P90
# x1=[64,32,16,8,4,2]
# x2=[64,32,16,8,4,2]
# x3=[64,32,16,8,4,2]
# x4=[64,32,16,8,4,2]
#
# y1=[13.609, 8.45, 4.601,2.591,1.901, 1.497]
# y2=[11.739, 5.943, 3.752, 2.202, 1.493, 1.207]
# y3=[8.007, 4.851,2.953,1.845, 1.236,0.99]
# y4=[1.229, 0.817,0.631,0.555,0.498, 0.349]

my_dpi=100
plt.figure(figsize=(1138/my_dpi, 871/my_dpi), dpi=my_dpi)


plt.plot([64,32,16,8,4,2], [14.987, 9.963, 6.143,4.383, 3.317, 2.83], color='yellow', linestyle='dashed', marker='o', label='mixer-both')
plt.plot([64,32,16,8,4,2], [12.699, 6.912,4.182, 2.489, 1.748, 1.427], color='pink', linestyle='dashed', marker='o', label='telemetryv2-both')
plt.plot([64,32,16,8,4,2], [8.981, 5.818,3.443,2.22, 1.492,1.247], color='blue', linestyle='dashed', marker='o', label='none-both')
plt.plot([64,32,16,8,4,2], [2.839, 1.732,1.05,0.738,0.656, 0.457], color='green', linestyle='dashed', marker='o', label='baseline')

plt.grid()

plt.plot(x1,y1,color='yellow')
for a, b in zip(x1,y1):
    plt.text(a,b,str(b))

plt.plot(x2,y2,color='pink')
for a, b in zip(x2,y2):
    plt.text(a,b,str(b))

plt.plot(x3,y3,color='blue')
for a, b in zip(x3,y3):
    plt.text(a,b,str(b))

plt.plot(x4,y4,color='green')
for a, b in zip(x4,y4):
    plt.text(a,b,str(b))

plt.legend()
plt.axis([0, 70, 0, 20])
# plt.show()
# plt.get_current_fig_manager().resize(1138,871)
# plt.show()

plt.savefig('1_6_p99.png', dpi=my_dpi)
plt.show()
