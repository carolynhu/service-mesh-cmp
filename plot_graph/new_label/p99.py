import matplotlib.pyplot as plt

x = [2, 4, 8, 16, 32, 64]


def draw_p99(latency_p99_list):
    y1 = latency_p99_list[0]   # latency_mixer_both_p50
    y2 = latency_p99_list[1]   # latency_none_base_p50
    y3 = latency_p99_list[2]   # latency_none_both_p50
    y4 = latency_p99_list[3]   # latency_v2_both_p50

    dpi = 100
    plt.figure(figsize=(1138/dpi, 871/dpi), dpi=dpi)

    plt.plot(x, y1, color='green', linestyle='dashed', marker='o', label='mixer_both')
    plt.plot(x, y2, color='purple', linestyle='dashed', marker='o', label='baseline')
    plt.plot(x, y3, color='yellow', linestyle='dashed', marker='o', label='none_both')
    plt.plot(x, y4, color='black', linestyle='dashed', marker='o', label='v2_both')

    plt.grid()

    plt.plot(x, y1, color='green')
    for a, b in zip(x, y1):
        plt.text(a, b, str(b))

    plt.plot(x, y2, color='purple')
    for a, b in zip(x, y2):
        plt.text(a, b, str(b))

    plt.plot(x, y3, color='yellow')
    for a, b in zip(x, y3):
        plt.text(a, b, str(b))

    plt.plot(x, y4, color='black')
    for a, b in zip(x, y4):
        plt.text(a, b, str(b))

    # title = "1.5-alpha.afe8e4a0f00e8baa80e19d92cead0284529d5006_p99"
    # plt.title(title + ' 1000QPS over 240 seconds')
    plt.ylabel('latency,milliseconds')
    plt.xlabel('connections')
    plt.legend()
    plt.axis([0, 68, 0, 25])

    # plt.savefig(title + ".png", dpi=dpi)
    plt.savefig("istio_master_p99.png", dpi=dpi)
    plt.show()
