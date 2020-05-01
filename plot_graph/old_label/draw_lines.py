import pandas as pd
from plot_graph.old_label.p99 import draw_p99
from plot_graph.old_label.p90 import draw_p90
from plot_graph.old_label.p50 import draw_p50
from plot_graph.old_label.p99_9 import draw_p99_9

filepath = "/Users/carolynprh/service-mesh-cmp/nighthawk_debugging/nighthawk_burst_size_experiment/istio-1.6-21162.csv"   # file out your csv path


def latency_vs_conn():
    df = pd.read_csv(filepath)

    latency_mixer_base_p50 = get_latency_vs_conn_y_series(df, '_mixer_base', 'p50')
    latency_mixer_serveronly_p50 = get_latency_vs_conn_y_series(df, '_mixer_serveronly', 'p50')
    latency_mixer_both_p50 = get_latency_vs_conn_y_series(df, '_mixer_both', 'p50')
    latency_none_serveronly_p50 = get_latency_vs_conn_y_series(df, '_none_serveronly', 'p50')
    latency_none_both_p50 = get_latency_vs_conn_y_series(df, '_none_both', 'p50')
    # latency_none_plaintext_both_p50 = get_latency_vs_conn_y_series(df, '_none_plaintext_both', 'p50')
    latency_v2_serveronly_p50 = get_latency_vs_conn_y_series(df, 'nullvm_serveronly', 'p50')
    latency_v2_both_p50 = get_latency_vs_conn_y_series(df, 'nullvm_both', 'p50')
    latency_p50_list = [latency_mixer_base_p50, latency_mixer_serveronly_p50, latency_mixer_both_p50,
                        latency_none_serveronly_p50, latency_none_both_p50, latency_v2_serveronly_p50,
                        latency_v2_both_p50]
    # print(latency_p50_list)
    # draw_p50(latency_p50_list)

    latency_mixer_base_p90 = get_latency_vs_conn_y_series(df, '_mixer_base', 'p90')
    latency_mixer_serveronly_p90 = get_latency_vs_conn_y_series(df, '_mixer_serveronly', 'p90')
    latency_mixer_both_p90 = get_latency_vs_conn_y_series(df, '_mixer_both', 'p90')
    latency_none_serveronly_p90 = get_latency_vs_conn_y_series(df, '_none_serveronly', 'p90')
    latency_none_both_p90 = get_latency_vs_conn_y_series(df, '_none_both', 'p90')
    # latency_none_plaintext_both_p90 = get_latency_vs_conn_y_series(df, '_none_plaintext_both', 'p90')
    latency_v2_serveronly_p90 = get_latency_vs_conn_y_series(df, 'nullvm_serveronly', 'p90')
    latency_v2_both_p90 = get_latency_vs_conn_y_series(df, 'nullvm_both', 'p90')
    latency_p90_list = [latency_mixer_base_p90, latency_mixer_serveronly_p90, latency_mixer_both_p90,
                                            latency_none_serveronly_p90, latency_none_both_p90, latency_v2_serveronly_p90,
                                            latency_v2_both_p90]
    # print("+=========")
    # print(latency_p90_list)

    # draw_p90(latency_p90_list)

    latency_mixer_base_p99 = get_latency_vs_conn_y_series(df, '_mixer_baseline', 'p99')
    latency_mixer_serveronly_p99 = get_latency_vs_conn_y_series(df, '_mixer_serveronly', 'p99')
    latency_mixer_both_p99 = get_latency_vs_conn_y_series(df, '_mixer_both', 'p99')
    latency_none_serveronly_p99 = get_latency_vs_conn_y_series(df, '_none_serveronly', 'p99')
    latency_none_both_p99 = get_latency_vs_conn_y_series(df, '_none_both', 'p99')
    # latency_none_plaintext_both_p99 = get_latency_vs_conn_y_series(df, '_none_plaintext_both', 'p99')
    latency_v2_serveronly_p99 = get_latency_vs_conn_y_series(df, 'v2-nullvm_severonly', 'p99')
    latency_v2_both_p99 = get_latency_vs_conn_y_series(df, 'v2-nullvm_both', 'p99')
    latency_p99_list = [latency_mixer_base_p99, latency_mixer_serveronly_p99, latency_mixer_both_p99,
                        latency_none_serveronly_p99, latency_none_both_p99, latency_v2_serveronly_p99,
                        latency_v2_both_p99]
    print(latency_p99_list)
    draw_p99(latency_p99_list)

    # latency_mixer_base_p99_9 = get_latency_vs_conn_y_series(df, '_mixer_base', 'p99.9')
    # latency_mixer_serveronly_p99_9 = get_latency_vs_conn_y_series(df, '_mixer_serveronly', 'p99.9')
    # latency_mixer_both_p99_9 = get_latency_vs_conn_y_series(df, '_mixer_both', 'p99.9')
    # latency_none_serveronly_p99_9 = get_latency_vs_conn_y_series(df, '_none_serveronly', 'p99.9')
    # latency_none_both_p99_9 = get_latency_vs_conn_y_series(df, '_none_both', 'p99.9')
    # # latency_none_plaintext_both_p99 = get_latency_vs_conn_y_series(df, '_none_plaintext_both', 'p99')
    # latency_v2_serveronly_p99_9 = get_latency_vs_conn_y_series(df, 'nullvm_serveronly', 'p99.9')
    # latency_v2_both_p99_9 = get_latency_vs_conn_y_series(df, 'nullvm_both', 'p99.9')
    # latency_p99_9_list = [latency_mixer_base_p99_9, latency_mixer_serveronly_p99_9, latency_mixer_both_p99_9,
    #                     latency_none_serveronly_p99_9, latency_none_both_p99_9, latency_v2_serveronly_p99_9,
    #                     latency_v2_both_p99_9]

    # draw_p99_9(latency_p99_9_list)

def get_latency_vs_conn_y_series(df, mixer_mode, quantiles):
    y_series_data = []
    for thread in [2, 4, 8, 16, 32, 64]:
        data = df.query('ActualQPS == 1000 and NumThreads == @thread and Labels.str.endswith(@mixer_mode)')
        if not data[quantiles].head().empty:
            y_series_data.append(data[quantiles].head(1).values[0])  # for fortio needs divide by 1000 here
        else:
            y_series_data.append('null')
    return y_series_data


latency_vs_conn()