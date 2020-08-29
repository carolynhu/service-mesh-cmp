import pandas as pd
from plot_graph.new_label.p99 import draw_p99
from plot_graph.new_label.p90 import draw_p90
from plot_graph.new_label.p50 import draw_p50
# from plot_graph.new_label.p99_9 import draw_p99_9

filepath = "/Users/carolynprh/fortio_no_jitter/fortio_no-jitter.csv"   # file out your csv path


def latency_vs_conn():
    df = pd.read_csv(filepath)

    latency_none_mtls_baseline_p50 = get_latency_vs_conn_y_series(df, '_none_mtls_baseline', 'p50')
    latency_none_mtls_both_p50 = get_latency_vs_conn_y_series(df, '_none_mtls_both', 'p50')
    latency_v2_stats_wasm_both_p50 = get_latency_vs_conn_y_series(df, '_v2-stats-wasm_both', 'p50')
    latency_v2_stats_nullvm_both_p50 = get_latency_vs_conn_y_series(df, '_v2-stats-nullvm_both', 'p50')
    latency_v2_sd_full_nullvm_both_p50 = get_latency_vs_conn_y_series(df, '_v2-sd-full-nullvm_both', 'p50')
    latency_v2_sd_nologging_nullvm_both_p50 = get_latency_vs_conn_y_series(df, '_v2-sd-nologging-nullvm_both', 'p50')

    latency_p50_list = [latency_none_mtls_baseline_p50, latency_none_mtls_both_p50, latency_v2_stats_wasm_both_p50, latency_v2_stats_nullvm_both_p50,
                        latency_v2_sd_full_nullvm_both_p50,latency_v2_sd_nologging_nullvm_both_p50]
    print(latency_p50_list)
    draw_p50(latency_p50_list)

    latency_none_mtls_baseline_p90 = get_latency_vs_conn_y_series(df, '_none_mtls_baseline', 'p90')
    latency_none_mtls_both_p90 = get_latency_vs_conn_y_series(df, '_none_mtls_both', 'p90')
    latency_v2_stats_wasm_both_p90 = get_latency_vs_conn_y_series(df, '_v2-stats-wasm_both', 'p90')
    latency_v2_stats_nullvm_both_p90 = get_latency_vs_conn_y_series(df, '_v2-stats-nullvm_both', 'p90')
    latency_v2_sd_full_nullvm_both_p90 = get_latency_vs_conn_y_series(df, '_v2-sd-full-nullvm_both', 'p90')
    latency_v2_sd_nologging_nullvm_both_p90 = get_latency_vs_conn_y_series(df, '_v2-sd-nologging-nullvm_both', 'p90')

    latency_p90_list = [latency_none_mtls_baseline_p90, latency_none_mtls_both_p90, latency_v2_stats_wasm_both_p90,
                        latency_v2_stats_nullvm_both_p90,
                        latency_v2_sd_full_nullvm_both_p90, latency_v2_sd_nologging_nullvm_both_p90]

    print(latency_p90_list)
    draw_p90(latency_p90_list)

    latency_none_mtls_baseline_p99 = get_latency_vs_conn_y_series(df, '_none_mtls_baseline', 'p99')
    latency_none_mtls_both_p99 = get_latency_vs_conn_y_series(df, '_none_mtls_both', 'p99')
    latency_v2_stats_wasm_both_p99 = get_latency_vs_conn_y_series(df, '_v2-stats-wasm_both', 'p99')
    latency_v2_stats_nullvm_both_p99 = get_latency_vs_conn_y_series(df, '_v2-stats-nullvm_both', 'p99')
    latency_v2_sd_full_nullvm_both_p99 = get_latency_vs_conn_y_series(df, '_v2-sd-full-nullvm_both', 'p99')
    latency_v2_sd_nologging_nullvm_both_p99 = get_latency_vs_conn_y_series(df, '_v2-sd-nologging-nullvm_both', 'p99')

    latency_p99_list = [latency_none_mtls_baseline_p99, latency_none_mtls_both_p99, latency_v2_stats_wasm_both_p99,
                        latency_v2_stats_nullvm_both_p99,
                        latency_v2_sd_full_nullvm_both_p99, latency_v2_sd_nologging_nullvm_both_p99]

    print(latency_p99_list)
    draw_p99(latency_p99_list)

def get_latency_vs_conn_y_series(df, mixer_mode, quantiles):
    y_series_data = []
    for thread in [2, 4, 8, 16, 32, 64]:
        data = df.query('ActualQPS == 1000 and NumThreads == @thread and Labels.str.endswith(@mixer_mode)')
        if not data[quantiles].head().empty:
            y_series_data.append(data[quantiles].head(1).values[0])
        else:
            y_series_data.append('null')
    return y_series_data


latency_vs_conn()