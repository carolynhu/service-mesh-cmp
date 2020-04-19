import matplotlib.pyplot as plt

x = [2, 4, 8, 16, 32, 64]


def draw_p99_9(latency_p99_9_list):
    y1 = latency_p99_9_list[0]
    # y2 = latency_p99_9_list[1]
    y3 = latency_p99_9_list[2]

    # y4 = latency_p99_9_list[3]
    y5 = latency_p99_9_list[4]

    # y6 = latency_p99_9_list[5]
    y7 = latency_p99_9_list[6]

    dpi = 100
    plt.figure(figsize=(1138/dpi, 871/dpi), dpi=dpi)

    plt.plot(x, y1, color='red', linestyle='dashed', marker='o', label='istio-baseline')
    # plt.plot(x, y2, color='purple', linestyle='dashed', marker='o', label='mixer-serveronly')
    plt.plot(x, y3, color='green', linestyle='dashed', marker='o', label='mixer-both')
    #
    # plt.plot(x, y4, color='black', linestyle='dashed', marker='o', label='none-serveronly')
    plt.plot(x, y5, color='orange', linestyle='dashed', marker='o', label='none-both')
    #
    # plt.plot(x, y6, color='blue', linestyle='dashed', marker='o', label='telemetryv2-serveronly')
    plt.plot(x, y7, color='silver', linestyle='dashed', marker='o', label='telemetryv2-both')
    plt.grid()

    plt.plot(x, y1, color='red')
    for a, b in zip(x, y1):
        plt.text(a, b, str(b))

    # plt.plot(x, y2, color='purple')
    # for a, b in zip(x, y2):
    #     plt.text(a, b, str(b))

    plt.plot(x, y3, color='green')
    for a, b in zip(x, y3):
        plt.text(a, b, str(b))

    # plt.plot(x, y4, color='black')
    # for a, b in zip(x, y4):
    #     plt.text(a, b, str(b))

    plt.plot(x, y5, color='orange')
    for a, b in zip(x, y5):
        plt.text(a, b, str(b))

    # plt.plot(x, y6, color='blue')
    # for a, b in zip(x, y6):
    #     plt.text(a, b, str(b))

    plt.plot(x, y7, color='silver')
    for a, b in zip(x, y7):
        plt.text(a, b, str(b))

    title = "istio-1.5-alpha.e508b3d58a05b53ed30a61a7e2c1c23c2af267fb_p99.9"
    plt.title(title + ' 1000QPS over 240 seconds')
    plt.ylabel('latency,milliseconds')
    plt.xlabel('connections')
    plt.legend()
    plt.axis([0, 68, 0, 23.0000])

    plt.savefig(title + ".png", dpi=dpi)
    plt.show()
