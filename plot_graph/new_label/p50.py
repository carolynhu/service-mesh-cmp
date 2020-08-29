import matplotlib.pyplot as plt

x = [2, 4, 8, 16, 32, 64]


def draw_p50(latency_p50_list):
    y1 = latency_p50_list[0]
    y2 = latency_p50_list[1]
    y3 = latency_p50_list[2]
    y4 = latency_p50_list[3]
    y5 = latency_p50_list[4]
    y6 = latency_p50_list[5]

    dpi = 100
    plt.figure(figsize=(1138/dpi, 871/dpi), dpi=dpi)

    plt.plot(x, y1, color='green', linestyle='dashed', marker='o', label='baseline')
    plt.plot(x, y2, color='blue', linestyle='dashed', marker='o', label='none_mtls_both')
    plt.plot(x, y3, color='red', linestyle='dashed', marker='o', label='v2-stats-wasm_both')
    plt.plot(x, y4, color='pink', linestyle='dashed', marker='o', label='v2-stats-nullvm_both')
    plt.plot(x, y5, color='yellow', linestyle='dashed', marker='o', label='v2-sd-full-nullvm_both')
    plt.plot(x, y6, color='black', linestyle='dashed', marker='o', label='v2-sd-nologging-nullvm_both')
    plt.grid()

    plt.plot(x, y1, color='green')
    for a, b in zip(x, y1):
        plt.text(a, b, str(b))

    plt.plot(x, y2, color='blue')
    for a, b in zip(x, y2):
        plt.text(a, b, str(b))

    plt.plot(x, y3, color='red')
    for a, b in zip(x, y3):
        plt.text(a, b, str(b))

    plt.plot(x, y4, color='pink')
    for a, b in zip(x, y4):
        plt.text(a, b, str(b))

    plt.plot(x, y5, color='yellow')
    for a, b in zip(x, y5):
        plt.text(a, b, str(b))

    plt.plot(x, y6, color='black')
    for a, b in zip(x, y6):
        plt.text(a, b, str(b))

    # title = "1.5-alpha.afe8e4a0f00e8baa80e19d92cead0284529d5006_p50"
    # plt.title(title + '1000QPS over 240 seconds')
    plt.ylabel('latency,milliseconds')
    plt.xlabel('connections')
    plt.legend()
    plt.axis([0, 68, 0, 25])

    plt.savefig("fortio_no_jitter_1_7_p50.png", dpi=dpi)
    plt.show()
