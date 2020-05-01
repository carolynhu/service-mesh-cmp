import json
import math
import glob
import csv


def parse_fortio_json(file_name):
    # read file
    with open(file_name, 'r') as json_file:
        data = json_file.read()

    # parse file
    obj = json.loads(data)
    # obj = "{'RunType': 'HTTP', 'Labels': 'cff63081_qps_1000_c_16_1024_mixer_both', 'StartTime': '2020-02-11T20:57:42.100843708Z', 'RequestedQPS': '1000', 'RequestedDuration': '4m0s', 'ActualQPS': 999.980782406823, 'ActualDuration': 240004612311, 'NumThreads': 16, 'Version': '1.3.2-pre', 'DurationHistogram': {'Count': 240000, 'Min': 0.001319145, 'Max': 0.008643753, 'Sum': 933.7981637779999, 'Avg': 0.003890825682408333, 'StdDev': 0.0009336343061967972, 'Data': [{'Start': 0.001319145, 'End': 0.0015, 'Percent': 0.19583333333333333, 'Count': 470}, {'Start': 0.0015, 'End': 0.00175, 'Percent': 0.75375, 'Count': 1339}, {'Start': 0.00175, 'End': 0.002, 'Percent': 1.3066666666666666, 'Count': 1327}, {'Start': 0.002, 'End': 0.0022500000000000003, 'Percent': 1.9020833333333333, 'Count': 1429}, {'Start': 0.0022500000000000003, 'End': 0.0025, 'Percent': 4.234166666666667, 'Count': 5597}, {'Start': 0.0025, 'End': 0.003, 'Percent': 19.692916666666665, 'Count': 37101}, {'Start': 0.003, 'End': 0.0035, 'Percent': 35.975833333333334, 'Count': 39079}, {'Start': 0.0035, 'End': 0.004, 'Percent': 54.232083333333335, 'Count': 43815}, {'Start': 0.004, 'End': 0.0045000000000000005, 'Percent': 76.73708333333333, 'Count': 54012}, {'Start': 0.0045000000000000005, 'End': 0.005, 'Percent': 86.76166666666667, 'Count': 24059}, {'Start': 0.005, 'End': 0.006, 'Percent': 98.60833333333333, 'Count': 28432}, {'Start': 0.006, 'End': 0.007, 'Percent': 99.95625, 'Count': 3235}, {'Start': 0.007, 'End': 0.008, 'Percent': 99.99333333333334, 'Count': 89}, {'Start': 0.008, 'End': 0.008643753, 'Percent': 100, 'Count': 16}], 'Percentiles': [{'Percentile': 50, 'Value': 0.003884092205865571}, {'Percentile': 75, 'Value': 0.004461406724431609}, {'Percentile': 90, 'Value': 0.00527335396736072}, {'Percentile': 99, 'Value': 0.006290571870170016}, {'Percentile': 99.9, 'Value': 0.0069582689335394195}]}, 'Exactly': 0, 'Jitter': False, 'RetCodes': {'200': 240000}, 'Sizes': {'Count': 240000, 'Min': 1191, 'Max': 1191, 'Sum': 285840000, 'Avg': 1191, 'StdDev': 0, 'Data': [{'Start': 1191, 'End': 1191, 'Percent': 100, 'Count': 240000}], 'Percentiles': None}, 'HeaderSizes': {'Count': 240000, 'Min': 167, 'Max': 167, 'Sum': 40080000, 'Avg': 167, 'StdDev': 0, 'Data': [{'Start': 167, 'End': 167, 'Percent': 100, 'Count': 240000}], 'Percentiles': None}, 'URL': 'http://fortioserver:8080/echo?size=1024', 'SocketCount': 16, 'AbortOn': 0}"
    # print(obj)
    # show values
    start_time = str(obj['StartTime'])
    actual_duration = str(int((obj['ActualDuration']/1000000000)))
    labels = str(obj['Labels'])
    num_threads = str(obj['NumThreads'])
    actual_QPS = str(math.ceil(obj['ActualQPS']))
    percentiles = obj['DurationHistogram']['Percentiles']

    # start_time = str(obj.get('StartTime'))
    # actual_duration = str(int((obj.get('ActualDuration') / 1000000000)))
    # labels = str(obj.get('Labels'))
    # num_threads = str(obj.get('NumThreads'))
    # actual_QPS = str(math.ceil(obj.get('ActualQPS')))
    # percentiles = obj.get('DurationHistogram').get('Percentiles')

    if "_nighthawk_" in file_name:
        p50 = round(percentiles[0]['Value'] * 1000, 3)  # ms
        p90 = round(percentiles[3]['Value'] * 1000, 3)
        p99 = round(percentiles[5]['Value'] * 1000, 3)
        p99_9 = round(percentiles[6]['Value'] * 1000, 3)
    else:
        p50 = round(percentiles[0]['Value'] * 1000, 3)  # ms
        p90 = round(percentiles[2]['Value'] * 1000, 3)
        p99 = round(percentiles[3]['Value'] * 1000, 3)
        p99_9 = round(percentiles[4]['Value'] * 1000, 3)
    perf_row_list = [start_time, actual_duration, labels, num_threads, actual_QPS, p50, p90, p99, p99_9]
    return perf_row_list


def write_perf_number_to_csv(perf_num_list):
    with open('istio-1.6-20891.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['StartTime', 'ActualDuration', 'Labels', 'NumThreads', 'ActualQPS', 'p50', 'p90', 'p99', 'p99.9'])
        for lst in perf_num_list:
            writer.writerow([lst[0], lst[1], lst[2], lst[3], lst[4], lst[5], lst[6], lst[7], lst[8]])


def parse_perf_num():
    fortio_json_file_path = "/Users/carolynprh/PR_20891_2nd_run/rawdata/"    # fill out the folder path of all your fortio format json files
    perf_num_list = []
    for file_name in glob.glob(fortio_json_file_path + "/*.json"):
        # print(file_name)
        perf_row_list = parse_fortio_json(file_name)
        perf_num_list.append(perf_row_list)
    # print(perf_num_list)
    write_perf_number_to_csv(perf_num_list)


parse_perf_num()
