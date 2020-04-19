import matplotlib.pyplot as plt

x = [2, 4, 8, 16, 32, 64]


def draw_p90(latency_p90_list):
    y1 = latency_p90_list[0]
    y2 = latency_p90_list[1]
    y3 = latency_p90_list[2]

    y4 = latency_p90_list[3]
    y5 = latency_p90_list[4]

    y6 = latency_p90_list[5]
    y7 = latency_p90_list[6]

    dpi = 100
    plt.figure(figsize=(1138/dpi, 871/dpi), dpi=dpi)

    plt.plot(x, y1, color='green', linestyle='dashed', marker='o', label='baseline')
    # plt.plot(x, y2, color='purple', linestyle='dashed', marker='o', label='mixer-serveronly')
    plt.plot(x, y3, color='yellow', linestyle='dashed', marker='o', label='mixer-both')

    # plt.plot(x, y4, color='black', linestyle='dashed', marker='o', label='none-serveronly')
    plt.plot(x, y5, color='blue', linestyle='dashed', marker='o', label='none-both')

    # plt.plot(x, y6, color='blue', linestyle='dashed', marker='o', label='telemetryv2-serveronly')
    plt.plot(x, y7, color='pink', linestyle='dashed', marker='o', label='telemetryv2-both')
    plt.grid()

    plt.plot(x, y1, color='green')
    for a, b in zip(x, y1):
        plt.text(a, b, str(b))

    # plt.plot(x, y2, color='purple')
    # for a, b in zip(x, y2):
    #     plt.text(a, b, str(b))

    plt.plot(x, y3, color='yellow')
    for a, b in zip(x, y3):
        plt.text(a, b, str(b))

    # plt.plot(x, y4, color='black')
    # for a, b in zip(x, y4):
    #     plt.text(a, b, str(b))

    plt.plot(x, y5, color='blue')
    for a, b in zip(x, y5):
        plt.text(a, b, str(b))

    # plt.plot(x, y6, color='blue')
    # for a, b in zip(x, y6):
    #     plt.text(a, b, str(b))

    plt.plot(x, y7, color='pink')
    for a, b in zip(x, y7):
        plt.text(a, b, str(b))

    # title = "1.5 p90"
    # plt.title(title + ' 1000QPS over 240 seconds')
    plt.ylabel('latency,milliseconds')
    plt.xlabel('connections')
    plt.legend()
    plt.axis([0, 68, 0, 26])

    # plt.savefig(title + ".png", dpi=dpi)
    plt.savefig("istio_1_6_p90.png", dpi=dpi)
    plt.show()
