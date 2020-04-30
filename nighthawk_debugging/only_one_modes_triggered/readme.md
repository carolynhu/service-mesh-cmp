I ran this command 

```bash
(runner) bash-3.2$ python runner.py --conn 2,4,8,16,32,64 --qps 1000 --duration 240 --baseline --load_gen_type=nighthawk --telemetry_mode=v2-nullvm
```

1. but I only collected [both mode data](./istio_1_6_p99_nighthawk.csv). No other modes.
2. [latency graph](./istio_1_6_p99_nighthawk.png) almost no changes after conn=8
